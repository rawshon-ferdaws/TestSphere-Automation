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
- browser.quit(): Closes the browser during fixture teardown, including when the test fails after the fixture has yielded.

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

## 7. Why do we need PyTest Parameterization?

**Answer:**

PyTest parameterization (`@pytest.mark.parametrize`) allows us to execute the same test function multiple times with different sets of test data without duplicating test code.

**Benefits:**

- Code Reusability: Avoids writing separate test functions for similar scenarios.
- Maintainability: Test logic is managed in one place.
- Test Coverage: Makes it easier to validate multiple input combinations and edge cases.
- Readability: Separates test data from test logic.
- Reporting: Each parameterized scenario appears as a separate test result in PyTest.

## 8. How did we solve synchronization issue?

**Answer:**

### 1. What is a Synchronization Issue?

A synchronization issue occurs when Selenium tries to interact with or validate an element before the application is ready.

### 2. When Did It Happen?

In our TestSphere-Automation project, Selenium checked the Cart page title before navigation completed.

- Expected: Your Cart
- Actual: Products
- Error: `AssertionError: assert 'Products' == 'Your Cart'`

### 3. How Did We Solve It?

We added an explicit wait using WebDriverWait and Expected Conditions (EC).

**Before:**

```python
def open_cart(self):
    self.click(self.CART_LINK)
```

**After:**

```python
def open_cart(self):
    self.click(self.CART_LINK)
    self.wait.until(
        EC.text_to_be_present_in_element(
            self.PAGE_TITLE, "Your Cart"
        )
    )
```

**Explanation:** Selenium waits until the Cart page heading contains "Your Cart" before continuing.

`self.wait` is a `WebDriverWait` instance initialized in `BasePage` and inherited by `ProductsPage`. This lets page classes reuse the synchronization setup defined in `BasePage`.

**Result:** All 12 UI tests passed.

**Jira:** KAN-4 — Resolved (Done).

## 9. How did we investigate Flaky Test issues?

**Answer:**

### 1. What is a Flaky Test?

A flaky test is an automated test that sometimes passes and sometimes fails without changes to the application or test code.

### 2. When Did It Happen?

In our TestSphere-Automation project, we experienced intermittent Selenium failures during Cart testing.

- Error: `NoSuchWindowException: target window already closed`
- Behavior: Some test runs failed, while subsequent runs passed.
- Possible Causes: Browser lifecycle issues, timing problems, or WebDriver session instability.

The exact root cause was not confirmed.

### 3. How Did We Investigate It?

We reran the UI tests and compared execution results with the Allure plugin enabled and disabled.

**Without Allure plugin:**

```bash
python -m pytest tests/ui/ -v -p no:allure_pytest
```

**With Allure reporting:**

```bash
python -m pytest tests/ui/ -v --alluredir=allure-results --clean-alluredir
```

**Explanation:** Both configurations eventually passed, so we could not confirm that Allure caused the intermittent failures.

### 4. Verification

- Result: 12 Passed, 0 Failed in the latest execution.
- Status: Intermittent issue under monitoring; root cause not confirmed.
