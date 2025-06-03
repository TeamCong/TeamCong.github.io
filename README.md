# TeamCong GitHub Pages

This repository hosts the official GitHub Pages site for TeamCong at [https://teamcong.github.io](https://teamcong.github.io).

## Purpose

This site serves as the central hub for:

- **`app-ads.txt`** - Ad network authorization file for Google AdMob and other advertising partners
- **Privacy Policy** - Comprehensive privacy policy for all TeamCong mobile applications
- **Terms and Conditions** - Terms of service for all TeamCong mobile applications
- **App Portfolio** - Showcase of all TeamCong mobile applications

## Site Structure

```
├── app-ads.txt          # Ad network authorization
├── privacy.md           # Privacy policy page
├── terms.md             # Terms and conditions page
├── index.md             # Main landing page
├── _config.yml          # Jekyll configuration
├── .cursorrules         # Development guidelines
└── README.md            # This file
```

## Key URLs

- **Main Site**: https://teamcong.github.io/
- **Privacy Policy**: https://teamcong.github.io/privacy
- **Terms & Conditions**: https://teamcong.github.io/terms
- **App-Ads.txt**: https://teamcong.github.io/app-ads.txt

## Maintenance Tasks

### Before Publishing

1. **Update `app-ads.txt`**:
   - Replace `pub-0000000000000000` with your actual Google AdMob Publisher ID
   - Add any additional ad network entries as needed

2. **Verify Contact Information**:
   - Ensure `support@teamcong.dev` email is active and monitored
   - Update any other contact details as needed

3. **Review Legal Documents**:
   - Have privacy policy and terms reviewed by legal counsel if required
   - Ensure compliance with GDPR, CCPA, and app store policies

### Regular Maintenance

- **Monthly**: Check that all links work correctly
- **Quarterly**: Review app list and update descriptions
- **Annually**: Review and update privacy policy and terms as needed
- **As Needed**: Update `app-ads.txt` when changing ad networks

## Development

This site uses Jekyll and GitHub Pages. Changes pushed to the `main` branch are automatically deployed.

### Local Development (Optional)

```bash
# Install Jekyll and dependencies
gem install bundler jekyll

# Serve locally (if you want to preview changes)
bundle exec jekyll serve
```

### Making Changes

1. Edit the relevant Markdown files
2. Commit and push to the `main` branch
3. Changes will be live within a few minutes at https://teamcong.github.io

## App Integration

When integrating these URLs into your mobile applications:

### Privacy Policy Links
Update your apps to use: `https://teamcong.github.io/privacy`

### Terms and Conditions Links  
Update your apps to use: `https://teamcong.github.io/terms`

## Apps Covered by These Policies

This site provides policies for all TeamCong applications:

- Fish Scanner AI Identifier
- Anniversary Tracker
- Card Value Tracker for Pokemon
- Pomodoro timer: Focus
- Baby Kicks: Track Movements
- Link Saver - fast and easy
- Couple days counter
- Mortgage Calculator - Learn
- Simplest Stopwatch and Timer
- to do リスト - やること管理アプリ
- Birthday Tracker and Reminders
- Learn Japanese
- Othello boardgame
- Sunrise & Sunset tracker
- Photo Image Compression
- VidCompression
- Lullaby Pal - White Noise
- Countdown Tracker Reminders
- Driving Theory Test UK 2025
- Solitaire - TEAMCONG
- Fish Run - Collect stars
- Run Run Run
- Water them plants

## Legal Disclaimer

The legal documents in this repository are templates and starting points. They should be reviewed by qualified legal counsel to ensure compliance with all applicable laws and regulations in your jurisdiction.

## Support

For questions about this site or TeamCong applications:
- **Email**: support@teamcong.dev
- **Website**: https://teamcong.github.io
