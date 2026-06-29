from pages.base_page import BasePage


class BookDetailsPage(BasePage):

    def get_book_title(self):

        return self.page.locator(
            ".product_main h1"
        ).inner_text()

    def get_book_price(self):

        return self.page.locator(
            ".product_main .price_color"
        ).inner_text()

    def is_book_information_visible(self):

        return self.page.locator(
            "table.table"
        ).is_visible()