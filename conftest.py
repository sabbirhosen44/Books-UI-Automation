import pytest
import allure

from playwright.sync_api import (
    sync_playwright
)


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        context = browser.new_context(
            record_video_dir="videos"
        )

        page = context.new_page()

        yield page

        context.close()

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get(
            "page"
        )

        if page:

            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )