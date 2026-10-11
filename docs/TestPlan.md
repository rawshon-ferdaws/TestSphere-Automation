# TestSphere-Automation — Test Plan

## 1. Project Overview

| Field | Details |
|---|---|
| Project Name | TestSphere-Automation |
| Application Under Test (AUT) | SauceDemo |
| Application URL | https://www.saucedemo.com/ |
| Objective | Validate critical e-commerce functionality through manual test design and automated testing |
| Testing Approach | Functional, Regression, and Risk-Based Testing |
| Automation Framework | Python, Selenium WebDriver, PyTest |
| Design Pattern | Page Object Model (POM) |
| Test Environment | macOS, Google Chrome |
| Reporting Tool | Allure Reports |
| Defect Tracking Tool | Jira — TestSphere-Automation (KAN) |
| Test Strategy | `docs/TestStrategy.md` |
| Test Cases | `docs/TestCases.md` |
| Debugging Documentation | `docs/DebuggingIssues.md` |
| Current Execution Status | 12 Passed, 0 Failed |

## 2. Test Objectives

- Verify Login, Products, and Cart functionality against expected behavior.
- Validate positive and negative scenarios.
- Verify product sorting, cart updates, and product removal.
- Identify, investigate, and document test failures.
- Maintain reusable automated test scripts.
- Execute regression tests to verify existing functionality after changes.
- Extend test coverage to Checkout, API, and Integration testing in future phases.

## 3. Test Scope

| Module | Test Scenarios | Test Cases | Status |
|---|---|---:|---|
| Login | Valid login, invalid credentials, empty username, empty password | 4 | Completed |
| Products | Page validation, product listing, price sorting (ascending and descending) | 4 | Completed |
| Cart | Add one product, verify cart contents, remove product, add multiple products | 4 | Completed |
| Checkout | Customer information, field validation, order completion | TBD | Planned — Optional Extension |
| API | HTTP requests, response status codes, JSON validation, negative scenarios; target API/endpoints TBD | TBD | Planned |
| Integration / End-to-End | Component-interface validation and the complete login → products → cart → checkout workflow | TBD | Planned |
| **Current Total** | **Implemented UI automation** | **12** | **Completed** |

**Out of Scope — Current Phase:** Performance/load testing, penetration testing, cross-browser compatibility testing, and production deployment validation.

Checkout automation is a proposed extension beyond the current 12-test UI suite.

## 4. Testing Activities and Approaches

| Testing Activity / Approach | Application | Status |
|---|---|---|
| Functional Testing | Login, Products, Cart | Completed |
| Positive Testing | Valid login and successful product/cart operations | Completed |
| Negative Testing | Invalid credentials and empty required fields | Completed |
| Regression Testing | Execute the complete implemented UI suite after changes | Completed |
| Risk-Based Testing | Prioritize critical user workflows | Applied |
| Smoke Testing | Execute selected critical tests after new builds | Planned |
| API Testing | Validate REST API behavior using Python Requests and PyTest | Planned |
| Integration Testing | Verify interactions and interfaces between connected components | Planned |
| End-to-End Testing | Verify the complete login → products → cart → checkout workflow | Planned |
| Exploratory Testing | Investigate unexpected behavior manually | As Needed |

Risk-based testing guides test prioritization; exploratory testing is an experience-based test technique.

## 5. Test Environment

| Component | Configuration |
|---|---|
| Operating System | macOS |
| Browser | Google Chrome |
| Programming Language | Python 3.13.5 |
| UI Automation | Selenium WebDriver |
| Test Framework | PyTest |
| Design Pattern | POM |
| Development Tool | VS Code |
| Version Control | Git / GitHub |
| Test Reporting | Allure Reports |
| Defect Tracking | Jira |
| API Automation | Python Requests (Planned) |
| CI/CD | GitHub Actions (Planned) |

## 6. Test Data

| Module | Test Data |
|---|---|
| Login | `standard_user`, `secret_sauce`, `invalid_user`, `invalid_password`, empty fields |
| Products | Product names, product prices, sorting options |
| Cart | Sauce Labs Backpack, Sauce Labs Bike Light, expected cart counts |
| Checkout (Planned) | Customer information, valid and invalid input values |
| API (Planned) | Request payloads, expected status codes, JSON responses |

Test data will use demonstration credentials and non-sensitive values.

## 7. Test Execution Approach

1. Review test cases and expected results.
2. Verify the test environment and required test data.
3. Execute automated tests using PyTest.
4. Review test execution results and investigate failures.
5. Document debugging findings in `docs/DebuggingIssues.md`.
6. Track confirmed issues in Jira.
7. Update automation scripts when verified changes are needed.
8. Rerun failed tests and execute the regression suite.
9. Review Allure reporting results and record final execution status.

**Current Regression Execution Command:**

Run from the project directory with the project's virtual environment activated:

```bash
source .venv/bin/activate
python -m pytest tests/ui/ -v --alluredir=allure-results --clean-alluredir
```

**Generate and View Allure Report:**

```bash
allure serve allure-results
```

The `allure-results/` directory contains raw execution data. The `allure serve` command generates and opens a temporary HTML report.

**Current Execution Result:** 12 Passed, 0 Failed.

## 8. Entry and Exit Criteria

