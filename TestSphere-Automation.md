## 1. Why do we need BasePage?

**Answer:**

BasePage contains common, reusable Selenium methods such as click(), enter_text(), and explicit waits. Instead of repeating these operations in every page class, we define them once in BasePage and reuse them through inheritance.

**Benefits:**

- Code Reusability: Avoids duplicate Selenium code.
- Maintainability: Common methods can be updated in one place.
- Readability: Keeps page classes clean and organized.
- Reliability: Centralizes explicit waits to handle dynamic elements.

## 2. Why do we need LoginPage?

**Answer:**

LoginPage is a class that follows the Page Object Model (POM) design pattern.
It separates page-specific elements (locators) and actions (methods) from test logic and assertions.
If a login element's locator changes, we update it in LoginPage instead of modifying multiple test cases.

**Benefits:**

- Maintainability: Update locators in one place.
- Reusability: Reuse login methods across multiple tests.
- Readability: Keeps test cases clean and easy to understand.
- Separation of Concerns: Separates page interactions from test assertions.

## 3. PyTest Fixture (conftest.py)

- @pytest.fixture: Defines a reusable fixture for browser setup and teardown.
- webdriver.Chrome(): Launches Chrome using Selenium WebDriver. Selenium Manager automatically manages the ChromeDriver when needed.
- yield browser: Provides the browser instance to the test and allows teardown code to execute after the test finishes.
- browser.quit(): Closes the browser session after test execution, even if the test fails, because it is inside a finally block.

**Why do we need it?**

To centralize browser setup and teardown, avoid duplicate code, improve test isolation, and maintain a clean automation framework.

## 4. What are we validating?

**Answer:**

We are verifying that a user can successfully log in to the application using valid credentials and is redirected to the Products (Inventory) page. This assertion checks whether the current URL contains `/inventory.html` after login, indicating successful navigation to the Products page.

**Expected Result:** The user successfully logs in and is redirected to the Products page.

## 5. Why use EC.visibility_of_element_located()?

**Answer:**

When used with `WebDriverWait.until()`, it explicitly waits until the error message is present and visible before retrieving its text. This helps prevent timing-related test failures.

## 6. Why do we need conftest.py?

**Answer:**

conftest.py is a PyTest configuration file used to define shared fixtures and hooks. Tests in the same directory and its subdirectories can use these fixtures without importing them directly, and PyTest calls the hooks automatically.

**Benefits:**

- Reusability: Browser setup and teardown are shared across multiple test files.
- Maintainability: Browser configuration is managed in one place.
- Test Isolation: Each test using our default function-scoped `driver` fixture receives a fresh browser instance.
- Reliability: Ensures proper browser cleanup after test execution.
