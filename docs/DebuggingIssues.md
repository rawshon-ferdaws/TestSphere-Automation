# TestSphere-Automation — Debugging Issues

## Debugging Issues Summary

| Q | Page / File | Issue We Faced | Debugging Category | How We Addressed It |
|---|---|---|---|---|
| Q1 | `products_page.py` | `TimeoutException` | Synchronization / Explicit Waits | Investigated cart badge timeout using explicit waits and debug logging |
| Q2 | `products_page.py` | Cart badge count mismatch | Synchronization / Element State | Implemented `get_cart_count(expected_count)` |
| Q3 | `products_page.py` | Cart navigation verification failure | Navigation / Synchronization | Added explicit wait for the "Your Cart" heading in `open_cart()` |
| Q4 | `cart_page.py` | Product removal verification failure | Synchronization / Dynamic UI | Added `wait_for_cart_item_count(0)` |
| Q5 | `cart_page.py` | Cart badge disappearance verification failure | Element Visibility / Synchronization | Used `EC.invisibility_of_element_located()` |
| Q6 | `test_cart.py` | Flaky cart tests | Test Reliability / Test Isolation | Investigated failures and repeated test executions |
| Q7 | `conftest.py` / ChromeDriver log | `NoSuchWindowException` | Browser Lifecycle / Selenium | Investigated browser closure, window handles, and driver lifecycle |
| Q8 | Chrome / ChromeDriver | Suspected version mismatch | Browser Compatibility Investigation | Verified matching major version 154 |
| Q9 | `test_browser_debug.py` (removed) | `AttributeError` involving `NoneType` | Python / Diagnostic Debugging | Updated temporary diagnostic wait condition |

---

## Q1. How did we investigate the TimeoutException during cart badge verification?

**Issue:** `TimeoutException`  
**Page:** `pages/products_page.py`  
**Debugging Category:** Synchronization / Explicit Waits

**What happened:**

After clicking Add to Cart, Selenium sometimes failed to verify that the cart badge displayed `1` within 10 seconds.

**Error location:**

```python
assert products_page.get_cart_count(expected_count=1) == 1
```

**How we addressed it:**

We added temporary debugging statements to inspect the cart badge and used an explicit wait to check the expected count.

**Relevant code:**

```python
if expected_count is not None:
    self.wait.until(
        lambda driver: read_cart_count(driver) == expected_count
    )
```

**Explanation:** Selenium waits until the actual cart count matches the expected count.

**Result:** Later executions successfully verified the badge count.

---

## Q2. How did we handle the cart badge count mismatch?

**Issue:** Cart badge count mismatch (`0` instead of `1` or `2`)  
**Page:** `pages/products_page.py`  
**Debugging Category:** Synchronization / Element State

**What happened:**

After adding products, Selenium sometimes returned `0` or failed to observe the expected badge count.

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

**Explanation:**

- `find_elements()` finds the badge without raising an error if it is absent.
- `return 0` handles a missing badge.
- `self.wait.until()` waits for the expected count.

**Result:** Subsequent tests successfully verified cart counts of `1` and `2`.

---

## Q3. How did we solve the cart navigation synchronization issue?

**Issue:** Cart navigation verification failure  
**Page:** `pages/products_page.py`  
**Debugging Category:** Navigation / Synchronization  
**Jira:** `KAN-4` — Done

**What happened:**

After clicking the cart icon, Selenium checked the heading before navigation completed.

**Expected:** `Your Cart`  
**Actual:** `Products`

**Error:**

```text
AssertionError: assert 'Products' == 'Your Cart'
```

**How we addressed it:**

We added an explicit wait using Selenium Expected Conditions.

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

**Explanation:** Selenium waits until the Cart page heading contains `"Your Cart"` before continuing.

**Result:** All 4 Cart tests and the complete 12-test UI suite passed.

**Status:** Resolved and Verified — Jira `KAN-4` Done.

---

## Q4. How did we resolve product removal verification failures?

**Issue:** Product removal verification failure  
**Page:** `pages/cart_page.py`  
**Debugging Category:** Synchronization / Dynamic UI

**What happened:**

After clicking Remove, Selenium sometimes detected one cart item before the Cart page finished updating.

**How we addressed it:**

We added an explicit wait for the expected number of cart items.

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

**Explanation:** Selenium waits until the number of cart items becomes zero.

**Result:** The test successfully verified an empty cart.

---

## Q5. How did we verify cart badge disappearance after product removal?

**Issue:** Cart badge disappearance verification failure  
**Page:** `pages/cart_page.py`  
**Debugging Category:** Element Visibility / Synchronization

**What happened:**

After removing the final product, Selenium sometimes failed during cart badge disappearance verification.

One observed failure involved losing access to the browser window, rather than confirming that the badge remained visible.

**How we addressed it:**

We used an explicit invisibility wait to check whether the badge was hidden or absent.

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

**Explanation:** Selenium waits until the cart badge is invisible or no longer exists.

**Result:** The badge disappearance test passed in subsequent executions. This wait does not itself resolve browser-window closure errors.

