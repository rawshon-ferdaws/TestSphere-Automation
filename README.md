# TestSphere-Automation — QA Automation Framework

## 1. Project Overview

**TestSphere-Automation** is a Python-based QA automation project designed to validate the functionality of the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

The framework uses **Selenium WebDriver, PyTest, and Page Object Model (POM)** to develop reusable, maintainable, and scalable automated tests.

The current implementation covers Login, Products, and Cart functionality, with **12 automated UI test cases successfully executed**.

The project is being extended to include REST API testing, integration testing, and CI/CD automation.

### Technologies and Tools

| Technology / Tool | Purpose | Status |
|---|---|---|
| Python | Automation programming language | Implemented |
| Selenium WebDriver | UI browser automation | Implemented |
| PyTest | Test execution, assertions, fixtures, parameterization | Implemented |
| Page Object Model (POM) | Reusable page objects | Implemented |
| Allure Report | Test execution reporting | Implemented |
| Jira | Defect tracking and management | Implemented |
| Python Requests / Postman | REST API testing | Planned |
| GitHub Actions | CI/CD automation | Planned |

## 2. Test Automation Coverage

| Module | Test Scenarios | Total Tests | Status |
|---|---|---:|---|
| Login | Valid login, invalid credentials, empty username, empty password | 4 | Passed |
| Products | Page validation, product listing, price sorting low-to-high and high-to-low | 4 | Passed |
| Cart | Add product, verify cart contents, remove product, add multiple products | 4 | Passed |
| **Total** | | **12** | **12 Passed** |

### Login Testing

**Positive Testing:** Verify successful login using valid credentials and navigation to the Products page (`/inventory.html`).

**Negative Testing:** Verify appropriate error messages for invalid credentials, an empty username, and an empty password.

**Data-Driven Testing:** Use `@pytest.mark.parametrize` to execute multiple negative login scenarios.

### Products Testing

Validate the Products page, product listing, and price sorting in ascending and descending order.

### Cart Testing

Validate adding products, verifying cart contents, removing products, and adding multiple products.

Explicit waits handle dynamic page updates and navigation synchronization.

## 3. Test Execution Summary

| Metric | Result |
|---|---:|
| Total UI Tests | 12 |
| Passed | 12 |
| Failed | 0 |
| Skipped | 0 |
| Pass Rate | 100% |

**Execution Status:** Completed

**Result:** All 12 UI tests passed in the latest recorded regression execution.

For detailed results, see [Test Execution Report](docs/TestExecutionReport.md).

## 4. Project Structure

