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
```

▶️ How to Use

Run Selenite directly from your terminal:

python selenite.py


You will be prompted with a menu:

Select an existing test plan (YAML file), or

Create a new no-code test plan interactively

🧠 Example Workflow

Choose “Create New Custom Plan (No-Code)”

Enter:

Test name

Target URL

Number of steps

Define each step (action, selector, value, etc.)

Selenite saves your test plan to testplans/ and asks if you want to execute it.

When executed:

Opens Chrome

Runs each step automatically

Takes screenshots

Generates reports in /reports/

📄 Example of a Test Plan (YAML)
name: Login_Test
url: https://example.com/login
timeout: 20
steps:
  - action: fill
    selector: "#username"
    value: "demo_user"
  - action: fill
    selector: "#password"
    value: "12345"
  - action: click
    selector: "button[type='submit']"
  - action: wait_visible
    selector: ".welcome-message"
  - action: assert_text
    selector: ".welcome-message"
    contains: "Welcome"

📊 Reports Generated

After execution, Selenite automatically creates:

📘 Excel Report
<PLAN_NAME>_EXECUTION_PLAN.xlsx
– All test steps with results (PASS/FAIL, duration, screenshots)

📕 Word Report (Defects Only)
<PLAN_NAME>_DEFECTS.docx
– Only failed steps, with steps to reproduce, errors, and screenshots

Reports are stored in:
reports/<plan_name>_<timestamp>/

🎯 Ideal For
Role	Benefit
🧪 Manual QAs	Automate repetitive web checks
⚙️ Agile Teams	Quick validation during sprints
💼 Freelancers	Verify client sites in minutes
🎓 Students	Learn Selenium concepts practically
🛠️ Roadmap

🪟 GUI with Tkinter

🌐 Web dashboard (Flask)

📁 Multiple test scenarios per plan

🧾 Report export to HTML / PDF

🤖 GitHub Actions integration

🤝 Contributing

Selenite is open-source and built for the testing community.

Found a bug? → Open an Issue

Want to add a feature? → Send a Pull Request!

📜 License

This project is licensed under the MIT License — free to use, modify, and distribute.

💡 Selenite Philosophy

“A good tester doesn’t write code — they make the code work for them.”

Selenite — Because testing doesn’t have to be complicated.
Made with ❤️, Python, and automation by Filipe Araujo.