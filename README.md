# TeamCong Portfolio & GitHub Pages

**Professional iOS developer portfolio hosted on GitHub Pages**

🌐 **Live Site**: [https://teamcong.github.io](https://teamcong.github.io)  
🍎 **App Store**: [Cong Le Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)  
👨‍💻 **Personal Site**: [https://congl3.github.io](https://congl3.github.io)

## 🎯 Purpose

This repository serves multiple purposes:

- **📱 Professional Portfolio**: Showcase of all TeamCong mobile applications with real statistics
- **🏆 Featured Apps**: Highlighting Anniversary Tracker (65k+ downloads) and other popular apps
- **📋 Legal Hub**: Privacy Policy and Terms & Conditions for all apps
- **📺 Ad Network**: `app-ads.txt` file for AdMob and other advertising partners
- **📄 Professional CV**: Complete resume with technical skills and achievements
- **🔗 Central Reference**: Canonical URLs for app submissions and legal compliance

## 📁 Repository Structure

```
├── index.md                    # Main portfolio page with featured apps
├── cv.md                       # Professional CV/Resume  
├── privacy.md                  # Privacy policy for all apps
├── terms.md                    # Terms and conditions for all apps
├── app-ads.txt                 # Ad network authorization file
├── _config.yml                 # Jekyll configuration
├── .cursorrules               # Development guidelines
├── scrape_appstore.py         # App Store data scraper
├── update_portfolio.py        # Portfolio update automation
├── update_app_ids.py          # App Store ID updater
├── requirements.txt           # Python dependencies
├── Makefile                   # Automation commands
├── DEPLOYMENT_CHECKLIST.md    # Deployment guide
├── FINAL_DEPLOYMENT_GUIDE.md  # Complete deployment instructions
└── README.md                  # This file
```

## 🚀 Quick Start

### Option 1: Using Make (Recommended)
```bash
# Install dependencies and update portfolio
make setup

# Update portfolio with latest app data
make update-portfolio

# Update App Store IDs (after configuring real IDs)
make update-ids

# Deploy to GitHub Pages
make deploy
```

### Option 2: Manual Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Update portfolio with current app data
python3 update_portfolio.py

# Update App Store IDs with real ones
python3 update_app_ids.py

# Deploy changes
git add .
git commit -m "feat: Update portfolio"
git push origin main
```

## 🌟 Portfolio Highlights

### 🏆 Featured Apps
The portfolio prominently features your most successful applications:

**🎯 Anniversary Tracker**
- **65k+ Downloads** | **800k Sessions** | **4.7⭐ Rating**
- Your flagship relationship tracking app
- Technologies: SwiftUI, Core Data, MVVM, Swift

**💕 Couple Days Counter**
- Popular relationship milestone tracking
- Technologies: Swift, Core Data, Local Notifications

### 📱 Complete App Collection (15+ Apps)

#### 📸 Photo & Video Apps
- **VidCompression** - Video compression tool
- **Photo Image Compression** - Image optimization

#### 🛠️ Utilities & Productivity  
- **Birthday Tracker and Reminders** - Birthday management
- **Lullaby Pal - White Noise** - Sleep sounds
- **Link Saver - fast and easy** - Bookmark management
- **To Do List - One focus** - Minimalist task management
- **Water them plants** (1k downloads) - Plant care reminders

#### ⏰ Productivity & Time Management
- **Pomodoro timer: Focus** - Time management

#### 💰 Finance & Calculations
- **Mortgage Calculator - Learn** - Financial calculations

#### 🎮 Entertainment & Games
- **Card Value Tracker for Pokemon** - Trading card management
- **Fish Run - Collect stars** - Unity infinity runner
- **Run Run Run** - Canabalt-style Unity game

#### 💕 Lifestyle
- **Couple days counter** - Relationship milestones (also featured)

#### 🌅 Weather & Information
- **Sunrise & Sunset tracker** - Solar tracking

#### 🚗 Education
- **Driving Theory Test UK 2025** - UK driving test prep

## 🔧 Automation Features

### Portfolio Management
- **`update_portfolio.py`**: Updates portfolio with current app information
- **`update_app_ids.py`**: **NEW!** Easily update App Store IDs with real ones
- **`scrape_appstore.py`**: Scrapes live App Store data
- **`Makefile`**: Provides easy command-line automation

### Available Commands
```bash
make help              # Show all available commands
make install           # Install dependencies
make update-portfolio  # Update with current app data
make update-ids        # Update App Store IDs with real ones
make scrape           # Scrape live App Store data
make validate         # Validate markdown files
make deploy           # Deploy to GitHub Pages
make status           # Show current portfolio status
make serve            # Start local development server
```

## 🆔 Updating App Store IDs

Your apps currently use placeholder IDs. To update with real App Store IDs:

### Method 1: Using the ID Updater (Recommended)
```bash
# 1. Edit update_app_ids.py and replace XXXXXXXXX with real IDs
# 2. Run the updater
make update-ids
```

### Method 2: Manual Update
1. Visit each app's App Store page
2. Copy the ID from the URL (e.g., `id6743774763`)
3. Update the `REAL_APP_IDS` dictionary in `update_app_ids.py`
4. Run `python3 update_app_ids.py`

**Example:**
```python
REAL_APP_IDS = {
    "Card Value Tracker for Pokemon": "6743774763",  # ✅ Already updated
    "Anniversary Tracker": "1234567890",  # Update with real ID
    # ... etc
}
```

## 🔗 Key URLs

When deployed, the following URLs are available:

- **Portfolio**: `https://teamcong.github.io/`
- **CV/Resume**: `https://teamcong.github.io/cv`
- **Privacy Policy**: `https://teamcong.github.io/privacy`
- **Terms & Conditions**: `https://teamcong.github.io/terms`
- **App-Ads.txt**: `https://teamcong.github.io/app-ads.txt`

## 👨‍💻 Professional Features

### Personal Bio Integration
- Integrated bio from your existing [congl3.github.io](https://congl3.github.io) portfolio
- Professional journey: iOS Engineer → Backpacker → English Teacher → Back to iOS
- Unique perspective combining technical skills with global experience

### CV/Resume Page
- Complete professional resume at `/cv`
- Technical skills breakdown
- Project highlights with statistics
- Professional experience and achievements
- Career objectives and contact information

### Portfolio Design
- **Mobile-responsive** design
- **Featured apps section** highlighting your biggest successes
- **Real statistics** (65k downloads, 4.7 stars, etc.)
- **Technology tags** for each project
- **Professional presentation** suitable for job applications

## ⚙️ Configuration

### Before Deployment

1. **Update `app-ads.txt`** with your real AdMob Publisher ID:
   ```
   google.com, pub-YOUR_ACTUAL_PUBLISHER_ID, DIRECT, f08c47fec0942fa0
   ```

2. **Update App Store IDs** using the ID updater script

3. **Verify Contact Email**: Ensure `anniversarytrackerteamcong@gmail.com` is active

4. **Customize CV**: Edit `cv.md` with your specific experience details

### GitHub Pages Setup

1. Create repository named `TeamCong.github.io` under your organization
2. Set repository to **Public** visibility
3. Go to Settings → Pages → Deploy from main branch
4. Push all files and wait 5-10 minutes for deployment

## 📊 Portfolio Statistics

- **Total Apps**: 15+ iOS applications
- **Featured App Downloads**: 65k+ (Anniversary Tracker)
- **Average Rating**: 4.7+ stars
- **Categories**: 8 categories across the App Store
- **Platforms**: iPhone and iPad
- **Developer**: Published under "Cong Le"
- **Technologies**: Swift, SwiftUI, Unity, Core Data, etc.

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
1. Update app data in `update_portfolio.py`
2. Add real App Store ID to `update_app_ids.py`
3. Run `make update-portfolio && make update-ids`
4. Deploy with `make deploy`

## 📋 Maintenance Schedule

### Monthly
- [ ] Check all links work correctly
- [ ] Monitor AdMob for `app-ads.txt` status
- [ ] Run `make status` to verify setup
- [ ] Update app statistics if significant changes

### Quarterly
- [ ] Review app list and descriptions
- [ ] Update portfolio with new apps
- [ ] Run `make scrape` to get latest data
- [ ] Update CV with new achievements

### Annually
- [ ] Review and update privacy policy
- [ ] Review and update terms and conditions  
- [ ] Update "Last Updated" dates
- [ ] Legal compliance review

## 🚨 Important Notes

1. **App Store IDs**: Currently use placeholders - update with real IDs using the updater script
2. **Legal Compliance**: The privacy policy and terms are templates - consider legal review
3. **Contact Email**: Ensure `anniversarytrackerteamcong@gmail.com` is monitored
4. **AdMob Publisher ID**: Must be updated in `app-ads.txt` before going live
5. **CV Customization**: Edit `cv.md` with your specific details and experience

## 🎯 Professional Use

This portfolio is designed for:
- **Job Applications** - Complete professional presence
- **App Store Submissions** - Legal compliance and contact information
- **Networking** - Professional developer portfolio
- **Business Development** - Showcase of successful apps with real metrics

## 📞 Support & Contact

**Developer**: Cong Le (@CongLe)  
**Email**: anniversarytrackerteamcong@gmail.com  
**Portfolio**: https://teamcong.github.io  
**Personal Site**: https://congl3.github.io  
**App Store**: [Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)

## 📄 License

This portfolio template and automation scripts are provided as-is. The legal documents should be reviewed by qualified legal counsel for your specific use case.

---

**⭐ Professional iOS Developer Portfolio - Showcasing 65k+ Downloads and 15+ Quality Apps**
