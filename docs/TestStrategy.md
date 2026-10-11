# TestSphere-Automation — Test Strategy

## 1. Project Overview

| Field | Details |
|---|---|
| Project Name | TestSphere-Automation |
| Application Under Test (AUT) | SauceDemo |
| Application URL | https://www.saucedemo.com/ |
| Objective | Validate critical e-commerce functionality through structured testing and automation |
| Testing Approach | Risk-Based, Functional, and Automated Regression Testing |
| Automation Framework | Python, Selenium WebDriver, PyTest |
| Design Pattern | Page Object Model (POM) |
| Test Environment | macOS, Google Chrome |
| Test Case Documentation | `docs/TestCases.md` |
| Debugging Documentation | `docs/DebuggingIssues.md` |
| Defect Tracking | Jira — TestSphere-Automation (KAN) |
| Test Reporting | Allure Reports |
| Current Execution Status | 12 Passed, 0 Failed |

## 2. Testing Objectives

- Verify critical e-commerce workflows against expected application behavior.
- Validate positive and negative test scenarios.
- Identify functional defects and unexpected behavior.
- Develop reusable, maintainable automated regression tests.
- Improve automation reliability through explicit waits and independent test execution.
- Document debugging investigations and track confirmed issues using Jira.
- Generate automated test execution reports using Allure.
- Support future API automation, continuous integration, and expanded test coverage.

## 3. Testing Scope

| Module | Testing Coverage | Status |
|---|---|---|
| Login | Valid login, invalid credentials, empty username/password | Completed |
| Products | Page validation, product listing, price sorting | Completed |
| Cart | Add product, verify cart contents, remove product, add multiple products | Completed |
| Checkout | Customer information, input validation, order completion | Planned — Optional Extension |
| API | REST API testing using Python Requests and PyTest; HTTP methods, status codes, JSON responses, and negative scenarios; target API/endpoints TBD | Planned |
| Integration / End-to-End | Component-interface validation and the complete login → products → cart → checkout workflow | Planned |

**Out of Scope (Current Phase):** Load/stress testing, security penetration testing, cross-browser compatibility testing, and production deployment validation.

Checkout automation is an optional extension beyond the current 12-test UI suite.

## 4. Testing Activities and Approaches

| Testing Activity / Approach | Application | Status |
|---|---|---|
| Functional Testing | Verify Login, Products, and Cart functionality | Completed |
| Positive Testing | Validate successful login and product/cart operations | Completed |
| Negative Testing | Validate invalid login credentials and required fields | Completed |
| Regression Testing | Execute all implemented automated tests after changes | Completed |
| Smoke Testing | Execute a selected subset of critical tests after new builds | Planned |
| API Testing | Validate REST API requests, responses, status codes, and negative scenarios | Planned |
| Integration Testing | Validate interactions and interfaces between connected components | Planned |
| End-to-End Testing | Validate the complete login → products → cart → checkout workflow | Planned |
| Risk-Based Testing | Prioritize critical user journeys, especially login and cart; checkout when implemented | Applied in test selection |
| Exploratory Testing | Manually investigate unexpected application behavior | As Needed |

Risk-based testing guides test prioritization; exploratory testing is an experience-based test technique.

## 5. Automation Strategy

- Automate stable, repeatable, and high-priority functional scenarios.
- Use Selenium WebDriver for browser interaction.
- Use PyTest for test execution, assertions, parametrization, and fixtures.
- Apply Page Object Model (POM) to separate page interactions from test logic.
- Use reusable methods for element interaction and synchronization.
- Apply explicit waits to handle dynamic UI behavior.
- Use function-scoped PyTest fixtures to provide a fresh browser for each test.
- Execute tests independently to reduce dependencies and improve reliability.
- Run regression tests after changes to automation code.
- Generate automated test execution reports using Allure Reports.
- Analyze test execution results and failures through PyTest and Allure.
- Track confirmed automation framework and application defects using Jira.
- Document technical debugging investigations in `docs/DebuggingIssues.md`.
- Use Python Requests with PyTest for REST API automation when the API testing module is implemented.
- Integrate automated test execution into CI/CD after GitHub Actions is configured.

## 6. Test Environment and Test Data

### Test Environment

