import allure
from urllib.parse import urljoin

from config.settings import BASE_URL


@allure.feature("Links")
@allure.story("Broken Link Validation")
@allure.title("Verify all hyperlinks return successful responses")
def test_broken_links(page):

    page.goto(BASE_URL)

    anchors = page.locator("a")

    urls = set()

    for i in range(anchors.count()):

        href = anchors.nth(i).get_attribute("href")

        if not href:
            continue

        if href.startswith("#"):
            continue

        if href.startswith("javascript:"):
            continue

        urls.add(
            urljoin(BASE_URL, href)
        )

    assert urls, "No URLs found"

    broken_links = []

    for url in sorted(urls):

        try:

            response = page.request.get(url)

            if response.status != 200:

                broken_links.append(
                    f"{url} -> {response.status}"
                )

        except Exception as e:

            broken_links.append(
                f"{url} -> {str(e)}"
            )

    assert not broken_links, (
        "Broken links found:\n"
        + "\n".join(broken_links)
    )