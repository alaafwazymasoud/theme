from playwright.sync_api import sync_playwright
import os

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to src directory
        cwd = os.getcwd()
        src_dir = os.path.join(cwd, 'src')

        # List of pages to verify
        pages_to_verify = [
            "index.html",
            "category.html",
            "destination.html",
            "post.html",
            "build-your-tour.html"
        ]

        for filename in pages_to_verify:
            print(f"Verifying {filename}...")
            page.goto(f'file://{os.path.join(src_dir, filename)}')

            # Create screenshot filename
            screenshot_name = os.path.splitext(filename)[0] + '.png'
            page.screenshot(path=screenshot_name, full_page=True)

        browser.close()
        print("Verification complete. Screenshots saved.")

if __name__ == "__main__":
    verify_pages()
