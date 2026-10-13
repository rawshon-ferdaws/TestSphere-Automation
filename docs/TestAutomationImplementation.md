# Selenium UI Automation Testing with PyTest

## Test Case 1: Valid Login

**Test Case ID:** TC_LOGIN_001

**What We Tested:** Verify that a user can successfully log in with valid credentials and navigate to the Products page.

**Which Files:**

- `tests/ui/test_login.py` — Test logic and assertions.
- `pages/login_page.py` — Login locators and actions.
- `pages/base_page.py` — Reusable Selenium methods inherited by LoginPage.

**Which Code (illustrative):**

```python
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url
```

**Explanation:** Selenium enters valid credentials, clicks the Login button, and PyTest verifies that the browser navigates to the Products page.

**Expected Result:** The user successfully logs in, and the current URL contains `/inventory.html`.

**Result:** Passed.

## Test Case 2: Invalid Username and Password

**Test Case ID:** TC_LOGIN_002

**What We Tested:** Verify that the application rejects invalid login credentials and displays the appropriate error message.

**Which Files:**

- `tests/ui/test_login.py` — Test logic, parameterization, and assertions.
- `pages/login_page.py` — Login locators, actions, and error message retrieval.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "invalid_user",
            "invalid_password",
            "Username and password do not match"
        )
    ]
)
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
```

**Explanation:** Selenium enters invalid credentials and clicks Login. PyTest verifies that the displayed error message contains the expected text. This scenario is one of three parameterized negative login cases.

**Expected Result:** The application rejects the invalid credentials and displays an error message containing "Username and password do not match".

**Result:** Passed.

## Test Case 3: Empty Username

**Test Case ID:** TC_LOGIN_003

**What We Tested:** Verify that the application displays an appropriate error message when the username is empty.

**Which Files:**

- `tests/ui/test_login.py` — Test logic, parameterization, and assertions.
- `pages/login_page.py` — Login locators, actions, and error message retrieval.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "",
            "secret_sauce",
            "Username is required"
        )
    ]
)
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
```

**Explanation:** Selenium leaves the username field empty, enters a valid password, and clicks Login. PyTest verifies that the application displays the expected validation error.

**Expected Result:** The application rejects the login attempt and displays "Username is required".

**Result:** Passed.

## Test Case 4: Empty Password

**Test Case ID:** TC_LOGIN_004

**What We Tested:** Verify that the application displays an appropriate error message when the password is empty.

**Which Files:**

- `tests/ui/test_login.py` — Test logic, parameterization, and assertions.
- `pages/login_page.py` — Login locators, actions, and error message retrieval.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "standard_user",
            "",
            "Password is required"
        )
    ]
)
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
```

**Explanation:** Selenium enters a valid username, leaves the password field empty, and clicks Login. PyTest verifies that the application displays the expected validation error.

**Expected Result:** The application rejects the login attempt and displays "Password is required".

**Result:** Passed.

## Test Case 5: Products Page Validation

**Test Case ID:** TC_PRODUCTS_001

**What We Tested:** Verify that after successful login, the Products page loads correctly and displays the "Products" heading.

**Which Files:**

- `tests/ui/test_products.py` — Test logic and assertions.
- `pages/login_page.py` — Login actions.
- `pages/products_page.py` — Products page locators and validation.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
def test_products_page(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert products_page.get_page_title() == "Products"
```

**Explanation:** Selenium logs in with valid credentials and navigates to the Products page. PyTest verifies that the page heading displays "Products".

**Expected Result:** The Products page loads successfully and displays the "Products" heading.

**Result:** Passed.

## Test Case 6: Product Listing Validation

**Test Case ID:** TC_PRODUCTS_002

**What We Tested:** Verify that the Products page displays a list of available products after successful login.

**Which Files:**

