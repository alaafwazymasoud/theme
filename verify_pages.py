import asyncio
import os
from playwright.async_api import async_playwright

async def verify_page(context, page_name, src_dir, output_dir):
    print(f"Verifying {page_name}...")
    page = await context.new_page()
    try:
        url = f'file://{os.path.join(src_dir, page_name)}'
        await page.goto(url)
        # Determine output path
        screenshot_name = page_name.replace('.html', '.png')
        output_path = os.path.join(output_dir, screenshot_name)
        await page.screenshot(path=output_path, full_page=True)
        print(f"Verified {page_name}")
    finally:
        await page.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()

        cwd = os.getcwd()
        src_dir = os.path.join(cwd, 'src')
        output_dir = os.path.join(cwd, 'verification')

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        pages_to_verify = [
            'index.html',
            'category.html',
            'destination.html',
            'post.html',
            'build-your-tour.html'
        ]

        tasks = [verify_page(context, page, src_dir, output_dir) for page in pages_to_verify]
        await asyncio.gather(*tasks)

        await browser.close()
        print("Verification complete. Screenshots saved to verification/ directory.")

if __name__ == "__main__":
    asyncio.run(main())
