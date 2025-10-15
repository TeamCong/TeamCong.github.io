import json

def generate_featured_project_html(app):
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

def generate_app_portfolio_html(apps):
    html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 2em;">\\n'
    for app in apps:
        html += f"""
<div style="text-align: center;">
  <a href="{app['app_store_url']}">
    <img src="{app['icon_url']}" alt="{app['name']} Icon" style="width: 100px; height: 100px; border-radius: 22.5%;">
  </a>
  <h5 style="margin-top: 0.5em;"><a href="{app['app_store_url']}">{app['name']}</a></h5>
</div>
"""
    html += '</div>\\n'
    return html

def main():
    with open('apps_data.json', 'r') as f:
        apps = json.load(f)

    # For now, let's feature the first app and list the rest.
    featured_app = apps[0]
    other_apps = apps[1:]

    featured_project_html = generate_featured_project_html(featured_app)
    app_portfolio_html = generate_app_portfolio_html(other_apps)

    with open('portfolio.md', 'r') as f:
        content = f.read()

    # Replace featured project section
    start_featured = content.find('## 🌟 Featured Personal Project')
    end_featured = content.find('---', start_featured)

    new_content = content[:start_featured] + '## 🌟 Featured Personal Project\\n\\n' + featured_project_html + '\\n' + content[end_featured:]

    # Replace app portfolio section
    start_portfolio = new_content.find('## My Personal App Portfolio')
    end_portfolio = new_content.find('---', start_portfolio)

    final_content = new_content[:start_portfolio] + '## My Personal App Portfolio\\n\\n' + app_portfolio_html + new_content[end_portfolio:]

    with open('portfolio.md', 'w') as f:
        f.write(final_content)

if __name__ == '__main__':
    main()
