# TestSphere-Automation — Test Cases

## Project Information

| Field | Details |
|---|---|
| Project Name | TestSphere-Automation |
| Application Under Test (AUT) | SauceDemo |
| Application URL | https://www.saucedemo.com/ |
| Programming Language | Python |
| Automation Framework | Selenium WebDriver + PyTest |
| Design Pattern | Page Object Model (POM) |
| Test Environment | Chrome Browser |
| Test Type | Functional UI Automation |
| Test Execution Tool | PyTest |
| Reporting Tool | Allure Reports |
| Test Execution Date | October 2026 |
| Test Execution Command | `python -m pytest tests/ui/ -v` |
| Test Scope | Login, Products, Shopping Cart |
| Total Automated Tests | 12 |
| Detailed Test Cases Documented | 4 (Login); Products and Cart documentation pending |
| Execution Status | 12 Passed, 0 Failed |

The automated suite contains 4 Login, 4 Products, and 4 Cart cases. This document currently describes only Login. The three negative cases use different data sets in the same parameterized test function.

**Automation Implementation Note:**

TC_LOGIN_002, TC_LOGIN_003, and TC_LOGIN_004 are implemented using a single parameterized PyTest function, `test_invalid_login`, with three different test data sets. PyTest executes each data set as a separate test case.

---

## 1. Login Module — 4 Test Cases

### TC_LOGIN_001 — Verify Login with Valid Credentials

| Field | Details |
|---|---|
| Test Case ID | TC_LOGIN_001 |
| Test Scenario | Verify login with valid credentials |
| Preconditions | SauceDemo login page is accessible |
| Test Data | Username: `standard_user`; Password: `secret_sauce` |
| Test Steps | 1. Open SauceDemo login page. 2. Enter valid username. 3. Enter valid password. 4. Click Login. |
| Expected Result | User successfully navigates to the Products page; URL contains `/inventory.html` |
| Actual Result | Successful navigation verified through the `/inventory.html` URL assertion |
| Status | Pass |
| Automation Script | `tests/ui/test_login.py::test_valid_login` |

### TC_LOGIN_002 — Verify Login with Invalid Credentials

| Field | Details |
|---|---|
| Test Case ID | TC_LOGIN_002 |
| Test Scenario | Verify login with invalid username and password |
| Preconditions | SauceDemo login page is accessible |
| Test Data | Username: `invalid_user`; Password: `invalid_password` |
| Test Steps | 1. Open SauceDemo login page. 2. Enter invalid username. 3. Enter invalid password. 4. Click Login. |
| Expected Result | Error message contains `Username and password do not match`; user must not successfully log in |
| Actual Result | Expected login error message was displayed and validated |
| Status | Pass |
| Automation Script | `tests/ui/test_login.py::test_invalid_login` — invalid credentials data set |

### TC_LOGIN_003 — Verify Login with Empty Username

| Field | Details |
|---|---|
| Test Case ID | TC_LOGIN_003 |
| Test Scenario | Verify login validation when username is empty |
| Preconditions | SauceDemo login page is accessible |
| Test Data | Username: Empty; Password: `secret_sauce` |
| Test Steps | 1. Open SauceDemo login page. 2. Leave username empty. 3. Enter valid password. 4. Click Login. |
| Expected Result | Error message contains `Username is required`; user must not successfully log in |
| Actual Result | "Username is required" error message was displayed and validated |
| Status | Pass |
| Automation Script | `tests/ui/test_login.py::test_invalid_login` — empty username data set |

### TC_LOGIN_004 — Verify Login with Empty Password

| Field | Details |
|---|---|
| Test Case ID | TC_LOGIN_004 |
| Test Scenario | Verify login validation when password is empty |
| Preconditions | SauceDemo login page is accessible |
| Test Data | Username: `standard_user`; Password: Empty |
| Test Steps | 1. Open SauceDemo login page. 2. Enter valid username. 3. Leave password empty. 4. Click Login. |
| Expected Result | Error message contains `Password is required`; user must not successfully log in |
| Actual Result | "Password is required" error message was displayed and validated |
| Status | Pass |
| Automation Script | `tests/ui/test_login.py::test_invalid_login` — empty password data set |

---

### Login Module — Execution Summary

| Test Case ID | Test Type | Result |
|---|---|---|
| TC_LOGIN_001 | Positive Testing | Pass |
| TC_LOGIN_002 | Negative Testing | Pass |
| TC_LOGIN_003 | Negative / Required Field Validation | Pass |
| TC_LOGIN_004 | Negative / Required Field Validation | Pass |
| **Total** | **4 Test Cases** | **4 Passed** |
