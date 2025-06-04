# Cong Le - Principal iOS Developer Portfolio

**Professional iOS developer portfolio for Principal iOS Developer at Capital One**

🌐 **Live Site**: [https://teamcong.github.io](https://teamcong.github.io)  
🍎 **App Store**: [Cong Le Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)  
👨‍💻 **Personal Site**: [https://congl3.github.io](https://congl3.github.io)  
🏦 **Current Role**: Principal iOS Developer at Capital One

## 🎯 Purpose

This repository serves dual purposes with a smart page structure:

### 🏢 Company Landing Page (`index.md`)
- **TeamCong App Showcase**: Perfect Support URL for App Store apps
- **Customer Support**: Help and contact information for app users
- **App Discovery**: All 12+ apps organized by category
- **Legal Compliance**: Links to privacy policy and terms

### 💼 Professional Portfolio (`portfolio.md`)  
- **Career Showcase**: Highlighting 9+ years of iOS development experience
- **Technical Leadership**: Demonstrating architecture skills and enterprise-scale development
- **Professional Contact**: Targeted at employers and career opportunities
- **Achievement Focus**: Principal-level role, team leadership, 150k+ downloads

**Additional Pages:**
- **📄 Professional CV** (`cv.md`): Complete resume for job applications
- **📋 Legal Documents**: Privacy Policy and Terms & Conditions
- **📺 Ad Network**: `app-ads.txt` file for AdMob integration

## 📁 Repository Structure

```
├── index.md                   # TeamCong company landing page (App Support URL)
├── portfolio.md               # Professional developer portfolio (Career focus)
├── cv.md                      # Comprehensive professional CV/Resume  
├── privacy.md                 # Privacy policy for personal apps
├── terms.md                   # Terms and conditions for personal apps
├── app-ads.txt                # Ad network authorization file
├── _config.yml                # Jekyll configuration
├── .cursorrules              # Development guidelines
├── scrape_appstore.py        # App Store data scraper
├── update_portfolio.py       # Portfolio update automation
├── update_app_ids.py         # App Store ID updater
├── requirements.txt          # Python dependencies
├── Makefile                  # Automation commands
├── DEPLOYMENT_CHECKLIST.md   # Deployment guide
├── FINAL_DEPLOYMENT_GUIDE.md # Complete deployment instructions
└── README.md                 # This file
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

## 💼 Professional Profile

### Current Role: Principal iOS Developer at Capital One
**Dec 2021 - Present (3 yrs 7 mos)**

- 🏆 **Highest contributor** to the iOS repository across the entire team
- 🏗️ **Architecture leadership** - tackling challenges with legacy codebases and modernization
- 🤝 **Cross-functional collaboration** - working with designers, product owners, QA, and services teams
- 📈 **Continuous improvement** - driving codebase health and development practices

### Professional Experience Timeline
- **2021-Present**: Principal iOS Developer at Capital One (Nottingham)
- **2020-2021**: English Second Language Teacher (Career transition)
- **2015-2018**: Senior iOS Developer at Capital One (London)
- **2013-2014**: iOS Developer at Wonder PL (London)

**Total Professional Experience**: 9+ years of iOS development

## 🌟 Portfolio Highlights

### 🏆 Featured Personal Project: Anniversary Tracker
- **150k+ Downloads** | **5k Ratings at 4.7⭐**
- Demonstrates end-to-end product development skills alongside professional work
- Technologies: SwiftUI, Core Data, MVVM, Swift

### 📱 Personal App Collection (12+ Apps)

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

#### 🎮 Entertainment
- **Card Value Tracker for Pokemon** - Trading card management

#### 💕 Lifestyle
- **Couple days counter** - Relationship milestones

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

Your personal apps currently use placeholder IDs. To update with real App Store IDs:

### Method 1: Using the ID Updater (Recommended)
```bash
# 1. Edit update_app_ids.py and replace XXXXXXXXX with real IDs
# 2. Run the updater
make update-ids
```

## 🔗 Key URLs

When deployed, the following URLs are available:

- **Company Landing**: `https://teamcong.github.io/` (Perfect for App Store Support URL)
- **Professional Portfolio**: `https://teamcong.github.io/portfolio` (Career opportunities)
- **CV/Resume**: `https://teamcong.github.io/cv`
- **Privacy Policy**: `https://teamcong.github.io/privacy`
- **Terms & Conditions**: `https://teamcong.github.io/terms`
- **App-Ads.txt**: `https://teamcong.github.io/app-ads.txt`

## 💡 Perfect Structure Benefits

### For App Store Apps
- **Support URL**: Use `https://teamcong.github.io` - looks professional and company-focused
- **Customer Experience**: Users see a clean company page with all apps and support info
- **Legal Compliance**: Direct links to privacy/terms for App Store requirements

### For Career Opportunities  
- **Professional Portfolio**: `https://teamcong.github.io/portfolio` - targeted for employers
- **Principal Developer Focus**: Highlights leadership role and technical expertise
- **Complete Profile**: Links to CV, company work, and personal projects

## 👨‍💻 Professional Features

### Enterprise Experience Showcase
- **Capital One Leadership**: Highlighting current Principal iOS Developer role
- **9+ Years Experience**: Comprehensive professional timeline and achievements
- **Technical Leadership**: Architecture decisions, team mentoring, and process improvements
- **Large-scale Applications**: Experience with consumer banking apps serving millions

### Personal Project Portfolio
- **150k+ Downloads**: Demonstrating product development and user acquisition skills
- **12+ Published Apps**: Showcasing diverse technical skills and App Store success
- **Real Statistics**: Highlighting measurable success metrics
- **End-to-end Development**: From concept to App Store success

### CV/Resume Features
- **Technical Leadership**: Principal-level experience and responsibilities
- **Enterprise Technologies**: SwiftUI, UIKit, CI/CD, TDD, architecture patterns
- **Team Collaboration**: Cross-functional team experience and mentoring
- **Measurable Achievements**: Specific accomplishments and recognition

## ⚙️ Configuration

### Before Deployment

1. **Update `app-ads.txt`** with your real AdMob Publisher ID:
   ```
   google.com, pub-YOUR_ACTUAL_PUBLISHER_ID, DIRECT, f08c47fec0942fa0
   ```

2. **Update App Store IDs** using the ID updater script

3. **Verify Contact Email**: Ensure `anniversarytrackerteamcong@gmail.com` is active

4. **Customize CV**: Edit `cv.md` with any specific experience details

### GitHub Pages Setup

1. Create repository named `TeamCong.github.io` under your organization
2. Set repository to **Public** visibility
3. Go to Settings → Pages → Deploy from main branch
4. Push all files and wait 5-10 minutes for deployment

## 📊 Portfolio Statistics

- **Professional Experience**: 9+ years iOS development
- **Current Role**: Principal iOS Developer at Capital One
- **Personal Apps**: 12+ iOS applications
- **Personal Project Downloads**: 150k+ (Anniversary Tracker)
- **Average Rating**: 4.7+ stars
- **Technologies**: Swift, SwiftUI, UIKit, Objective-C, MVVM, TDD, CI/CD
- **Leadership**: Team mentoring, architecture decisions, process improvements

## 🎯 Professional Target Audience

This portfolio is designed for:
- **Senior/Principal iOS Developer roles** - showcasing technical leadership
- **iOS Architect positions** - demonstrating architecture and technical decision-making
- **Team Lead opportunities** - highlighting mentoring and collaboration skills
- **Enterprise companies** - showing large-scale application experience
- **Financial services** - demonstrating fintech and banking app experience

## 📋 Technical Skills Highlighted

### Enterprise iOS Development
- **Large-scale Applications** - Capital One consumer banking apps
- **Legacy Codebase Management** - Modernization and architectural improvements
- **CI/CD Implementation** - Jenkins, Fastlane, automated deployment
- **Cross-functional Collaboration** - Working with design, product, QA, backend teams

### iOS Technologies (Expert Level)
- **Swift** (9+ years) - Expert-level professional experience
- **SwiftUI** - Modern declarative UI development
- **UIKit** - Extensive traditional iOS UI experience
- **Objective-C** - Legacy codebase maintenance
- **MVVM/Clean Architecture** - Scalable application design
- **XCTest/TDD** - Comprehensive testing strategies

### Leadership & Process
- **Technical Leadership** - Architecture decisions and team guidance
- **Code Quality** - Review processes and development standards
- **Team Mentoring** - Supporting junior developers
- **Process Improvement** - Development workflow optimization

## 🚨 Important Notes

1. **Professional Positioning**: Portfolio emphasizes current Principal iOS Developer role at Capital One
2. **Technical Leadership**: Highlights architecture, mentoring, and enterprise experience
3. **Personal Projects**: Showcases entrepreneurial skills alongside professional work
4. **Contact Information**: Ensure `anniversarytrackerteamcong@gmail.com` is monitored
5. **App Store IDs**: Currently use placeholders - update with real IDs using the updater script

## 📞 Support & Contact

**Principal iOS Developer**: Cong Le (@CongLe)  
**Current Role**: Principal iOS Developer at Capital One  
**Email**: anniversarytrackerteamcong@gmail.com  
**Portfolio**: https://teamcong.github.io  
**Personal Site**: https://congl3.github.io  
**App Store**: [Developer Profile](https://apps.apple.com/gb/developer/cong-le/id954373766)

## 📄 License

This portfolio template and automation scripts are provided as-is. The legal documents should be reviewed by qualified legal counsel for your specific use case.

---

**⭐ Principal iOS Developer Portfolio - 9+ Years Experience | Capital One | 150k+ App Downloads**
