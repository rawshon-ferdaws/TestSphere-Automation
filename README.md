## TestSphere Automation — Selenium UI Testing

**Technologies:** Python, Selenium WebDriver, PyTest, and Page Object Model (POM).

**Application Under Test:** [SauceDemo](https://www.saucedemo.com/) — A demo e-commerce application designed for software testing.

### First Automation Test: Valid User Login

**Objective:** Verify that a user can successfully log in with valid credentials.

**Test Steps:**

1. Launch Google Chrome using Selenium WebDriver.
2. Navigate to the SauceDemo website.
3. Enter a valid username and password.
4. Click the Login button.
5. Verify that the user is redirected to the Products page.
6. Close the browser after test execution.

**Expected Result:** The user successfully logs in and is redirected to the Products page (`/inventory.html`).

**Tools and Framework:** Python, Selenium WebDriver, PyTest, Page Object Model (POM).

### Negative Login Testing

**Objective:** Verify that the application correctly handles invalid or missing login credentials by displaying appropriate error messages.

**Test Scenarios:**

1. Invalid username and password.
2. Empty username.
3. Empty password.

**Approach:** Use PyTest parameterization (`@pytest.mark.parametrize`) to execute multiple test scenarios with different input data using a single test function.

**Expected Result:** The application rejects each invalid login attempt, displays the appropriate error message, and prevents access to the Products page.

### Types of Testing

The following table summarizes the types of testing we have completed, are planning, and will implement in our QA Automation project.

| # | Testing Type | What We Are Testing | Status |
| --- | --- | --- | --- |
| 1 | Functional Testing | Login, product listing, product sorting, cart, checkout | In progress |
| 2 | Positive Testing | Valid login, successful product operations | Implemented |
| 3 | Negative Testing | Invalid credentials, empty username/password, invalid checkout data | In progress |
| 4 | UI Automation Testing | Browser interactions using Selenium WebDriver | In progress |
| 5 | Data-Driven Testing | Multiple test inputs using PyTest parameterization | Implemented |
| 6 | Smoke Testing | Critical functionality such as login and checkout | Planned |
| 7 | Sanity Testing | Focused testing after specific bug fixes | Planned |
| 8 | Regression Testing | Re-execute existing tests after application changes | Planned |
| 9 | Integration Testing | Validate interactions between UI, API, and database | Planned |
| 10 | REST API Testing | HTTP methods, status codes, JSON responses, CRUD operations | Planned |
| 11 | Database Testing | SQL validation, data integrity, transaction records | Planned |
| 12 | Exploratory Testing | Manually investigate application behavior and edge cases | Planned |
| 13 | End-to-End (E2E) Testing | Complete login → products → cart → checkout workflow | Planned |
| 14 | Cross-Browser Testing | Execute UI tests in Chrome and Firefox | Planned |
| 15 | CI/CD Automated Testing | Execute automated tests through GitHub Actions | Planned |

### Testing techniques and tools

These support our testing activities but are not separate testing types.

| Technique / Tool | Purpose |
| --- | --- |
| Selenium WebDriver | Automates browser interactions |
| PyTest | Test execution, fixtures, assertions, parameterization |
| Page Object Model (POM) | Organizes reusable page objects |
| Explicit Waits | Synchronizes interactions with dynamic elements |
| Python Requests / Postman | REST API testing |
| PostgreSQL / SQL | Database validation |
| GitHub Actions | CI/CD test execution |
| Allure / PyTest HTML | Test execution reporting |
| Jira | Defect tracking and management |
