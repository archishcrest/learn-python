import re
from playwright.sync_api import Page, expect



def test_login(page: Page):
    page.goto("https://hrms.crestinfosystems.net/signin")

    page.wait_for_timeout(2000)
    page.get_by_placeholder("Enter Email").fill("archish.p@crestinfosystems.com")
    page.get_by_placeholder("Enter Password").fill("Archish@9913")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name=re.compile("sign in", re.IGNORECASE)).click()

    page.locator('xpath=//*[@id="root"]/div[2]/header/div/div[2]/div/div').click()
    page.wait_for_timeout(1000)
    page.locator('xpath=//*[@id="account-menu"]/div[3]/ul/div[3]/li[1]/span[1]').click()

    page.wait_for_timeout(1000)
    page.locator('xpath=//*[@id="root"]/div[2]/main/div[1]/div/button').click()

    page.wait_for_timeout(5000)