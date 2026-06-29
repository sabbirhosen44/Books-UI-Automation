from pages.base_page import BasePage

class HomePage(BasePage):

    BOOKS = "article.product_pod"

    def get_headings(self):
        return self.page.locator(
            "h1,h2,h3,h4,h5,h6"
        )

    def get_books(self):
        return self.page.locator(
            self.BOOKS
        )

    def get_book_titles(self):

        books = self.get_books()

        titles = []

        for i in range(books.count()):

            title = (
                books.nth(i)
                .locator("h3 a")
                .get_attribute("title")
            )

            titles.append(title)

        return titles

    def click_book(self, title):

        self.page.locator(
            f'a[title="{title}"]'
        ).first.click()

    def get_book_price(self, title):

        books = self.get_books()

        for i in range(books.count()):

            book = books.nth(i)

            current_title = (
                book
                .locator("h3 a")
                .get_attribute("title")
            )

            if current_title == title:

                return (
                    book
                    .locator(".price_color")
                    .inner_text()
                )

        return None

    def click_next_page(self):

        self.page.locator(
            "li.next a"
        ).click()