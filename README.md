# TeamCong Portfolio & GitHub Pages

**Professional mobile app developer portfolio hosted on GitHub Pages**

🌐 **Live Site**: [https://teamcong.github.io](https://teamcong.github.io)  
🍎 **App Store**: [Cong Le Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)

## 🎯 Purpose

This repository serves multiple purposes:

- **📱 Portfolio**: Professional showcase of all TeamCong mobile applications
- **📋 Legal Hub**: Privacy Policy and Terms & Conditions for all apps
- **📺 Ad Network**: `app-ads.txt` file for AdMob and other advertising partners
- **🔗 Central Reference**: Canonical URLs for app submissions and legal compliance

## 📁 Repository Structure

```
├── index.md                    # Main portfolio page
├── privacy.md                  # Privacy policy for all apps
├── terms.md                    # Terms and conditions for all apps
├── app-ads.txt                 # Ad network authorization file
├── _config.yml                 # Jekyll configuration
├── .cursorrules               # Development guidelines
├── scrape_appstore.py         # App Store data scraper
├── update_portfolio.py        # Portfolio update automation
├── requirements.txt           # Python dependencies
├── Makefile                   # Automation commands
├── DEPLOYMENT_CHECKLIST.md    # Deployment guide
└── README.md                  # This file
```

## 🚀 Quick Start

### Option 1: Using Make (Recommended)
```bash
# Install dependencies and update portfolio
make setup

# Update portfolio with latest app data
make update-portfolio

# Deploy to GitHub Pages
make deploy
```

### Option 2: Manual Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Update portfolio with current app data
python update_portfolio.py

# Deploy changes
git add .
git commit -m "feat: Update portfolio"
git push origin main
```

## 📱 App Portfolio

The portfolio currently showcases **12 published iOS applications**:

### 📸 Photo & Video Apps
- **VidCompression** - Video compression tool
- **Photo Image Compression** - Image optimization

### 🛠️ Utilities & Productivity  
- **Birthday Tracker and Reminders** - Birthday management
- **Lullaby Pal - White Noise** - Sleep sounds
- **Link Saver - fast and easy** - Bookmark management
- **To Do List - One focus** - Minimalist task management

### ⏰ Productivity & Time Management
- **Pomodoro timer: Focus** - Time management

### 💰 Finance & Calculations
- **Mortgage Calculator - Learn** - Financial calculations

### 🎮 Entertainment
- **Card Value Tracker for Pokemon** - Trading card management

### 💕 Lifestyle
- **Couple days counter** - Relationship milestones

### 🌅 Weather & Information
- **Sunrise & Sunset tracker** - Solar tracking

### 🚗 Education
- **Driving Theory Test UK 2025** - UK driving test prep

## 🔧 Automation Features

### Portfolio Updates
The system includes automated tools to keep the portfolio current:

- **`scrape_appstore.py`**: Scrapes live App Store data
- **`update_portfolio.py`**: Updates portfolio with current app information
- **`Makefile`**: Provides easy command-line automation

### Available Commands
```bash
make help              # Show all available commands
make install           # Install dependencies
make update-portfolio  # Update with current app data
make scrape           # Scrape live App Store data
make validate         # Validate markdown files
make deploy           # Deploy to GitHub Pages
make status           # Show current portfolio status
make serve            # Start local development server
```

## 🔗 Key URLs

When deployed, the following URLs are available:

- **Portfolio**: `https://teamcong.github.io/`
- **Privacy Policy**: `https://teamcong.github.io/privacy`
- **Terms & Conditions**: `https://teamcong.github.io/terms`
- **App-Ads.txt**: `https://teamcong.github.io/app-ads.txt`

## ⚙️ Configuration

### Before Deployment

1. **Update `app-ads.txt`**:
   ```
   # Replace with your actual Google AdMob Publisher ID
   google.com, pub-YOUR_ACTUAL_PUBLISHER_ID, DIRECT, f08c47fec0942fa0
   ```

2. **Verify Contact Email**:
   - Ensure `anniversarytrackerteamcong@gmail.com` is active
   - Update in all files if needed

3. **Legal Review**:
   - Have privacy policy and terms reviewed by legal counsel
   - Ensure compliance with GDPR, CCPA, and app store policies

### GitHub Pages Setup

1. Create repository named `TeamCong.github.io` under your organization
2. Set repository to **Public** visibility
3. Go to Settings → Pages
4. Set source to "Deploy from a branch" 
5. Set branch to `main` and folder to `/ (root)`
6. Push all files to main branch

## 📊 Portfolio Features

### Professional Presentation
- Clean, modern design optimized for mobile and desktop
- Organized by app categories with emoji icons
- Direct links to App Store listings
- Platform indicators (iPhone/iPad)
- App descriptions and key features

### SEO Optimized
- Proper Jekyll front matter and metadata
- Search engine friendly URLs
- Social media meta tags
- Structured data for better indexing

### Easy Maintenance
- Automated data updates from App Store
- Version-controlled documentation
- Simple deployment process
- Comprehensive checklists

## 🔄 Updating Your Apps

After deployment, update each app to use these URLs:

### In App Store Connect:
- Privacy Policy URL: `https://teamcong.github.io/privacy`
- Terms & Conditions URL: `https://teamcong.github.io/terms`

### In App Code (if applicable):
- Update hardcoded policy links in settings screens
- Test links in development builds
- Submit app updates where necessary

## 🛠️ Development

### Local Development
```bash
# Install Jekyll (optional)
gem install bundler jekyll

# Serve locally
make serve
# or
bundle exec jekyll serve --livereload
```

### Adding New Apps
1. Update the app data in `update_portfolio.py`
2. Run `make update-portfolio`
3. Review changes and deploy

### Updating Content
1. Edit relevant markdown files
2. Run `make validate` to check syntax
3. Deploy with `make deploy`

## 📋 Maintenance Schedule

### Monthly
- [ ] Check all links work correctly
- [ ] Monitor AdMob for `app-ads.txt` status
- [ ] Run `make status` to verify setup

### Quarterly
- [ ] Review app list and descriptions
- [ ] Update portfolio with new apps
- [ ] Run `make scrape` to get latest data

### Annually
- [ ] Review and update privacy policy
- [ ] Review and update terms and conditions  
- [ ] Update "Last Updated" dates
- [ ] Legal compliance review

## 🚨 Important Notes

1. **Legal Compliance**: The privacy policy and terms are templates. Consider legal review for compliance with applicable laws.

2. **Contact Email**: Ensure `anniversarytrackerteamcong@gmail.com` is active before going live.

3. **Publisher ID**: The `app-ads.txt` file MUST be updated with your real AdMob Publisher ID.

4. **App Store URLs**: Currently use placeholder IDs. Update with actual App Store IDs when available.

## 📞 Support & Contact

**Developer**: Cong Le  
**Email**: anniversarytrackerteamcong@gmail.com  
**Portfolio**: https://teamcong.github.io  
**App Store**: [Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)

## 📄 License

This portfolio template and automation scripts are provided as-is. The legal documents should be reviewed by qualified legal counsel for your specific use case.

---

**⭐ Professional iOS Developer Portfolio - Showcasing Quality Mobile Applications**
