import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1440,900")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
