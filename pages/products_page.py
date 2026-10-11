from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


# ProductsPage: Page Object Model for the Products page
# Contains reusable product listing, sorting, and cart actions.
class ProductsPage(BasePage):

    # Locators: Product listing and sorting
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # Locators: Shopping cart
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Product-specific buttons
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE = (By.ID, "remove-sauce-labs-backpack")
    BIKE_LIGHT_ADD = (By.ID, "add-to-cart-sauce-labs-bike-light")

    # Get the Products page heading
    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        ).text

    # Get the number of products displayed
    def get_product_count(self):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_ITEMS
            )
        )
        return len(products)

    # Select a product sorting option
    def sort_products(self, option):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_visible_text(option)

    # Retrieve product prices as floating-point numbers
    def get_product_prices(self):
        price_elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_PRICES
            )
        )
        return [
            float(element.text.replace("$", ""))
            for element in price_elements
        ]

    # Add Sauce Labs Backpack to the cart
    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD)

    # Remove Sauce Labs Backpack from the Products page
    def remove_backpack_from_cart(self):
        self.click(self.BACKPACK_REMOVE)

    # Add Sauce Labs Bike Light to the cart
    def add_bike_light_to_cart(self):
        self.click(self.BIKE_LIGHT_ADD)

    # Get the shopping cart badge count with an optional explicit wait
    def get_cart_count(self, expected_count=None):
        def read_cart_count(driver):
            badges = driver.find_elements(*self.CART_BADGE)

            if not badges:
                return 0

            badge_text = badges[0].text.strip()
            return int(badge_text) if badge_text.isdigit() else 0

        if expected_count is not None:
            self.wait.until(
                lambda driver: read_cart_count(driver) == expected_count
            )

        return read_cart_count(self.driver)

    # Open the Shopping Cart page and wait until it is loaded.
    def open_cart(self):
        # Click the shopping cart icon.
        self.click(self.CART_LINK)

        # Wait until the Shopping Cart heading is displayed.
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.PAGE_TITLE, "Your Cart"
            )
        )
