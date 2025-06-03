# TeamCong Portfolio Makefile
# Provides easy commands for portfolio management

.PHONY: help install update-portfolio scrape validate deploy clean update-ids

# Default target
help:
	@echo "TeamCong Portfolio Management"
	@echo "============================"
	@echo ""
	@echo "Available commands:"
	@echo "  make install          - Install Python dependencies"
	@echo "  make update-portfolio - Update portfolio with current app data"
	@echo "  make update-ids       - Update App Store IDs (after configuring real IDs)"
	@echo "  make scrape          - Scrape App Store data (if available)"
	@echo "  make validate        - Validate markdown files"
	@echo "  make deploy          - Deploy to GitHub Pages (git push)"
	@echo "  make clean           - Clean generated files"
	@echo ""
	@echo "Quick start:"
	@echo "  make install && make update-portfolio"
	@echo ""
	@echo "To update App Store IDs:"
	@echo "  1. Edit update_app_ids.py with real App Store IDs"
	@echo "  2. Run: make update-ids"

# Install Python dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed"

# Update portfolio with current data
update-portfolio:
	@echo "🚀 Updating portfolio..."
	python3 update_portfolio.py
	@echo "✅ Portfolio updated"

# Try to scrape live App Store data
scrape:
	@echo "🔍 Scraping App Store data..."
	python3 scrape_appstore.py --details --update-md --output apps_data.json
	@echo "✅ Scraping complete"

# Validate markdown files
validate:
	@echo "🔍 Validating markdown files..."
	@if command -v markdownlint >/dev/null 2>&1; then \
		markdownlint *.md; \
	else \
		echo "⚠️  markdownlint not installed, skipping validation"; \
		echo "   Install with: npm install -g markdownlint-cli"; \
	fi
	@echo "🔗 Checking internal links..."
	@grep -n "](\./" *.md || echo "No internal links found"
	@echo "✅ Validation complete"

# Deploy to GitHub Pages
deploy:
	@echo "🚀 Deploying to GitHub Pages..."
	@if git diff --quiet && git diff --cached --quiet; then \
		echo "⚠️  No changes to commit"; \
	else \
		git add .; \
		git commit -m "feat: Update portfolio and documentation"; \
		git push origin main; \
		echo "✅ Deployed to GitHub Pages"; \
		echo "🌐 Site will be available at: https://teamcong.github.io"; \
	fi

# Deploy with custom message
deploy-msg:
	@read -p "Enter commit message: " msg; \
	git add .; \
	git commit -m "$$msg"; \
	git push origin main; \
	echo "✅ Deployed to GitHub Pages"

# Clean generated files
clean:
	@echo "🧹 Cleaning generated files..."
	rm -f apps_data.json
	rm -f *.pyc
	rm -rf __pycache__
	@echo "✅ Cleanup complete"

# Quick setup for new environment
setup: install update-portfolio
	@echo "🎉 Setup complete!"
	@echo "📝 Next steps:"
	@echo "  1. Update app-ads.txt with your AdMob Publisher ID"
	@echo "  2. Verify contact email is active"
	@echo "  3. Run 'make deploy' to publish"

# Development server (if Jekyll is installed)
serve:
	@echo "🌐 Starting local development server..."
	@if command -v bundle >/dev/null 2>&1; then \
		bundle exec jekyll serve --livereload; \
	elif command -v jekyll >/dev/null 2>&1; then \
		jekyll serve --livereload; \
	else \
		echo "❌ Jekyll not installed"; \
		echo "   Install with: gem install bundler jekyll"; \
		echo "   Or use GitHub Pages directly"; \
	fi

# Show current status
status:
	@echo "📊 Portfolio Status"
	@echo "=================="
	@echo "📁 Files:"
	@ls -la *.md *.txt *.yml *.py 2>/dev/null | wc -l | sed 's/^/  Total files: /'
	@if [ -f apps_data.json ]; then \
		echo "  Apps data: ✅ Available"; \
		cat apps_data.json | jq length 2>/dev/null | sed 's/^/  Apps count: /' || echo "  Apps count: Available"; \
	else \
		echo "  Apps data: ❌ Missing"; \
	fi
	@echo ""
	@echo "🔗 URLs when deployed:"
	@echo "  Main site: https://teamcong.github.io/"
	@echo "  Privacy:   https://teamcong.github.io/privacy"
	@echo "  Terms:     https://teamcong.github.io/terms"
	@echo "  app-ads:   https://teamcong.github.io/app-ads.txt"

# Update App Store IDs with real ones
update-ids:
	@echo "🔄 Updating App Store IDs..."
	python3 update_app_ids.py
	@echo "✅ App ID update complete" 