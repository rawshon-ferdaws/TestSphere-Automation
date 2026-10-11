import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    """
    Initialize a fresh Chrome WebDriver for each test.

    Ensures test isolation and closes the browser
    after test execution, even if the test fails.
    """

    # Configure Chrome browser options.
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1440,900")

    # Launch a new Chrome browser session.
    browser = webdriver.Chrome(options=chrome_options)

    # Set the maximum page loading time.
    browser.set_page_load_timeout(30)

    try:
        # Provide the WebDriver instance to the test.
        yield browser

    finally:
        # Close the browser and release WebDriver resources.
        browser.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Provide an authenticated WebDriver session.

    Logs in with valid SauceDemo credentials and
    waits for the Products page before returning control.
    """

    # Navigate to the SauceDemo login page.
    driver.get("https://www.saucedemo.com/")

    # Initialize the Login Page Object.
    login_page = LoginPage(driver)

    # Log in using valid test credentials.
    login_page.login("standard_user", "secret_sauce")

    # Wait until the Products page is loaded.
    WebDriverWait(driver, 15).until(
        lambda browser: "inventory.html" in browser.current_url
    )

    # Return the authenticated browser to the test.
    return driver