```text
TestSphere-Automation/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   └── test_cart.py
│   ├── api/
│   └── integration/
├── docs/
│   ├── TestStrategy.md
│   ├── TestPlan.md
│   ├── TestCases.md
│   ├── TestExecutionReport.md
│   ├── DebuggingIssues.md
│   └── screenshots/
│       ├── allure-overview.png
│       └── allure-test-results.png
├── utils/
├── test_data/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

*Planned directories and screenshots should only be shown as existing files once they have been created.*

## 5. Types of Testing

| # | Testing Type | What We Are Testing | Status |
|---|---|---|---|
| 1 | Functional Testing | Login, product listing, sorting, cart | Implemented |
| 2 | Positive Testing | Valid login and successful product operations | Implemented |
| 3 | Negative Testing | Invalid login credentials and missing inputs | Implemented |
| 4 | UI Automation Testing | Browser interactions using Selenium WebDriver | Implemented |
| 5 | Data-Driven Testing | Multiple login inputs using PyTest parameterization | Implemented |
| 6 | Smoke Testing | Critical login and application functionality | Planned |
| 7 | Sanity Testing | Focused testing after specific bug fixes | Planned |
| 8 | Regression Testing | Re-execution of existing UI tests | Implemented |
| 9 | Integration Testing | UI and API interactions | Planned |
| 10 | REST API Testing | HTTP methods, status codes, JSON responses, CRUD operations | Planned |
| 11 | Database Testing | SQL validation and data integrity | Planned |
| 12 | Exploratory Testing | Manual investigation of application behavior | Planned |
| 13 | End-to-End (E2E) Testing | Login → Products → Cart → Checkout | Planned |
| 14 | Cross-Browser Testing | Chrome and Firefox execution | Planned |
| 15 | CI/CD Automated Testing | GitHub Actions automated execution | Planned |

## 6. Testing Techniques and Tools

| Technique / Tool | Purpose |
|---|---|
| Selenium WebDriver | Browser automation |
| PyTest | Fixtures, assertions, parameterization, and test execution |
| Page Object Model | Reusable and maintainable page objects |
| Explicit Waits | Synchronization with dynamic UI elements |
| Allure Report | Automated test reporting |
| Jira | Defect tracking and debugging issue management |
| Python Requests / Postman | Planned REST API testing |
| GitHub Actions | Planned CI/CD integration |

## 7. Installation and Test Execution

### Prerequisites

- Python 3.13 or compatible version
- Google Chrome
- Git
- Allure CLI (optional for viewing reports)

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TestSphere-Automation.git
cd TestSphere-Automation
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run All UI Tests

```bash
python -m pytest tests/ui/ -v
```

### Run Tests with Allure Reporting

```bash
python -m pytest tests/ui/ -v --alluredir=allure-results --clean-alluredir
```

### View Allure Report

```bash
allure serve allure-results
```

## 8. Allure Test Reporting

Allure reporting is integrated with PyTest to provide test execution summaries, individual test results, and detailed reporting.

### Allure Overview

![Allure Overview](docs/screenshots/allure-overview.png)

### Allure Test Results

![Allure Test Results](docs/screenshots/allure-test-results.png)

*Add the actual screenshots to `docs/screenshots/` before publishing. Generated Allure result and report folders are excluded from Git.*

## 9. Defect Tracking and Debugging

**Defect Management Tool:** Jira

| Jira Issue | Description | Status |
|---|---|---|
| KAN-4 | Cart Navigation Synchronization Failure | Done |

**Issue:** Selenium read the Products page heading before Cart navigation completed.

**Resolution:** Implemented an explicit wait using Selenium Expected Conditions to verify the `"Your Cart"` heading.

Additional synchronization issues, flaky test investigations, and browser lifecycle debugging are documented in [Debugging Issues](docs/DebuggingIssues.md).

## 10. Project Documentation

| Document | Description |
|---|---|
| [Test Strategy](docs/TestStrategy.md) | Testing approach and automation strategy |
| [Test Plan](docs/TestPlan.md) | Objectives, scope, environment, risks, and planning |
| [Test Cases](docs/TestCases.md) | Test scenarios, steps, and expected results |
| [Test Execution Report](docs/TestExecutionReport.md) | Execution results, metrics, and screenshots |
| [Debugging Issues](docs/DebuggingIssues.md) | Selenium issues, debugging techniques, and resolutions |
| [Automation Concepts & Learning Notes](docs/TestSphere-Automation.md) | Explains POM, PyTest fixtures, parameterization, synchronization, and flaky test investigations |

## 11. Future Enhancements

- Implement REST API testing using Python Requests and PyTest.
- Add integration testing between UI and API.
- Configure GitHub Actions for CI/CD automation.
- Extend UI coverage to Checkout functionality.
- Add cross-browser testing.
- Enhance automated reporting and failure diagnostics.

## 12. Conclusion

**TestSphere-Automation** demonstrates hands-on experience in QA automation framework development, functional testing, regression testing, Selenium WebDriver, Python, PyTest, Page Object Model, Allure reporting, Jira defect tracking, and debugging.

The current framework includes **12 successfully executed UI test cases** covering Login, Products, and Cart functionality.

The project will continue expanding with API testing, integration testing, and CI/CD automation.
