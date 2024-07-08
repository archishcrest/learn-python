import re
from playwright.sync_api import Page, expect



def test_login(page: Page):
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



# https://stackoverflow.com/questions/71937343/playwright-how-to-wait-until-there-is-no-animation-on-the-page
# https://www.lambdatest.com/automation-testing-advisor/python/playwright-python-expect_file_chooser
# https://playwright.dev/python/docs/api/class-elementhandle#element-handle-wait-for-selector






    