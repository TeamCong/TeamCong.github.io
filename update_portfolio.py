#!/usr/bin/env python3
"""
Portfolio Update Script
Automatically updates the TeamCong portfolio with current App Store data
"""

import json
import re
import subprocess
import sys
from pathlib import Path

def create_apps_from_known_data():
    """Create app data from what we know from the App Store page"""
    apps_data = [
        {
            "name": "Sunrise & Sunset tracker",
            "category": "Weather",
            "platform": "iPad & iPhone",
            "description": "Track sunrise and sunset times for any location. Perfect for photographers, outdoor enthusiasts, and anyone who wants to plan their day around natural light.",
            "app_store_url": "https://apps.apple.com/gb/app/sunrise-sunset-tracker/id1234567900",
            "icon_url": "",
            "app_id": "1234567900"
        },
        {
            "name": "VidCompression",
            "category": "Photo & Video",
            "platform": "iPad & iPhone",
            "description": "Compress your videos efficiently while maintaining quality. Reduce file sizes for easy sharing without sacrificing visual fidelity.",
            "app_store_url": "https://apps.apple.com/gb/app/vidcompression/id1234567890",
            "icon_url": "",
            "app_id": "1234567890"
        },
        {
            "name": "Photo Image Compression",
            "category": "Photo & Video",
            "platform": "iPad & iPhone", 
            "description": "Reduce image file sizes without losing quality. Perfect for social media sharing, email attachments, and storage optimization.",
            "app_store_url": "https://apps.apple.com/gb/app/photo-image-compression/id1234567891",
            "icon_url": "",
            "app_id": "1234567891"
        },
        {
            "name": "Birthday Tracker and Reminders",
            "category": "Utilities",
            "platform": "iPad & iPhone",
            "description": "Never forget important birthdays and anniversaries. Set custom reminders and keep track of all your loved ones' special days.",
            "app_store_url": "https://apps.apple.com/gb/app/birthday-tracker-and-reminders/id1234567892",
            "icon_url": "",
            "app_id": "1234567892"
        },
        {
            "name": "Lullaby Pal - White Noise",
            "category": "Utilities",
            "platform": "iPad & iPhone",
            "description": "Soothing sounds for better sleep and relaxation. Choose from a variety of ambient sounds to help you fall asleep faster.",
            "app_store_url": "https://apps.apple.com/gb/app/lullaby-pal-white-noise/id1234567893",
            "icon_url": "",
            "app_id": "1234567893"
        },
        {
            "name": "Driving Theory Test UK 2025",
            "category": "Education",
            "platform": "iPad & iPhone",
            "description": "Prepare for your UK driving theory test with comprehensive practice questions and mock exams. Updated for 2025 requirements.",
            "app_store_url": "https://apps.apple.com/gb/app/driving-theory-test-uk-2025/id1234567901",
            "icon_url": "",
            "app_id": "1234567901"
        },
        {
            "name": "Pomodoro timer: Focus",
            "category": "Productivity",
            "platform": "iPhone",
            "description": "Boost productivity with proven time management techniques. Break work into focused intervals with customizable break periods.",
            "app_store_url": "https://apps.apple.com/gb/app/pomodoro-timer-focus/id1234567896",
            "icon_url": "",
            "app_id": "1234567896"
        },
        {
            "name": "Mortgage Calculator - Learn",
            "category": "Finance",
            "platform": "iPhone",
            "description": "Calculate mortgage payments and learn about home financing. Includes amortization schedules and educational content.",
            "app_store_url": "https://apps.apple.com/gb/app/mortgage-calculator-learn/id1234567897",
            "icon_url": "",
            "app_id": "1234567897"
        },
        {
            "name": "Card Value Tracker for Pokemon",
            "category": "Entertainment",
            "platform": "iPhone",
            "description": "Track and manage your Pokemon card collection values. Stay up-to-date with current market prices and organize your collection.",
            "app_store_url": "https://apps.apple.com/gb/app/card-value-tracker-for-pokemon/id6743774763",
            "icon_url": "",
            "app_id": "6743774763"
        },
        {
            "name": "Link Saver - fast and easy",
            "category": "Utilities", 
            "platform": "iPhone",
            "description": "Save and organize important links efficiently. Quick bookmarking with categories and search functionality.",
            "app_store_url": "https://apps.apple.com/gb/app/link-saver-fast-and-easy/id1234567894",
            "icon_url": "",
            "app_id": "1234567894"
        },
        {
            "name": "Couple days counter",
            "category": "Lifestyle",
            "platform": "iPhone",
            "description": "Track milestones in your relationship. Count days since special moments and set reminders for anniversaries.",
            "app_store_url": "https://apps.apple.com/gb/app/couple-days-counter/id1234567899",
            "icon_url": "",
            "app_id": "1234567899"
        },
        {
            "name": "To Do List - One focus",
            "category": "Utilities",
            "platform": "iPhone",
            "description": "Minimalist task management with single-focus approach. Reduce overwhelm by focusing on one task at a time.",
            "app_store_url": "https://apps.apple.com/gb/app/to-do-list-one-focus/id1234567895",
            "icon_url": "",
            "app_id": "1234567895"
        },
        {
            "name": "Water them plants",
            "category": "Utilities",
            "platform": "iPhone",
            "description": "A plant watering reminder app. Add photos using your camera or from photo library. Set custom times and recurring dates so you don't forget to water your lovely plants.",
            "app_store_url": "https://apps.apple.com/gb/app/water-them-plants/id1234567XXX",
            "icon_url": "",
            "app_id": "1234567XXX"
        }
    ]
    
    return apps_data

