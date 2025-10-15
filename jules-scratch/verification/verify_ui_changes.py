from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Verify landing page
    page.goto("http://127.0.0.1:4000")
    page.screenshot(path="jules-scratch/verification/landing_page.png")

    # Verify portfolio page
    page.goto("http://127.0.0.1:4000/portfolio")
    page.screenshot(path="jules-scratch/verification/portfolio_page.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
