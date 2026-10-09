import pytest
from pages.login_page import LoginPage


# Positive Testing: Verify login with valid credentials
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    # Enter valid credentials and click Login
    login_page.login("standard_user", "secret_sauce")

    # Verify successful login redirects to Products page
    assert "/inventory.html" in login_page.get_current_url()


# Negative Testing: Verify login with invalid or missing credentials
# Parameterization runs the same test with multiple sets of data
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        # Scenario 1: Invalid username and password
        (
            "invalid_user",
            "invalid_password",
            "Username and password do not match"
        ),

        # Scenario 2: Empty username
        (
            "",
            "secret_sauce",
            "Username is required"
        ),

        # Scenario 3: Empty password
        (
            "standard_user",
            "",
            "Password is required"
        ),
    ]
)
def test_invalid_login(driver, username, password, expected_error):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    # Attempt login with invalid or missing credentials
    login_page.login(username, password)

    # Retrieve the error message displayed by the application
    actual_error = login_page.get_error_message()

    # Verify the expected error message is displayed
    assert expected_error in actual_error

    # Verify invalid login does not redirect to Products page
    assert "/inventory.html" not in login_page.get_current_url()
