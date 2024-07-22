from playwright.sync_api import sync_playwright, Playwright

def run_test(url):

    try:
        with sync_playwright() as playwright:

            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context(record_video_dir="videos/")
            page = context.new_page()


            page.goto(url)

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
            
        print("Test run completed successfully.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# if __name__ == "__main__":
#     run_test()