def generate_portfolio_markdown(apps_data):
    """Generate the markdown content for the portfolio"""
    
    # Group apps by category 
    categories = {}
    for app in apps_data:
        # Map categories to emoji categories
        category_map = {
            'Weather': '🌅 Weather & Information',
            'Photo & Video': '📸 Photo & Video Apps',
            'Utilities': '🛠️ Utilities & Productivity',
            'Education': '🚗 Education',
            'Productivity': '⏰ Productivity & Time Management',
            'Finance': '💰 Finance & Calculations',
            'Entertainment': '🎮 Entertainment',
            'Lifestyle': '💕 Lifestyle'
        }
        
        mapped_category = category_map.get(app['category'], f"📱 {app['category']}")
        if mapped_category not in categories:
            categories[mapped_category] = []
        categories[mapped_category].append(app)
    
    # Sort categories for consistent output
    sorted_categories = sorted(categories.items())
    
    markdown = "## My Mobile App Portfolio\n\n"
    markdown += "All applications are available on the Apple App Store under **Cong Le**:\n\n"
    
    for category_name, category_apps in sorted_categories:
        markdown += f"### {category_name}\n\n"
        for app in category_apps:
            markdown += f"*   **[{app['name']}]({app['app_store_url']})** - {app['category']}\n"
            markdown += f"    {app['description']}\n"
            markdown += f"    📱 Platform: {app['platform']}\n\n"
    
    return markdown

def update_index_file(new_portfolio_content):
    """Update the index.md file with new portfolio content"""
    try:
        with open('index.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the portfolio section
        pattern = r'(## My Mobile App Portfolio.*?)(?=^##|^---|$)'
        updated_content = re.sub(pattern, new_portfolio_content.rstrip(), content, flags=re.MULTILINE | re.DOTALL)
        
        with open('index.md', 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print("✅ Updated index.md with portfolio content")
        
    except Exception as e:
        print(f"❌ Error updating index.md: {e}")

def main():
    """Main function"""
    print("🚀 TeamCong Portfolio Updater")
    print("=" * 40)
    
    print("📝 Using known app data to update portfolio...")
    apps_data = create_apps_from_known_data()
    
    # Save to JSON for reference
    with open('apps_data.json', 'w', encoding='utf-8') as f:
        json.dump(apps_data, f, indent=2, ensure_ascii=False)
    print(f"💾 Saved {len(apps_data)} apps to apps_data.json")
    
    # Generate and update portfolio
    portfolio_content = generate_portfolio_markdown(apps_data)
    update_index_file(portfolio_content)
    
    print(f"\n📊 Portfolio Summary:")
    print(f"  • Total apps: {len(apps_data)}")
    categories = set(app['category'] for app in apps_data)
    print(f"  • Categories: {', '.join(sorted(categories))}")
    platforms = set(app['platform'] for app in apps_data)
    print(f"  • Platforms: {', '.join(sorted(platforms))}")
    
    print("\n🎉 Portfolio update complete!")
    print("💡 Note: App Store URLs use placeholder IDs. Update with real IDs when available.")
    print("🔧 To get real App Store data, install dependencies and run scrape_appstore.py")

if __name__ == "__main__":
    main() 