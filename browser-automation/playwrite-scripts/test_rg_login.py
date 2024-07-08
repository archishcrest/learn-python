import re
from playwright.sync_api import Page, expect



def test_login(page: Page):
    page.goto("https://researchgiant.com/login")

    # Click the get started link.
    #page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    #expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    page.get_by_placeholder("Email Address").fill("jason@ilocal.net")
    page.get_by_placeholder("Password").fill("Plumbing++2024++")
    page.get_by_role("button", name=re.compile("login", re.IGNORECASE)).click()