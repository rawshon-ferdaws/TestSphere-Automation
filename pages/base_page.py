from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# BasePage: Contains reusable Selenium WebDriver methods
# Other page classes inherit from BasePage to avoid duplicate code.
class BasePage:

    # Initialize WebDriver and configure explicit wait
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Wait until an element is clickable, then click it
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Wait until an element is visible, then enter text
    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # Return the current browser URL for test validation
    def get_current_url(self):
        return self.driver.current_url
