import re
from playwright.sync_api import Page, expect



def test_login(page: Page):
    page.goto("https://imageresizer.com/")

    # Click the get started link.
    #page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    #expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # page.get_by_placeholder("Enter Email").fill("archish.p@crestinfosystems.com")
    # page.get_by_placeholder("Enter Password").fill("Archish@9913")
    # page.get_by_role("button", name=re.compile("sign in", re.IGNORECASE)).click()

    #page.locator('xpath=//*[@id="root"]/div[2]/header/div/div[2]/div/div').click()
    #page.locator("css=button").click()
    # page.locator('xpath=//*[@id="account-menu"]/div[3]/ul/div[3]/li[1]/span[1]').click()
    # page.locator('xpath=//*[@id="root"]/div[2]/main/div[1]/div/button').click()

    with page.expect_file_chooser() as fc_info:
        page.get_by_test_id("device-upload-direct").click()

    file_chooser = fc_info.value
    file_chooser.set_files('test-img.png')

    page.get_by_test_id("resize-settings-by-dimensions-width").fill("500")
    page.get_by_test_id("resize-settings-by-dimensions-height").fill("500")

    page.get_by_test_id("resize-image-button").click()

    page.wait_for_timeout(10000)



# https://stackoverflow.com/questions/71937343/playwright-how-to-wait-until-there-is-no-animation-on-the-page
# https://www.lambdatest.com/automation-testing-advisor/python/playwright-python-expect_file_chooser






    