# Books UI Automation Framework

## Project Overview

This project is a UI automation framework built to validate the functionality and reliability of the Books to Scrape website (https://books.toscrape.com/).

The framework is developed using Python, Playwright, and Pytest while following the Page Object Model (POM) design pattern to ensure maintainability, scalability, and reusability.

The project includes automated validation of key user workflows, report generation using HTML and Allure, and continuous execution through GitHub Actions.

### Live Allure Report

https://sabbirhosen44.github.io/Books-UI-Automation/

---

## Features

* Automated UI testing using Playwright
* Page Object Model (POM) architecture
* Cross-page navigation validation
* Data consistency verification
* Broken link detection
* Product image validation
* HTML report generation
* Allure report generation
* GitHub Actions CI integration
* Downloadable test artifacts from GitHub Actions

---

## Tech Stack

### Language

* Python 3.12

### Testing Framework

* Pytest

### Browser Automation

* Playwright

### Reporting

* Pytest HTML Report
* Allure Report

### CI/CD

* GitHub Actions

### Utilities

* Requests

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/sabbirhosen44/Books-UI-Automation.git

cd Books-UI-Automation
```

### Create Virtual Environment

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browser

```bash
playwright install chromium
```

---

## Environment Setup

The project currently uses a static configuration.

Base URL:

```python
BASE_URL = "https://books.toscrape.com/"
```

Configuration values are stored in:

```text
config/settings.py
```

No environment variables are required to execute the project.

---

## Running Tests

### Execute Complete Test Suite

```bash
pytest -v
```

### Execute Individual Test File

```bash
pytest tests/test_homepage.py -v
```

Example:

```bash
pytest tests/test_book_navigation.py -v
```

---

## Project Structure

```text
Books-UI-Automation/
│
├── .github/
│   └── workflows/
│       └── allure.yml
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── book_details_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_book_navigation.py
│   ├── test_book_consistency.py
│   ├── test_broken_links.py
│   └── test_product_images.py
│
├── utils/
│   ├── random_helper.py
│   └── link_checker.py
│
├── reports/
│   └── html/
│
├── allure-results/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Test Case Coverage

### Test Case 1: Homepage Validation

Objective:

Verify homepage loads correctly.

Validation:

* Homepage opens successfully
* Page title is displayed
* Product list is visible

---

### Test Case 2: Book Navigation Validation

Objective:

Verify users can navigate to book details.

Validation:

* Select a book from homepage
* Open product details page
* Verify navigation success

---

### Test Case 3: Data Consistency Validation

Objective:

Verify product information remains consistent.

Validation:

* Capture book title from homepage
* Open product details page
* Compare titles

Expected Result:

* Titles must match

---

### Test Case 4: Broken Link Validation

Objective:

Verify hyperlinks are functional.

Validation:

* Collect all anchor tags
* Extract href values
* Remove duplicates
* Send HTTP requests
* Validate response status

Expected Result:

* No broken links detected

---

### Test Case 5: Product Image Validation

Objective:

Verify product images load correctly.

Validation:

* Navigate through catalogue pages
* Verify image visibility
* Verify image source exists

Expected Result:

* Images load successfully

---

## Report Generation Guide

The framework generates two report formats:

1. HTML Report
2. Allure Report

Reports are generated automatically during test execution.

---

## HTML Report Guide

HTML reports are generated using pytest-html.

### Generate Report

```bash
pytest
```

Generated Location:

```text
reports/html/report.html
```

### Open Report

```bash
xdg-open reports/html/report.html
```

The report includes:

* Test execution summary
* Pass/fail status
* Execution duration
* Failure details

---

## Allure Report Guide

Allure provides a richer reporting dashboard with historical trends and test categorization.

### Generate Results

```bash
pytest
```

Generated Location:

```text
allure-results/
```

### Live Allure Dashboard

https://sabbirhosen44.github.io/Books-UI-Automation/

### Report Features

* Overview Dashboard
* Suites
* Behaviors
* Timeline
* Categories
* Execution History
* Failure Analysis

---

## GitHub Actions Setup

The project uses GitHub Actions for continuous integration.

Workflow Location:

```text
.github/workflows/allure.yml
```

### Workflow Capabilities

* Executes automatically on push
* Executes automatically on pull request
* Installs dependencies
* Installs Playwright browser
* Runs automation suite
* Generates Allure report
* Generates HTML report
* Uploads reports as downloadable artifacts

### Downloading Reports

Navigate to:

GitHub Repository → Actions → Workflow Run → Artifacts

Available downloads:

* allure-report
* html-report

---

## Design Decisions

### Page Object Model (POM)

The framework follows the Page Object Model design pattern.

Benefits:

* Improved maintainability
* Better code organization
* Reduced duplication
* Easier scalability

### Utility Layer

Reusable helper functions are isolated inside the utilities package.

Benefits:

* Cleaner test files
* Improved reusability
* Easier maintenance

### Centralized Configuration

Configuration values are maintained in a dedicated settings module.

Benefits:

* Single source of truth
* Easier updates

### Pytest Fixtures

Browser setup and teardown are managed through fixtures.

Benefits:

* Reduced boilerplate
* Consistent test execution

---

## Known Limitations

### External Website Dependency

The framework depends on the availability of:

https://books.toscrape.com/

If the website is unavailable, tests may fail.

### Network Restrictions

Broken link validation relies on outbound HTTP requests.

Corporate firewalls or network restrictions may affect results.

### Dynamic Website Changes

Locator updates may be required if website structure changes.

### Chromium-Focused Execution

The current implementation uses Chromium.

Additional browser coverage can be added if required.

---

## Future Improvements

* Cross-browser execution
* Parallel test execution
* Screenshot attachment on failure
* Historical Allure trend reporting
* Docker-based execution
* Environment-based configuration
* Test data management strategy

---

## Author

Sabbir Hosen

Automation Testing Assignment – Books UI Automation Framework
