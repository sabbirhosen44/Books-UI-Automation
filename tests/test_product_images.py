import allure
from urllib.parse import urljoin

from config.settings import (
    BASE_URL,
    MAX_IMAGE_PAGES
)


@allure.feature("Images")
@allure.story("Product Image Validation")
@allure.title("Verify all product images load correctly")
def test_product_images(page):

    page.goto(BASE_URL)

    current_page = 1

    while current_page <= MAX_IMAGE_PAGES:

        images = page.locator(
            "article.product_pod img"
        )

        assert images.count() > 0, (
            f"No images found on page {current_page}"
        )

        for i in range(images.count()):

            image = images.nth(i)

            assert image.is_visible(), (
                f"Image {i+1} not visible "
                f"on page {current_page}"
            )

            src = image.get_attribute("src")

            assert src, (
                f"Missing src attribute "
                f"on page {current_page}"
            )

            image_url = urljoin(
                page.url,
                src
            )

            response = page.request.get(
                image_url
            )

            assert response.status == 200, (
                f"Broken image: {image_url}"
            )

        if current_page < MAX_IMAGE_PAGES:

            page.locator(
                "li.next a"
            ).click()

            page.wait_for_load_state(
                "networkidle"
            )

        current_page += 1