- `tests/ui/test_products.py` — Test logic and assertions.
- `pages/login_page.py` — Login actions.
- `pages/products_page.py` — Product listing locators and validation.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
def test_product_listing(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert products_page.get_product_count() > 0
```

**Explanation:** Selenium logs in and retrieves the number of products displayed on the Products page. PyTest verifies that at least one product is available.

**Expected Result:** The Products page displays one or more products.

**Result:** Passed.

## Test Case 7: Price Sorting — Low to High

**Test Case ID:** TC_PRODUCTS_003

**What We Tested:** Verify that products are sorted by price in ascending order (lowest to highest).

**Which Files:**

- `tests/ui/test_products.py` — Test logic and assertions.
- `pages/login_page.py` — Login actions.
- `pages/products_page.py` — Product sorting and price retrieval.
- `pages/base_page.py` — Reusable Selenium methods and explicit waits.

**Which Code (illustrative):**

```python
def test_sort_products_low_to_high(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.login("standard_user", "secret_sauce")
    products_page.sort_by_price_low_to_high()
    prices = products_page.get_product_prices()
    assert prices == sorted(prices)
```

**Implementation Note:** The current framework uses `products_page.sort_products("Price (low to high)")` in the parameterized `test_product_price_sorting()` test. The illustrative `sort_by_price_low_to_high()` method is not defined in `ProductsPage`.

**Explanation:** Selenium logs in, selects the price sorting option (Low to High), and retrieves product prices. PyTest verifies that the prices are arranged in ascending order.

**Expected Result:** Products are displayed from the lowest price to the highest price.

**Result:** Passed.

# REST API Automation Testing with Python Requests and PyTest

## Test Case 1: GET All Posts

**Test Case ID:** TC_API_001

**What We Tested:** Verify that the GET API successfully retrieves all posts and returns a valid JSON response containing the required fields.

**Which Files:**

- `tests/api/test_get.py` — API test logic and assertions.

**Which Code:**

```python
import requests  # Import the library for sending HTTP requests

# Define the base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():

    # Send a GET request to retrieve all posts
    response = requests.get(
        f"{BASE_URL}/posts",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful HTTP response (200 OK)
    assert response.status_code == 200

    # Convert the JSON response into Python data
    posts = response.json()

    # Verify the response data type is a list
    assert isinstance(posts, list)

    # Verify that at least one post is returned
    assert len(posts) > 0

    # Verify each post contains all required fields
    for post in posts:
        assert "id" in post
        assert "userId" in post
        assert "title" in post
        assert "body" in post
```

**Explanation:** Python Requests sends a GET request to `/posts`. PyTest verifies that the API returns HTTP 200, the response is a non-empty JSON list, and every post contains the required fields (`id`, `userId`, `title`, `body`).

**Expected Result:** HTTP 200 OK, a non-empty JSON list, and all required fields present in every post.

**Result:** Passed.

## Test Case 2: GET Single Post

**Test Case ID:** TC_API_002

**What We Tested:** Verify that the GET API successfully retrieves a specific post using its ID and returns a valid JSON response containing the correct post details.

**Which Files:**

- `tests/api/test_get.py` — API test logic and assertions.

**Which Code:**

```python
# TC_API_002: Verify GET Single Post
def test_get_single_post():

    # Define the ID of the post to retrieve
    post_id = 1

    # Send a GET request to retrieve a specific post
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful HTTP response (200 OK)
    assert response.status_code == 200

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response data type is a dictionary
    assert isinstance(post, dict)

    # Verify the returned post ID matches the requested ID
    assert post["id"] == post_id

    # Verify the response contains all required fields
    assert "userId" in post
    assert "title" in post
    assert "body" in post

    # Verify the title and body are not empty
    assert len(post["title"]) > 0
    assert len(post["body"]) > 0
```

**Explanation:** Python Requests sends a GET request to `/posts/1`. PyTest verifies that the API returns HTTP 200, the response is a JSON object (Python dictionary), the returned post ID matches the requested ID, and the required fields are present with non-empty title and body.

**Expected Result:** HTTP 200 OK, a valid JSON object with post ID 1, all required fields present, and non-empty title and body.

**Result:** Passed.

## Test Case 3: GET Invalid Post

**Test Case ID:** TC_API_003

**What We Tested:** Verify that the GET API returns HTTP 404 (Not Found) when requesting a nonexistent post ID and provides an empty JSON response.

**Which Files:**

- `tests/api/test_get.py` — API test logic and assertions.

**Which Code:**

```python
# TC_API_003: Verify GET Invalid Post
def test_get_invalid_post():

    # Define a post ID that does not exist
    post_id = 999999

    # Send a GET request for the nonexistent post
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify HTTP 404 (Not Found) for an invalid post ID
    assert response.status_code == 404

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response data type is a dictionary
    assert isinstance(post, dict)

    # Verify the response contains an empty JSON object
    assert post == {}
```

**Explanation:** Python Requests sends a GET request to `/posts/999999`. PyTest verifies that the API returns HTTP 404 (Not Found), the response is a JSON object (Python dictionary), and the response body is empty (`{}`).

**Clarification:** The response body contains an empty JSON object (`{}`), rather than being zero-length. The object has no fields.

**Expected Result:** HTTP 404 Not Found, a valid JSON response containing an empty object (`{}`).

**Result:** Passed.

## Test Case 4: POST Valid Data

**Test Case ID:** TC_API_004

**What We Tested:** Verify that the POST API successfully accepts valid JSON data, returns HTTP 201 Created, and includes the correct resource details in the response.

**Which Files:**

- `tests/api/test_post.py` — API test logic and assertions.

**Which Code:**

```python
import requests  # Import the library for sending HTTP requests

# Define the base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


# TC_API_004: Verify POST Valid Data
def test_create_post():

    # Define valid JSON data for creating a new post
    payload = {
        "title": "TestSphere API Automation",
        "body": "Testing POST request using Python Requests",
        "userId": 1
    }

    # Send a POST request with JSON data to create a post
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,  # Automatically serialize data into JSON
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful resource creation response (201 Created)
    assert response.status_code == 201

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response data type is a dictionary
    assert isinstance(post, dict)

    # Verify the response contains a generated post ID
    assert "id" in post
    assert isinstance(post["id"], int)
```

**Implementation Note:** This excerpt ends after the generated ID checks. The full test in `tests/api/test_post.py` also verifies that the returned `title`, `body`, and `userId` match the submitted payload.

**Explanation:** Python Requests sends a POST request to `/posts` with valid JSON data. PyTest verifies that the API returns HTTP 201 Created, the response is a JSON object (Python dictionary), a generated post ID is present, and the returned title, body, and userId match the submitted data.

**Expected Result:** HTTP 201 Created, a valid JSON object containing a generated post ID and the correct title, body, and user ID. JSONPlaceholder simulates creation without permanently storing the post.

**Result:** Passed.
