# 🌟 Selenite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green)](https://www.selenium.dev/)
[![webdriver-manager](https://img.shields.io/badge/WebDriver%20Manager-Automatic-orange)](https://github.com/SergeyPirogov/webdriver_manager)

> **Test websites in 3 clicks. No code required.**

Selenite is a **no-code automated testing hub built with Selenium**, designed for **QAs, testers, and agile teams** who need to **quickly validate websites** — without writing any code.

> **"Enter the link. Define the steps. Selenite does the rest."**

---

## ✨ Features

- 🖥️ **Simple terminal interface** — no scripts required  
- 🧩 Supports **CSS Selectors** and **XPath**
- ⚡ Built-in actions:
  - `fill` → type into fields  
  - `click` → click elements  
  - `press_enter` → simulate Enter key  
  - `wait` → pause execution  
  - `wait_visible` → wait for element to appear  
  - `assert_text` → validate content
- ✅ Automatic validation of **visibility** and **text assertions**
- 📸 Screenshots saved for every step (and on errors)
- 📊 Automatic **Excel** and **Word defect reports**
- 🚗 Auto-installs browser drivers using `webdriver-manager`
- 🧾 Organized output folders (`reports/`, `testplans/`, `screenshots/`)
- 🔄 Works on **Windows**, **Linux**, and **macOS**

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USER/selenite.git
cd selenite
pip install -r requirements.txt
