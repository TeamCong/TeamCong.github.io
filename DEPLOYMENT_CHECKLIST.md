# TeamCong GitHub Pages Deployment Checklist

## ✅ Completed Tasks

- [x] Created `.cursorrules` for development guidelines
- [x] Created `app-ads.txt` template file
- [x] Created `privacy.md` with comprehensive privacy policy
- [x] Created `terms.md` with comprehensive terms and conditions
- [x] Created `index.md` with complete app portfolio
- [x] Created `_config.yml` for Jekyll configuration
- [x] Updated `README.md` with full documentation
- [x] All Markdown files include proper Jekyll front matter
- [x] All 23 TeamCong apps are listed in the portfolio

## 🔄 Next Steps (Before Going Live)

### 1. Repository Setup
- [ ] Create GitHub repository named `TeamCong.github.io` under TeamCong organization
- [ ] Set repository to **Public** visibility
- [ ] Push all files to the `main` branch

### 2. Critical Updates Required
- [ ] **UPDATE `app-ads.txt`**: Replace `pub-0000000000000000` with your actual Google AdMob Publisher ID
- [ ] **VERIFY email**: Ensure `support@teamcong.dev` is active and monitored
- [ ] **LEGAL REVIEW**: Have privacy policy and terms reviewed by legal counsel (recommended)

### 3. GitHub Pages Configuration
- [ ] Go to repository Settings → Pages
- [ ] Ensure source is set to "Deploy from a branch"
- [ ] Ensure branch is `main` and folder is `/ (root)`
- [ ] Wait for initial deployment (may take 5-10 minutes)

### 4. Verification Tests
- [ ] Visit `https://teamcong.github.io/` - should load main page
- [ ] Visit `https://teamcong.github.io/privacy` - should load privacy policy
- [ ] Visit `https://teamcong.github.io/terms` - should load terms and conditions
- [ ] Visit `https://teamcong.github.io/app-ads.txt` - should load ads file
- [ ] Test all internal links work correctly
- [ ] Test responsive design on mobile and desktop

### 5. AdMob Integration
- [ ] Log into Google AdMob/Ad Manager
- [ ] Verify `app-ads.txt` is correctly crawled (may take up to 24 hours)
- [ ] Confirm no `app-ads.txt` errors in AdMob dashboard

## 📱 App Updates (Per App)

For each of the 23 TeamCong apps, update the following:

### In App Store Connect/Google Play Console:
- [ ] Update Privacy Policy URL to: `https://teamcong.github.io/privacy`
- [ ] Update Terms & Conditions URL to: `https://teamcong.github.io/terms`

### In App Code (if applicable):
- [ ] Update hardcoded privacy policy links in app settings/about screens
- [ ] Update hardcoded terms links in app settings/about screens
- [ ] Test links open correctly in development builds
- [ ] Submit app updates where necessary

### App List for Updates:
- [ ] Fish Scanner AI Identifier
- [ ] Anniversary Tracker
- [ ] Card Value Tracker for Pokemon
- [ ] Pomodoro timer: Focus
- [ ] Baby Kicks: Track Movements
- [ ] Link Saver - fast and easy
- [ ] Couple days counter
- [ ] Mortgage Calculator - Learn
- [ ] Simplest Stopwatch and Timer
- [ ] to do リスト - やること管理アプリ
- [ ] Birthday Tracker and Reminders
- [ ] Learn Japanese
- [ ] Othello boardgame
- [ ] Sunrise & Sunset tracker
- [ ] Photo Image Compression
- [ ] VidCompression
- [ ] Lullaby Pal - White Noise
- [ ] Countdown Tracker Reminders
- [ ] Driving Theory Test UK 2025
- [ ] Solitaire - TEAMCONG
- [ ] Fish Run - Collect stars
- [ ] Run Run Run
- [ ] Water them plants

## 🔄 Ongoing Maintenance Schedule

### Monthly
- [ ] Check all links work correctly
- [ ] Monitor AdMob for `app-ads.txt` status

### Quarterly  
- [ ] Review app list and descriptions
- [ ] Update app portfolio on main page

### Annually
- [ ] Review and update privacy policy
- [ ] Review and update terms and conditions
- [ ] Update "Last Updated" dates

### As Needed
- [ ] Update `app-ads.txt` when changing ad networks
- [ ] Add new apps to portfolio
- [ ] Update contact information

## 🚨 Important Notes

1. **Legal Compliance**: The privacy policy and terms are templates. Consider legal review for compliance with GDPR, CCPA, and app store policies.

2. **Contact Email**: Ensure `anniversarytrackerteamcong@gmail.com` is active before going live.

3. **Publisher ID**: The `app-ads.txt` file MUST be updated with your real AdMob Publisher ID before deployment.

4. **Testing**: Always test changes in a development environment when possible.

## 📞 Support

If you encounter issues:
- Check GitHub Pages documentation: https://docs.github.com/en/pages
- Review Jekyll documentation: https://jekyllrb.com/docs/
- Test locally with `bundle exec jekyll serve` if needed 