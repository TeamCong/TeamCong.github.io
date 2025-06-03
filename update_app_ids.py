#!/usr/bin/env python3
"""
App ID Updater Script
Helps update the portfolio with real App Store IDs instead of placeholders
"""

import re
import json

# Real App Store IDs - update these with the actual IDs from your apps
REAL_APP_IDS = {
    "Card Value Tracker for Pokemon": "6743774763",  # Already updated
    "Anniversary Tracker": "XXXXXXXXX",  # Replace with real ID
    "Couple days counter": "XXXXXXXXX",  # Replace with real ID
    "Water them plants": "XXXXXXXXX",    # Replace with real ID
    "Fish Run - Collect stars": "XXXXXXXXX",  # Replace with real ID
    "Run Run Run": "XXXXXXXXX",          # Replace with real ID
    "Sunrise & Sunset tracker": "XXXXXXXXX",  # Replace with real ID
    "VidCompression": "XXXXXXXXX",       # Replace with real ID
    "Photo Image Compression": "XXXXXXXXX",  # Replace with real ID
    "Birthday Tracker and Reminders": "XXXXXXXXX",  # Replace with real ID
    "Lullaby Pal - White Noise": "XXXXXXXXX",  # Replace with real ID
    "Driving Theory Test UK 2025": "XXXXXXXXX",  # Replace with real ID
    "Pomodoro timer: Focus": "XXXXXXXXX",  # Replace with real ID
    "Mortgage Calculator - Learn": "XXXXXXXXX",  # Replace with real ID
    "Link Saver - fast and easy": "XXXXXXXXX",  # Replace with real ID
    "To Do List - One focus": "XXXXXXXXX",  # Replace with real ID
}

def update_app_ids_in_file(filename):
    """Update App Store IDs in a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        updates_made = 0
        
        for app_name, real_id in REAL_APP_IDS.items():
            if real_id == "XXXXXXXXX":
                continue  # Skip placeholder IDs
                
            # Pattern to match app store URLs with placeholder IDs
            pattern = rf'(https://apps\.apple\.com/gb/app/[^/]+/id)\d+XXX?'
            
            # Find lines containing the app name
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if app_name in line and 'apps.apple.com' in line:
                    # Update the ID in this line
                    updated_line = re.sub(pattern, rf'\g<1>{real_id}', line)
                    if updated_line != line:
                        lines[i] = updated_line
                        updates_made += 1
                        print(f"✅ Updated {app_name}: id{real_id}")
        
        content = '\n'.join(lines)
        
        if updates_made > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n💾 Updated {filename} with {updates_made} app ID changes")
        else:
            print(f"ℹ️  No updates needed for {filename}")
            
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

def show_app_id_instructions():
    """Show instructions for finding real App Store IDs"""
    print("📱 How to Find Real App Store IDs:")
    print("=" * 50)
    print("1. Go to your App Store developer page:")
    print("   https://apps.apple.com/gb/developer/cong-le/id954373766")
    print("\n2. Click on each app to go to its individual page")
    print("\n3. Look at the URL - the ID is the number after 'id'")
    print("   Example: https://apps.apple.com/gb/app/card-value-tracker-for-pokemon/id6743774763")
    print("   The ID is: 6743774763")
    print("\n4. Update the REAL_APP_IDS dictionary in this script")
    print("\n5. Run the script again to update all files")
    print("\n📋 Apps needing real IDs:")
    
    for app_name, app_id in REAL_APP_IDS.items():
        status = "✅ Set" if app_id != "XXXXXXXXX" else "❌ Needs real ID"
        print(f"   • {app_name}: {status}")

def main():
    """Main function"""
    print("🔄 App Store ID Updater")
    print("=" * 30)
    
    # Show current status
    show_app_id_instructions()
    
    print("\n" + "=" * 50)
    
    # Count how many real IDs we have
    real_ids = sum(1 for id in REAL_APP_IDS.values() if id != "XXXXXXXXX")
    total_apps = len(REAL_APP_IDS)
    
    if real_ids == 0:
        print("⚠️  No real App Store IDs configured yet.")
        print("📝 Please update the REAL_APP_IDS dictionary in this script first.")
        return
    
    print(f"🎯 Found {real_ids}/{total_apps} real App Store IDs configured")
    
    # Update files
    files_to_update = ['index.md', 'update_portfolio.py']
    
    for filename in files_to_update:
        print(f"\n🔄 Updating {filename}...")
        update_app_ids_in_file(filename)
    
    print(f"\n🎉 App ID update complete!")
    print(f"📊 {real_ids} apps have real IDs, {total_apps - real_ids} still need updating")

if __name__ == "__main__":
    main() 