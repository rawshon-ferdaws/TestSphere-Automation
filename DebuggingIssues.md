| Q  | Page / File             | Issue We Faced                                | Debugging Category                   | How We Addressed It                                                    |
| --- | ----------------------- | --------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------- |
| Q1 | `products_page.py`      | `TimeoutException`                            | Synchronization / Explicit Waits     | Investigated cart count timeout using explicit waits and debug logging |
| Q2 | `products_page.py`      | Cart badge count mismatch                     | Synchronization / Element State      | Implemented `get_cart_count(expected_count)`                           |
| Q3 | `cart_page.py`          | Cart navigation verification failure          | Navigation / Synchronization         | Added URL and page-heading text waits                                  |
| Q4 | `cart_page.py`          | Product removal verification failure          | Synchronization / Dynamic UI         | Added `wait_for_cart_item_count(0)`                                    |
| Q5 | `cart_page.py`          | Cart badge disappearance verification failure | Element Visibility / Synchronization | Used `EC.invisibility_of_element_located()`; subsequent tests passed   |
| Q6 | `test_cart.py`          | Flaky cart tests                              | Test Reliability / Test Isolation    | Isolated tests, investigated failures, and repeated executions         |
| Q7 | `conftest.py` / Browser | `NoSuchWindowException`                       | Browser Lifecycle / Selenium         | Checked window handles and investigated browser closure                |
| Q8 | Chrome / ChromeDriver   | Suspected version mismatch                    | Browser Compatibility Investigation  | Verified both used major version 154; no major-version mismatch found  |
| Q9 | `test_browser_debug.py` | `AttributeError` involving `NoneType`         | Python / Diagnostic Debugging        | Changed the diagnostic wait condition                                  |

## Q1. How did we investigate the TimeoutException during cart badge verification?

**Issue:** `TimeoutException`

**Page:** `pages/products_page.py`

**Debugging Category:** Synchronization / Explicit Waits

**What happened:**

After clicking Add to Cart, Selenium sometimes failed to verify that the cart badge displayed 1 within 10 seconds.

The test failed at this assertion:

```python
assert products_page.get_cart_count(expected_count=1) == 1
```

**How we addressed it:**

We added temporary debugging statements to inspect the cart badge text and used an explicit wait to check the expected count.

**Relevant code:**

```python
if expected_count is not None:
    self.wait.until(
        lambda driver: read_cart_count(driver) == expected_count
    )
```

**Key code line:**

`self.wait.until(...)` repeatedly checks whether the actual cart count matches the expected count.

**Result:** Later runs successfully verified the badge count.

## Q2. How did we handle the cart badge count mismatch?

**Issue:** Cart badge count mismatch (0 instead of 1 or 2)

**Page:** `pages/products_page.py`

**Debugging Category:** Synchronization / Element State

**What happened:**

After adding one or two products, Selenium sometimes returned 0 or failed to observe the expected badge count.

**How we addressed it:**

We implemented a reusable `get_cart_count()` method that handles a missing badge and waits for the expected value.

**Relevant code:**

```python
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
```

**Key code lines:**

- `driver.find_elements(*self.CART_BADGE)` finds the badge if present.
- `if not badges: return 0` handles an absent badge.
- `badge_text.isdigit()` validates the text before converting it to an integer.
- `self.wait.until(...)` waits for the expected count.

**Result:** The tests subsequently verified cart counts of 1 and 2.

## Q3. How did we handle cart navigation verification failures?

**Issue:** Cart navigation verification failure

**Page:** `pages/cart_page.py`

**Debugging Category:** Navigation / Synchronization

**What happened:**

After clicking the cart icon, Selenium sometimes still observed the Products page title instead of Your Cart.

In another execution, `driver.current_url` unexpectedly returned `None`, causing the URL wait to fail.

**How we addressed it:**

We added explicit waits to verify the cart URL and expected page title before continuing.

**Relevant code:**

```python
def get_page_title(self):
    self.wait.until(EC.url_contains("/cart.html"))
    return self.wait.until(
        EC.text_to_be_present_in_element(
            self.PAGE_TITLE, "Your Cart"
        )
    ) and self.driver.find_element(*self.PAGE_TITLE).text
```

**Key code lines:**

- `EC.url_contains("/cart.html")` waits for the expected URL.
- `EC.text_to_be_present_in_element(...)` waits for the title Your Cart.

**Result:** Cart navigation verification passed in later regression runs.

## Q4. How did we resolve product removal verification failures?

**Issue:** Product removal verification failure

**Page:** `pages/cart_page.py`

**Debugging Category:** Synchronization / Dynamic UI

**What happened:**

After clicking Remove, Selenium sometimes still detected one cart item when checking whether the cart was empty.

**How we addressed it:**

We implemented an explicit wait that checks whether the number of cart items becomes zero.

**Relevant code:**

```python
def wait_for_cart_item_count(self, expected_count):
    self.wait.until(
        lambda driver: len(
            driver.find_elements(*self.CART_ITEMS)
        ) == expected_count
    )
    return expected_count
```

**Test assertion:**

```python
cart_page.remove_backpack()
assert cart_page.wait_for_cart_item_count(0) == 0
```

**Key code line:**

`len(driver.find_elements(*self.CART_ITEMS)) == expected_count` checks whether the cart contains the expected number of items.

**Result:** The test successfully verified an empty cart.

## Q5. How did we verify cart badge disappearance after product removal?

