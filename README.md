# Selenite – No-Code Automated Testing Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green)](https://www.selenium.dev/)
[![webdriver-manager](https://img.shields.io/badge/WebDriver%20Manager-Automatic-orange)](https://github.com/SergeyPirogov/webdriver_manager)

> **Test websites in 3 clicks. No code required.**

**Selenite** is a **no-code web automation testing tool** built with **Python + Selenium**, designed for **QAs, testers, students, and agile teams** who need to quickly validate websites — **without writing any code**.

> *“Enter the link. Define the steps. Selenite does the rest.”*

---

## Table of Contents
- Overview
- Features
- Technologies
- Installation
- How to Use
- Test Plan Example
- Generated Reports
- Who It's For
- Roadmap
- Contributing
- License

---

## Overview

**Selenite** turns Selenium web automation into a **simple, fast, and accessible** process, eliminating the need for custom scripts.

You define **what to test**, **how to test it**, and **on which site**, and Selenite handles everything automatically — generating **visual evidence** and **professional reports**.

---

## Features

- Simple **terminal-based** interface
- Full support for **CSS Selectors** and **XPath**
- Built-in actions:
  - `fill` → type into fields
  - `click` → click elements
  - `press_enter` → simulate Enter key
  - `wait` → pause execution
  - `wait_visible` → wait for element to appear
  - `assert_text` → validate text content
- Automatic validation of visibility and content
- Automatic screenshots (every step + errors)
- Auto-generated **Excel** execution reports
- **Word** defect reports (steps to reproduce + screenshots)
- Automatic driver installation with `webdriver-manager`
- Clean folder structure:
  - `testplans/` → your YAML plans
  - `screenshots/` → visual evidence
  - `reports/` → execution results
- Fully compatible with **Windows**, **Linux**, and **macOS**

---

## Technologies Used

- **Python 3.8+**
- **Selenium 4**
- **webdriver-manager**
- **PyYAML**
- **OpenPyXL**
- **python-docx**

---

##  Who It's For

| Profile             | Benefit                                   |
|---------------------|-------------------------------------------|
|  Manual QAs         | Automate repetitive tests                 |
|  Agile Teams        | Fast validation during sprints            |
|  Freelancers        | Test client sites in minutes              |
|  Students           | Learn Selenium in practice                |

---

##  Roadmap (Coming Soon)

-  Graphical interface (Tkinter)
-  Web dashboard (Flask)
-  Multiple scenarios per plan
-  Report export (HTML/PDF)
-  GitHub Actions integration

---

##  Contributors

<a href="https://github.com/FilipeHSAraujo/Selenite/graphs/contributors">
  <img src="https://contributors-img.firebaseapp.com/image?repo=FilipeHSAraujo/Selenite" />
</a>

Selenite is **open-source** and built for the testing community.

 Found a bug? → Open an Issue  
 Want to add something? → Send a Pull Request

---

##  License

This project is licensed under the **MIT License** — free to use, modify, and distribute.
