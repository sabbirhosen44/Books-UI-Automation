import allure

from config.settings import BASE_URL
from pages.home_page import HomePage


@allure.feature("Homepage")
@allure.story("Homepage Validation")
@allure.title("Verify homepage loads successfully")
def test_homepage_validation(page):

    home_page = HomePage(page)

    home_page.navigate(BASE_URL)

    assert home_page.get_current_url() == BASE_URL

    assert "Books to Scrape" in home_page.get_page_title()

    headings = home_page.get_headings()

    assert headings.count() > 0

    for i in range(headings.count()):

        heading_text = (
            headings.nth(i)
            .inner_text()
            .strip()
        )

        assert heading_text != ""

    books = home_page.get_books()

    assert books.count() > 0