**Issue:** Cart badge disappearance verification failure

**Page:** `pages/cart_page.py`

**Debugging Category:** Element Visibility / Synchronization

**What happened:**

After removing the final product, Selenium sometimes failed while verifying that the cart badge disappeared.

One observed failure was caused by losing access to the browser window during verification; it did not prove the badge remained visible.

**How we addressed it:**

We used Selenium's explicit invisibility wait to verify that the badge was hidden or absent.

**Relevant code:**

```python
def is_cart_badge_absent(self):
    return self.wait.until(
        EC.invisibility_of_element_located(self.CART_BADGE)
    )
```

**Test assertion:**

```python
assert cart_page.is_cart_badge_absent()
```

**Key code line:**

`EC.invisibility_of_element_located(self.CART_BADGE)` waits until the badge is invisible or no longer exists.

**Result:** The badge disappearance assertion passed in subsequent executions.

## Q6. How did we investigate flaky cart automation tests?

**Issue:** Flaky cart tests

**Page:** `tests/ui/test_cart.py`

**Debugging Category:** Test Reliability / Test Isolation

**What happened:**

Some cart tests passed during one execution but failed during another.

We encountered different errors, including `TimeoutException`, `NoSuchWindowException`, and cart state verification failures.

**How we addressed it:**

We ran failing tests individually, inspected browser state, added temporary debugging logs, and repeated regression runs.

**Relevant debugging code:**

```python
print("Before adding product")
print("Windows:", logged_in_driver.window_handles)
products_page.add_backpack_to_cart()
print("After adding product")
print("Windows:", logged_in_driver.window_handles)
print("Current URL:", logged_in_driver.current_url)
```

**Commands used:**

Run one failing test:

```bash
python -m pytest tests/ui/test_cart.py::test_remove_product_from_cart -v -s
```

Run all four cart tests:

```bash
python -m pytest tests/ui/test_cart.py -v -s
```

**Key code lines:**

- `window_handles` identifies currently available browser windows.
- `current_url` checks the browser's current location.
- `-s` allows debugging prints to appear in the terminal.

**Result:** All four cart tests passed together after debugging.

## Q7. How did we investigate NoSuchWindowException?

**Issue:** `NoSuchWindowException`

**Page:** `conftest.py` / Chrome browser

**Debugging Category:** Browser Lifecycle / Selenium

**What happened:**

During cart testing, Selenium sometimes lost access to the Chrome window.

The error was:

```text
NoSuchWindowException:
no such window: target window already closed
```

We also established that manually closing Chrome during test execution can cause this exception, although the exact cause of every earlier occurrence was not confirmed.

**How we addressed it:**

We checked browser window handles, investigated browser closure, and retained a function-scoped PyTest fixture for automatic browser management.

**Relevant code:**

```python
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1440,900")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
```

**Key code lines:**

- `scope="function"` creates a separate fixture instance for each test.
- `webdriver.Chrome(options=options)` starts Chrome.
- `yield browser` provides the driver to the test.
- `browser.quit()` closes Chrome during fixture cleanup.

**Result:** Later regression runs passed without encountering the exception.

## Q8. How did we investigate a suspected ChromeDriver version mismatch?

**Issue:** Suspected ChromeDriver version mismatch

**Component:** Chrome / ChromeDriver

**Debugging Category:** Browser Compatibility Investigation

**What happened:**

While investigating Selenium browser failures, we considered whether Chrome and ChromeDriver versions were incompatible.

**How we addressed it:**

We checked both versions using Selenium capabilities.

**Relevant code:**

```python
from selenium import webdriver

driver = webdriver.Chrome()
print(
    "Chrome:",
    driver.capabilities.get("browserVersion")
)
print(
    "ChromeDriver:",
    driver.capabilities.get("chrome", {}).get("chromedriverVersion")
)
driver.quit()
```

**Observed versions:**

| Component | Version |
| --- | --- |
| Chrome | 154.0.8037.98 |
| ChromeDriver | 154.0.8037.92 |

**Key code lines:**

- `driver.capabilities.get("browserVersion")` retrieves the Chrome version.
- `driver.capabilities.get("chrome", {}).get("chromedriverVersion")` retrieves the ChromeDriver version.

**Result:** Both used major version 154. We ruled out a major version mismatch; this was an investigation, not a confirmed compatibility defect.

## Q9. How did we investigate an AttributeError in the browser diagnostic test?

**Issue:** `AttributeError: 'NoneType' object has no attribute 'text'`

**Page:** `tests/ui/test_browser_debug.py` (temporary diagnostic file)

**Debugging Category:** Selenium / Diagnostic Debugging

**What happened:**

During cart navigation debugging, a diagnostic test encountered an unexpected `AttributeError` while checking the page title.

**How we addressed it:**

We changed the diagnostic wait condition to check matching title elements directly.

**Relevant code (representative diagnostic approach):**

```python
WebDriverWait(driver, 10).until(
    lambda d: any(
        element.text == "Your Cart"
        for element in d.find_elements(
            By.CLASS_NAME, "title"
        )
    )
)
```

**Key code lines:**

- `find_elements(By.CLASS_NAME, "title")` finds matching title elements.
- `element.text == "Your Cart"` checks the expected title.
- `any(...)` succeeds when at least one matching element has the expected text.

**Result:** The temporary diagnostic test passed in a later execution. The file was no longer needed for the final test suite.
