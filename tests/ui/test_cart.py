import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


# Fixture: Log in before each Shopping Cart test
@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Verify login succeeded before testing cart operations
    assert "/inventory.html" in driver.current_url

    return driver


# TC_CART_01: Verify adding one product updates the cart badge
def test_add_one_product_to_cart(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    # Add Sauce Labs Backpack
    products_page.add_backpack_to_cart()

    # Verify cart badge displays 1
    assert products_page.get_cart_count(expected_count=1) == 1


# TC_CART_02: Verify the correct product appears in the cart
def test_product_displayed_in_cart(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    # Add product and navigate to Shopping Cart
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(logged_in_driver)

    # Verify Shopping Cart page is displayed
    assert cart_page.get_page_title() == "Your Cart"

    # Verify the correct product appears in the cart
    assert "Sauce Labs Backpack" in cart_page.get_product_names()


# TC_CART_03: Verify removing a product empties the cart
def test_remove_product_from_cart(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    products_page.add_backpack_to_cart()
    assert products_page.get_cart_count(expected_count=1) == 1

    products_page.open_cart()
    cart_page = CartPage(logged_in_driver)

    assert cart_page.get_page_title() == "Your Cart"
    assert "Sauce Labs Backpack" in cart_page.get_product_names()

    cart_page.remove_backpack()

    assert cart_page.wait_for_cart_item_count(0) == 0
    assert cart_page.is_cart_badge_absent()


# TC_CART_04: Verify adding multiple products updates the badge
def test_add_multiple_products(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)

    # Add two different products
    products_page.add_backpack_to_cart()
    products_page.add_bike_light_to_cart()

    # Verify cart badge displays 2
    assert products_page.get_cart_count(expected_count=2) == 2
