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
@allure.story("Consistency")
@allure.title(
    "Verify homepage and details page data match"
)
def test_book_consistency(page):

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

        homepage_price = (
            home_page.get_book_price(book)
        )

        home_page.click_book(book)

        details_title = (
            details_page.get_book_title()
        )

        details_price = (
            details_page.get_book_price()
        )

        assert details_title == book

        assert details_price == homepage_price

        details_page.go_back()