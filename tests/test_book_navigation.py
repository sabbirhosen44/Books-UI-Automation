import allure

from config.settings import (
    BASE_URL,
    RANDOM_BOOK_COUNT
)

from pages.home_page import HomePage
from pages.book_details_page import (
    BookDetailsPage
)

from utils.random_helper import (
    get_random_books
)


@allure.feature("Books")
@allure.story("Navigation")
@allure.title(
    "Verify random books open correctly"
)
def test_book_navigation(page):

    home_page = HomePage(page)

    details_page = BookDetailsPage(page)

    home_page.navigate(BASE_URL)

    all_books = (
        home_page.get_book_titles()
    )

    selected_books = (
        get_random_books(
            all_books,
            RANDOM_BOOK_COUNT
        )
    )

    for book in selected_books:

        home_page.click_book(book)

        assert (
            details_page.get_book_title()
            == book
        )

        assert (
            details_page
            .is_book_information_visible()
        )

        details_page.go_back()