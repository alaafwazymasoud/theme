from playwright.sync_api import sync_playwright
import os

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to src directory
        cwd = os.getcwd()
        src_dir = os.path.join(cwd, 'src')

        # Verify index.html
        print("Verifying index.html...")
        page.goto(f'file://{os.path.join(src_dir, "index.html")}')
        page.screenshot(path='index.png', full_page=True)

        # Verify category.html
        print("Verifying category.html...")
        page.goto(f'file://{os.path.join(src_dir, "category.html")}')
        page.screenshot(path='category.png', full_page=True)

        # Verify destination.html
        print("Verifying destination.html...")
        page.goto(f'file://{os.path.join(src_dir, "destination.html")}')
        page.screenshot(path='destination.png', full_page=True)

        browser.close()
        print("Verification complete. Screenshots saved.")

if __name__ == "__main__":
    verify_pages()
