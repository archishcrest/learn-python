from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    page.goto("https://www.reduceimages.com/")

    with page.expect_file_chooser() as fc_info:
        page.locator('xpath=//*[@id="dropzone-container-offline"]/div[2]/button').click()

    file_chooser = fc_info.value
    file_chooser.set_files('test-img.png')

    #page.waitForSelector('xpath=//*[@id="width_field"]')

    page.locator('xpath=//*[@id="width_field"]').fill("500")
    page.locator('xpath=//*[@id="height_field"]').fill("500")

    page.locator('xpath=//*[@id="offline-submit-button"]').click()

    page.locator('xpath=//*[@id="download-button-container-cta"]').click()

    page.wait_for_timeout(10000)

with sync_playwright() as playwright:
    run(playwright)