| Component | Configuration |
|---|---|
| Application | SauceDemo |
| Operating System | macOS |
| Browser | Google Chrome |
| Programming Language | Python 3.13.5 |
| UI Automation Tool | Selenium WebDriver |
| Test Framework | PyTest |
| Design Pattern | Page Object Model (POM) |
| Development Environment | VS Code |
| Version Control | Git; GitHub hosting to be verified |
| Test Reporting | Allure Reports |
| Defect Tracking | Jira |
| API Automation | Python Requests (Planned) |
| CI/CD | GitHub Actions (Planned) |

### Test Data

| Module | Test Data |
|---|---|
| Login | `standard_user`, `secret_sauce`, invalid credentials, empty fields |
| Products | Product names, product prices, sorting options |
| Cart | Sauce Labs Backpack, Sauce Labs Bike Light, expected cart counts |
| API (Planned) | Valid/invalid request payloads, HTTP status codes, JSON responses |

Test data is based on publicly available SauceDemo demonstration accounts and products. No real customer data is required.

## 7. Defect Management

The following defect management process is used to identify, investigate, track, and resolve issues:

1. Identify unexpected application behavior or automation failures.
2. Reproduce the issue and verify test data and environment.
3. Document reproduction steps, expected and actual results, logs, and error messages.
4. Distinguish application defects from automation framework defects.
5. Classify confirmed issues based on severity and priority.
6. Track confirmed defects using Jira — TestSphere-Automation (KAN).
7. Document detailed technical investigations in `docs/DebuggingIssues.md`.
8. Retest resolved issues and execute relevant regression tests.
9. Move Jira issues to Done after successful verification.

**Current Practice:** Jira is used for defect tracking, while `docs/DebuggingIssues.md` contains detailed technical debugging documentation. Automation framework defects are distinguished from application defects.

**Example — KAN-4: Cart Navigation Synchronization Failure**

- **Issue Type:** Automation Framework Bug
- **Problem:** Cart page title validation returned "Products" instead of "Your Cart".
- **Root Cause:** The automation validated the page title before Cart navigation completed.
- **Resolution:** Added an explicit wait for the Cart page title.
- **Verification:** All 4 Cart tests and the complete 12-test UI suite passed.
- **Jira Status:** Done.

## 8. Entry and Exit Criteria

| Criteria | Definition |
|---|---|
| Entry — Application | SauceDemo is accessible and the required functionality is available |
| Entry — Environment | Chrome, Python, Selenium, and PyTest are configured |
| Entry — Test Data | Required credentials and product data are available |
| Entry — Test Readiness | Test cases and automation scripts are ready for execution |
| Exit — Execution | All planned critical tests for the current scope are executed |
| Exit — Pass Criteria | All critical test cases pass |
| Exit — Defects | No unresolved blocker or critical application defects within the tested scope |
| Exit — Documentation | Test execution results and known issues are documented |

These criteria apply to the TestSphere-Automation portfolio testing scope, not to SauceDemo's production release decisions. Detailed case documentation currently covers the 4 Login cases; Products and Cart case documentation remains in progress.

## 9. Testing Tools

| Tool / Design Pattern | Purpose | Status |
|---|---|---|
| Python | Automation programming | In Use |
| Selenium WebDriver | UI automation | In Use |
| PyTest | Test execution, assertions, fixtures, parametrization | In Use |
| Page Object Model (POM) | Reusable automation design pattern | In Use |
| VS Code | Development and debugging | In Use |
| Git | Version control | In Use |
| GitHub | Project hosting and portfolio presentation | Pending Verification |
| Allure Reports | Test execution reporting and result analysis | In Use |
| Jira | Defect tracking and issue lifecycle management | In Use |
| ChromeDriver Logs | Browser troubleshooting | Used during debugging |
| Python Requests | REST API automation, HTTP requests, response validation | Planned |
| Postman | Manual API testing and API exploration | Planned |
| GitHub Actions | CI/CD automation | Planned |

## 10. Test Execution Summary

| Module | Automated Test Cases | Passed | Failed |
|---|---:|---:|---:|
| Login | 4 | 4 | 0 |
| Products | 4 | 4 | 0 |
| Cart | 4 | 4 | 0 |
| **Total** | **12** | **12** | **0** |

**Pass Rate:** 100% for the 12 implemented UI automation tests.

**Current Outcome:** All 12 UI automation tests passed in the latest regression execution, achieving a 100% pass rate. Allure reporting has been implemented, and Jira is used for defect tracking and issue management. Checkout automation (optional), API testing, integration testing, GitHub Actions CI/CD, and final portfolio documentation remain planned activities.
