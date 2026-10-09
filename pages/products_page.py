from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


# ProductsPage: Contains locators and actions for the Products page
# Inherits reusable Selenium methods from BasePage
class ProductsPage(BasePage):

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

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