| Criteria | Description |
|---|---|
| Entry — Application | SauceDemo is accessible |
| Entry — Environment | Python, Chrome, Selenium, and PyTest are configured |
| Entry — Test Cases | Test cases and expected results are defined |
| Entry — Test Data | Required test data is available |
| Exit — Execution | All planned tests for the current phase are executed |
| Exit — Pass Criteria | All critical automated test cases pass |
| Exit — Defects | No unresolved blocker or critical application defects in the tested scope |
| Exit — Reporting | Execution results and known issues are documented |

These criteria apply to the portfolio's current test scope. Detailed test case documentation currently covers Login; Products and Cart case documentation remains in progress.

## 9. Defect Management

| Activity | Approach |
|---|---|
| Defect Identification | Identify unexpected behavior during test execution |
| Reproduction | Reproduce the issue and verify test data and environment |
| Documentation | Record steps, expected/actual results, logs, and error messages |
| Severity / Priority | Classify confirmed issues based on impact and urgency |
| Defect Tracking | Jira — TestSphere-Automation (KAN) |
| Technical Investigation | Document detailed findings in `docs/DebuggingIssues.md` |
| Retesting | Re-execute relevant tests after fixes |
| Regression | Run the automated regression suite |
| Defect Closure | Close verified issues after successful retesting |

**Current Practice:** Automation failures and debugging investigations are documented in `docs/DebuggingIssues.md`. Confirmed issues are tracked in Jira with reproduction steps, expected and actual results, root cause findings, resolution, verification, and issue status.

**Example — KAN-4: Cart Navigation Synchronization Failure**

- Issue Category: Test Automation Framework
- Problem: Cart page title validation returned "Products" instead of "Your Cart".
- Root Cause: Automation validated the title before Cart navigation completed.
- Resolution: Added an explicit wait for the Cart page title.
- Verification: All 4 Cart tests and the complete 12-test UI suite passed.
- Jira Status: Done

Automation framework defects are distinguished from application defects. A Selenium exception or failed assertion does not automatically indicate an application defect.

## 10. Roles and Responsibilities

| Role / Automation Capability | Responsibility |
|---|---|
| QA Automation Engineer (Project Owner) | Test planning, test case design, automation development, execution, debugging, Jira issue tracking, and documentation |
| Development Team | Not assigned — SauceDemo is an external demonstration application |
| CI/CD | Automated execution through GitHub Actions (Planned) |

## 11. Test Schedule and Milestones

| Phase | Deliverable | Status |
|---|---|---|
| Phase 1 | Framework setup and POM implementation | Completed |
| Phase 2 | Login Automation — 4 tests | Completed |
| Phase 3 | Products Automation — 4 tests | Completed |
| Phase 4 | Cart Automation — 4 tests | Completed |
| Phase 5 | Test Strategy, Test Plan, and Test Case documentation | In Progress |
| Phase 6 | Checkout Automation | Planned — Optional Extension |
| Phase 7 | API Testing using Python Requests and PyTest | Planned |
| Phase 8 | Integration / End-to-End Testing | Planned |
| Phase 9 | Allure Test Reporting | Completed |
| Phase 10 | GitHub Actions CI/CD | Planned |
| Phase 11 | GitHub Portfolio Documentation and Final Review | Planned |

Milestone dates will be assigned as future phases are scheduled.

## 12. Risks and Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Dynamic UI updates | Flaky tests or synchronization failures | Use explicit waits and reliable locators |
| Browser window closure | Selenium execution failures | Manage browser lifecycle through PyTest fixtures |
| Stale element references | Failed element interactions | Investigate element lifecycle and use fresh lookups where necessary |
| Changes to SauceDemo | Broken locators or assertions | Review page objects and update affected tests |
| Test data dependencies | Inconsistent test results | Use repeatable test data and isolated test execution |
| External application availability | Blocked test execution | Verify application availability before execution |

## 13. Test Deliverables

| Deliverable | File / Location | Status |
|---|---|---|
| Test Strategy | `docs/TestStrategy.md` | Drafted |
| Test Plan | `docs/TestPlan.md` | Updated |
| Test Cases | `docs/TestCases.md` | 4 Login cases documented; Products and Cart documentation pending |
| Debugging Documentation | `docs/DebuggingIssues.md` | Documented; ongoing updates |
| Jira Defect Tracking | Jira project KAN | In Progress |
| UI Automation Scripts | `tests/ui/` | 12 Tests Completed |
| Page Objects | `pages/` | Login, Products, Cart Completed |
| Test Execution Results | PyTest terminal output | 12 Passed |
| Allure Test Reporting | `allure-results/` and temporary HTML report | Completed |
| CI/CD Workflow | `.github/workflows/` | Planned |
| README | `README.md` | Final Update Planned |

Allure-generated results and reports are local execution artifacts and are normally excluded from Git version control. Reproduction instructions will be documented in the README.

## 14. Test Execution Summary

| Module | Total Tests | Passed | Failed |
|---|---:|---:|---:|
| Login | 4 | 4 | 0 |
| Products | 4 | 4 | 0 |
| Cart | 4 | 4 | 0 |
| **Total** | **12** | **12** | **0** |

**Pass Rate:** 100% for the currently implemented automated UI tests.

**Conclusion:** The current Login, Products, and Cart automation scope has completed regression execution successfully, with 12 passing tests. Allure reporting has been implemented, and Jira is being used for issue tracking. The project will continue with API Testing, Integration Testing, GitHub Actions CI/CD, and final portfolio documentation. Checkout automation remains an optional extension.
