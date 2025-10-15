import json

def generate_featured_app_html(app):
    return f"""
<div style="display: flex; align-items: center; margin-bottom: 2em;">
  <img src="{app['icon_url']}" alt="{app['name']} Icon" style="width: 150px; height: 150px; border-radius: 22.5%; margin-right: 2em;">
  <div>
    <h4><a href="{app['app_store_url']}">{app['name']}</a></h4>
    <p><strong>{app['category']}</strong> | 📱 {app['platform']}</p>
    <p>{app['description']}</p>
  </div>
</div>
"""

def generate_app_collection_html(apps):
    # Group apps by category
    categories = {}
    for app in apps:
        category = app.get('category', 'Unknown')
        if category not in categories:
            categories[category] = []
        categories[category].append(app)

    html = ""
    for category, apps_in_category in categories.items():
        html += f"### {category}\n\n"
        html += '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 2em;">\n'
        for app in apps_in_category:
            html += f"""
<div style="text-align: center;">
  <a href="{app['app_store_url']}">
    <img src="{app['icon_url']}" alt="{app['name']} Icon" style="width: 100px; height: 100px; border-radius: 22.5%;">
  </a>
  <h5 style="margin-top: 0.5em;"><a href="{app['app_store_url']}">{app['name']}</a></h5>
</div>
"""
        html += '</div>\n\n'
    return html

def main():
    with open('apps_data.json', 'r') as f:
        apps = json.load(f)

    # Find Anniversary Tracker to feature it
    featured_app = next((app for app in apps if app['name'] == 'Anniversary Tracker'), None)

    if featured_app:
        other_apps = [app for app in apps if app['name'] != 'Anniversary Tracker']
    else:
        # Default to the first app if Anniversary Tracker is not found
        featured_app = apps[0]
        other_apps = apps[1:]

    featured_app_html = generate_featured_app_html(featured_app)
    app_collection_html = generate_app_collection_html(other_apps)

    with open('index.md', 'r') as f:
        content = f.read()

    # Replace featured app section
    start_featured = content.find('### 🏆 Featured App')
    end_featured = content.find('---', start_featured)

    new_content = content[:start_featured] + '### 🏆 Featured App\n\n' + featured_app_html + '\n' + content[end_featured:]

    # Replace app collection section
    start_collection = new_content.find('## 📱 Complete App Collection')
    end_collection = new_content.find('---', start_collection)

    final_content = new_content[:start_collection] + '## 📱 Complete App Collection\n\n' + app_collection_html + new_content[end_collection:]

    with open('index.md', 'w') as f:
        f.write(final_content)

if __name__ == '__main__':
    main()
