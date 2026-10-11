from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# CartPage: Page Object Model for the Shopping Cart page
class CartPage(BasePage):

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    BACKPACK_REMOVE = (By.ID, "remove-sauce-labs-backpack")

    # Wait for the Shopping Cart page and return its heading.
    def get_page_title(self):
        # Wait until navigation to the Cart page is complete.
        self.wait.until(
            EC.url_contains("cart.html")
        )

        # Wait until the Cart page heading is visible.
        title = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return title.text

    # Get all product names displayed in the cart
    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    # Get the number of cart items
    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    # Remove Sauce Labs Backpack from the cart
    def remove_backpack(self):
        self.click(self.BACKPACK_REMOVE)

    # Wait until the cart badge disappears
    def is_cart_badge_absent(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                self.CART_BADGE
            )
        )

    # Wait until the Shopping Cart contains the expected number of items
    def wait_for_cart_item_count(self, expected_count):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.CART_ITEMS)
            ) == expected_count
        )

        return expected_count
