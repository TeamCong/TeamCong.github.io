#!/usr/bin/env python3
"""
TeamCong App Store Scraper
Scrapes app information from the Apple App Store developer page to automatically
update the portfolio website with current app data.
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin
import time
from dataclasses import dataclass
from typing import List, Optional
import argparse

@dataclass
class App:
    """Represents an app with its metadata"""
    name: str
    category: str
    platform: str
    description: str = ""
    app_store_url: str = ""
    icon_url: str = ""
    app_id: str = ""

class AppStoreScraper:
    """Scrapes TeamCong apps from the Apple App Store developer page"""
    
    def __init__(self):
        self.developer_url = "https://apps.apple.com/gb/developer/cong-le/id954373766"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
    
    def scrape_developer_page(self) -> List[App]:
        """Scrape the main developer page to get app list"""
        try:
            print(f"🔍 Scraping developer page: {self.developer_url}")
            response = self.session.get(self.developer_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            apps = []
            
            # Find app sections
            app_sections = soup.find_all('section', class_='l-content-width')
            
            for section in app_sections:
                platform_header = section.find('h2')
                if not platform_header:
                    continue
                    
                platform = platform_header.get_text(strip=True)
                print(f"📱 Found platform: {platform}")
                
                # Find all app links in this section
                app_links = section.find_all('a', href=re.compile(r'/app/'))
                
                for link in app_links:
                    app_url = urljoin('https://apps.apple.com', link.get('href'))
                    
                    # Extract app name and category from the link structure
                    app_name_elem = link.find('h3')
                    if app_name_elem:
                        app_name = app_name_elem.get_text(strip=True)
                    else:
                        # Fallback: extract from URL
                        app_name = link.get('href').split('/')[-2].replace('-', ' ').title()
                    
                    # Try to find category
                    category_elem = link.find('p', class_='we-truncate--single-line')
                    category = category_elem.get_text(strip=True) if category_elem else "Unknown"
                    
                    # Extract app ID from URL
                    app_id_match = re.search(r'id(\d+)', app_url)
                    app_id = app_id_match.group(1) if app_id_match else ""
                    
                    app = App(
                        name=app_name,
                        category=category,
                        platform=platform,
                        app_store_url=app_url,
                        app_id=app_id
                    )
                    
                    apps.append(app)
                    print(f"  ✅ Found: {app_name} ({category})")
                    
                    # Be respectful with requests
                    time.sleep(0.5)
            
            return apps
            
        except Exception as e:
            print(f"❌ Error scraping developer page: {e}")
            return []
    
    def get_app_details(self, app: App) -> App:
        """Get detailed information for a specific app"""
        try:
            print(f"🔍 Getting details for: {app.name}")
            response = self.session.get(app.app_store_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try to find app description
            description_elem = soup.find('div', class_='section__description')
            if description_elem:
                app.description = description_elem.get_text(strip=True)[:200] + "..."
            
            # Try to find app icon
            icon_elem = soup.find('picture', class_='we-artwork')
            if icon_elem:
                img_elem = icon_elem.find('img')
                if img_elem and img_elem.get('src'):
                    app.icon_url = img_elem['src']
            
            time.sleep(1)  # Be respectful
            return app
            
        except Exception as e:
            print(f"⚠️  Could not get details for {app.name}: {e}")
            return app
    
    def scrape_all_apps(self, get_details: bool = False) -> List[App]:
        """Scrape all apps from the developer page"""
        apps = self.scrape_developer_page()
        
        if get_details:
            print("\n📋 Getting detailed information for each app...")
            for i, app in enumerate(apps):
                apps[i] = self.get_app_details(app)
        
        return apps
    
    def save_to_json(self, apps: List[App], filename: str = "apps_data.json"):
        """Save apps data to JSON file"""
        apps_dict = [app.__dict__ for app in apps]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(apps_dict, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved {len(apps)} apps to {filename}")

def generate_markdown_portfolio(apps: List[App]) -> str:
    """Generate markdown content for the portfolio section"""
    
    # Group apps by category for better organization
    categories = {}
    for app in apps:
        # Map categories to emoji categories
        category_map = {
            'Weather': '🌅 Weather & Lifestyle',
            'Photo & Video': '📸 Photo & Video',
            'Utilities': '🛠️ Utilities',
            'Education': '🚗 Education',
            'Productivity': '⏰ Productivity',
            'Finance': '💰 Finance',
            'Entertainment': '🎮 Entertainment',
            'Lifestyle': '💕 Lifestyle'
        }
        
        mapped_category = category_map.get(app.category, f"📱 {app.category}")
        if mapped_category not in categories:
            categories[mapped_category] = []
        categories[mapped_category].append(app)
    
    markdown = "## Our Mobile Apps\n\n"
    markdown += "Our collection of mobile applications available on the App Store:\n\n"
    
    for category, category_apps in categories.items():
        markdown += f"### {category}\n\n"
        for app in category_apps:
            # Create a rich app entry with store link
            markdown += f"*   **[{app.name}]({app.app_store_url})** - {app.category}"
            if app.description:
                markdown += f"\n    {app.description[:100]}..."
            markdown += f"\n    📱 Platform: {app.platform}\n\n"
    
    return markdown

def update_index_md(apps: List[App]):
    """Update the index.md file with current app data"""
    try:
        # Read current index.md
        with open('index.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate new portfolio section
        new_portfolio = generate_markdown_portfolio(apps)
        
        # Replace the apps section (between "## Our Mobile Apps" and the next "##" or "---")
        pattern = r'(## Our Mobile Apps.*?)(?=^##|^---|$)'
        replacement = new_portfolio.rstrip()
        
        updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
        
        # Write back to file
        with open('index.md', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ Updated index.md with current app data")
        
    except Exception as e:
        print(f"❌ Error updating index.md: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Scrape TeamCong apps from App Store')
    parser.add_argument('--details', '-d', action='store_true', 
                       help='Get detailed information for each app (slower)')
    parser.add_argument('--update-md', '-u', action='store_true',
                       help='Update index.md with scraped data')
    parser.add_argument('--output', '-o', default='apps_data.json',
                       help='Output JSON file (default: apps_data.json)')
    
    args = parser.parse_args()
    
    print("🍎 TeamCong App Store Scraper")
    print("=" * 40)
    
    scraper = AppStoreScraper()
    apps = scraper.scrape_all_apps(get_details=args.details)
    
    if apps:
        print(f"\n✅ Successfully scraped {len(apps)} apps")
        
        # Save to JSON
        scraper.save_to_json(apps, args.output)
        
        # Update markdown if requested
        if args.update_md:
            update_index_md(apps)
        
        # Print summary
        print("\n📊 Apps Summary:")
        for app in apps:
            print(f"  • {app.name} ({app.category}) - {app.platform}")
    
    else:
        print("❌ No apps found")

if __name__ == "__main__":
    main() 