---

## Q6. How did we investigate flaky cart automation tests?

**Issue:** Flaky cart tests  
**Page:** `tests/ui/test_cart.py`  
**Debugging Category:** Test Reliability / Test Isolation

**What happened:**

Some Cart tests passed during one execution but failed during another.

**Errors observed:**

- `TimeoutException`
- `NoSuchWindowException`
- Cart state verification failures

**How we investigated it:**

We ran tests individually, inspected browser state, added temporary debugging statements, and repeated executions.

**Debugging code:**

```python
print("Before adding product")
print("Windows:", logged_in_driver.window_handles)

products_page.add_backpack_to_cart()

print("After adding product")
print("Windows:", logged_in_driver.window_handles)
print("Current URL:", logged_in_driver.current_url)
```

**Commands:**

Run one Cart test:

```bash
python -m pytest tests/ui/test_cart.py::test_remove_product_from_cart -v -s
```

Run all Cart tests:

```bash
python -m pytest tests/ui/test_cart.py -v -s
```

We also compared test execution with the Allure plugin enabled and disabled.

**Result:** All 4 Cart tests and the complete 12-test UI suite passed in subsequent executions.

**Status:** Monitoring. The exact cause of the intermittent failures remains unconfirmed.

---

## Q7. How did we investigate NoSuchWindowException?

**Issue:** `NoSuchWindowException`  
**File:** `conftest.py` / ChromeDriver log  
**Debugging Category:** Browser Lifecycle / Selenium

**What happened:**

During Cart automation, Selenium intermittently lost access to the Chrome browser window.

**Error:**

```text
NoSuchWindowException:
target window already closed
```

**How we investigated it:**

1. Examined ChromeDriver logs.
2. Checked browser window handles.
3. Reviewed browser lifecycle management in `conftest.py`.
4. Investigated whether Chrome closed unexpectedly.
5. Repeated UI regression executions.

**ChromeDriver logging example:**

```python
from selenium.webdriver.chrome.service import Service

service = Service(
    log_output="chromedriver.log",
    service_args=["--verbose"]
)

driver = webdriver.Chrome(
    service=service,
    options=options
)
```

**Browser fixture:**

```python
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1440,900")

    browser = webdriver.Chrome(options=options)

    try:
        yield browser
    finally:
        browser.quit()
```

The `try/finally` structure ensures cleanup is attempted after the test, including when the test raises an exception. It is not a confirmed fix for unexpected browser closure.

**Result:** All 12 UI tests passed in subsequent regression executions.

**Status:** Monitoring — exact root cause not confirmed.

---

## Q8. How did we investigate a suspected ChromeDriver version mismatch?

**Issue:** Suspected ChromeDriver version mismatch  
**Component:** Chrome / ChromeDriver  
**Debugging Category:** Browser Compatibility Investigation

**What happened:**

While investigating Selenium browser failures, we considered whether Chrome and ChromeDriver versions were incompatible.

**How we investigated it:**

We checked browser and driver versions using Selenium capabilities.

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

**Historical versions recorded during debugging:**

| Component | Version |
|---|---|
| Chrome | 154.0.8037.98 |
| ChromeDriver | 154.0.8037.92 |

**Explanation:** Both used major version `154`, so no major-version mismatch was identified.

**Result:** Major-version mismatch was ruled out as an explanation. This was an investigation, not a confirmed compatibility defect.

---

## Q9. How did we investigate an AttributeError in the browser diagnostic test?

**Issue:** `AttributeError: 'NoneType' object has no attribute 'text'`  
**File:** `tests/ui/test_browser_debug.py` (temporary file, removed)  
**Debugging Category:** Python / Diagnostic Debugging

**What happened:**

A temporary browser diagnostic test encountered an `AttributeError` while checking the page heading.

The error indicated that `.text` was accessed on `None`. The original source of the `None` value was not conclusively established.

**How we addressed it:**

We changed the diagnostic wait condition to check matching title elements directly.

**Representative diagnostic code:**

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

**Explanation:** The wait checks whether at least one matching heading element contains `"Your Cart"`.

**Result:** The diagnostic test passed in a later execution. The temporary file was removed from the final project.

---

## Final Debugging Summary

| Category | Outcome |
|---|---|
| Cart synchronization | Fixed and verified |
| Cart badge count verification | Improved with explicit waits |
| Product removal verification | Improved with explicit waits |
| Cart badge disappearance | Verified in subsequent executions |
| Flaky test investigation | Tests passing; monitoring |
| `NoSuchWindowException` | Investigated; root cause unconfirmed |
| ChromeDriver compatibility | No major-version mismatch identified |
| Temporary diagnostic `AttributeError` | Investigated; diagnostic file removed |
| Latest UI regression | 12 Passed, 0 Failed |
| Jira Issue | KAN-4 — Done |

**Conclusion:** The debugging work improved synchronization and test reliability in TestSphere-Automation. The latest UI regression execution passed all 12 tests. Intermittent browser failures remain documented as investigations because their exact root cause was not conclusively established.
