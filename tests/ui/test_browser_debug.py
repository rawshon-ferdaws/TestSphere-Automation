from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Diagnostic: Verify the complete Add and Remove Cart workflow
def test_browser_stability(driver):
    wait = WebDriverWait(driver, 10)

    # Step 1: Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Step 2: Log in
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    wait.until(EC.url_contains("/inventory.html"))
    print("Login successful:", driver.current_url)

    # Step 3: Add Sauce Labs Backpack
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # Wait for the cart badge without using Selenium's
    # text_to_be_present_in_element expected condition.
    def cart_badge_is_one(browser):
        badges = browser.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        if not badges:
            return False

        return badges[0].text.strip() == "1"


    wait.until(cart_badge_is_one)

    print("Product added successfully")
    print("Cart badge:", driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    ).text)

    # Step 4: Open Shopping Cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(EC.url_contains("/cart.html"))
    print("Shopping Cart opened:", driver.current_url)

    # Step 5: Verify product exists
    product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert product.text == "Sauce Labs Backpack"
    print("Product verified:", product.text)

    # Step 6: Remove the product
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "remove-sauce-labs-backpack")
        )
    ).click()

    # Step 7: Wait until cart becomes empty
    wait.until(
        lambda browser: len(
            browser.find_elements(
                By.CLASS_NAME, "cart_item"
            )
        ) == 0
    )

    # Step 8: Verify cart badge disappears
    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    print("Product removed successfully")
    print("Remaining cart items:", len(
        driver.find_elements(By.CLASS_NAME, "cart_item")
    ))
    print("Browser window handles:", driver.window_handles)
