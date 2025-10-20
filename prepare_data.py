import json
import re

def extract_experiences(cv_content):
    experiences = []
    lines = cv_content.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('### '):
            title = lines[i][4:]
            if i + 2 >= len(lines):
                i += 1
                continue
            company_line = lines[i+1]
            company = company_line.split('|')[0].strip().replace('**', '')
            period = lines[i+2].strip().replace('*', '')
            description_lines = []
            i += 4
            while i < len(lines) and not lines[i].startswith('### ') and not lines[i].startswith('---'):
                description_lines.append(lines[i])
                i += 1
            description = '\n'.join(description_lines).strip()
            experiences.append({
                "id": len(experiences) + 1,
                "title": title,
                "company": company,
                "period": period,
                "description": description
            })
        else:
            i += 1
    return experiences

def extract_skills(cv_content):
    skills = []
    skill_names = set()
    lines = cv_content.split('\n')
    for line in lines:
        if line.startswith('- **'):
            parts = line.split('**')
            if len(parts) > 1:
                name = parts[1]
                if name not in skill_names:
                    level = 90 # Placeholder
                    skills.append({
                        "name": name,
                        "level": level
                    })
                    skill_names.add(name)
    return skills

def main():
    with open('apps_data.json', 'r') as f:
        apps = json.load(f)

    with open('cv.md', 'r') as f:
        cv_content = f.read()

    experiences = extract_experiences(cv_content)
    skills = extract_skills(cv_content)

    for app in apps:
        app['id'] = app.get('app_id')
        app['rating'] = 4.5 # Placeholder
        app['downloads'] = "100K+" # Placeholder
        app['price'] = "Free" # Placeholder
        app['screenshots'] = 3 # Placeholder


    portfolio_data = {
        "apps": apps,
        "experiences": experiences,
        "skills": skills
    }

    with open('react-portfolio/src/portfolio_data.json', 'w') as f:
        json.dump(portfolio_data, f, indent=2)

if __name__ == '__main__':
    main()
