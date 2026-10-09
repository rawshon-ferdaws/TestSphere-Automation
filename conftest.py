import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# PyTest Fixture: Browser Setup and Teardown
# Provides a fresh Chrome browser instance for each test.
@pytest.fixture
def driver():

    # Configure Chrome browser options
    options = Options()
    options.add_argument("--window-size=1440,900")

    # Setup: Launch Chrome using Selenium WebDriver
    browser = webdriver.Chrome(options=options)

    try:
        # Provide the browser instance to the test function
        yield browser

    finally:
        # Teardown: Close the browser even if the test fails
        browser.quit()
