import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


# PyTest Fixture: Login before each Products page test
@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    return driver


# Positive Testing: Verify Products page is displayed
def test_products_page_displayed(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    # Verify the page heading
    assert products_page.get_page_title() == "Products"


# Positive Testing: Verify products are listed
def test_product_listing(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    # Verify at least one product is displayed
    assert products_page.get_product_count() > 0


# Functional Testing: Verify product sorting by price
# Parameterization tests both ascending and descending order
@pytest.mark.parametrize(
    "sort_option,reverse",
    [
        ("Price (low to high)", False),
        ("Price (high to low)", True),
    ]
)
def test_product_price_sorting(
    logged_in_driver, sort_option, reverse
):
    products_page = ProductsPage(logged_in_driver)

    # Select the sorting option
    products_page.sort_products(sort_option)

    # Retrieve the displayed product prices
    actual_prices = products_page.get_product_prices()

    # Compare actual prices against expected sorted prices
    expected_prices = sorted(actual_prices, reverse=reverse)

    assert actual_prices == expected_prices
