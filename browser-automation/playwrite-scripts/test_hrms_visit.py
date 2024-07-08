import re
from playwright.sync_api import Page, expect



def test_login(page: Page):
    page.goto("https://hrms.crestinfosystems.net/signin")

    # Click the get started link.
    #page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    #expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    page.get_by_placeholder("Enter Email").fill("archish.p@crestinfosystems.com")
    page.get_by_placeholder("Enter Password").fill("Archish@9913")
    page.get_by_role("button", name=re.compile("sign in", re.IGNORECASE)).click()

    page.locator('xpath=//*[@id="root"]/div[2]/header/div/div[2]/div/div').click()
    #page.get_by_test_id("PersonIcon").click()
    #page.locator("css=button").click()

    page.locator('xpath=//*[@id="account-menu"]/div[3]/ul/div[3]/li[1]/span[1]').click()


    page.locator('xpath=//*[@id="root"]/div[2]/main/div[1]/div/button').click()




    