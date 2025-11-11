# 🌟 Selenite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green)](https://www.selenium.dev/)

> **Test websites in 3 clicks. No code.**

Selenite is an **automated testing hub with Selenium** made for **QAs, testers, and agile teams** who want to **quickly validate websites** without writing scripts from scratch.

> **"Enter the link. Provide the elements. Selenite does the rest."**

---

## ✨ Features

- Simple **terminal** interface
- Support for **CSS Selectors** and **XPath**
- Actions: `click`, `fill`, `check text`, `wait`
- Automatic validation of **visibility** and **content**
- Clear report with **PASS / FAIL**
- Browser opens and **closes automatically**
- Zero configuration with `webdriver-manager`

---
## ▶️ How to use

python selenite.py

🎯 Who is this for?

Manual QAs: Automate repetitive tests

Agile Teams: Quick validation in sprints

Freelancers: Check websites in minutes

Students: Practical Selenium learning

🛠️ Roadmap (Coming soon)

GUI (Tkinter)

Web dashboard (Flask)

Support for multiple scenarios

Report exporting (HTML/PDF)

Integration with GitHub Actions

🤝 Contribute!

Selenite is open-source and made for the community.

Found a bug? Open an issue

Want to add something? Send a Pull Request

📄 License

This project is licensed under the MIT License — use, modify, and distribute it freely.

💡 Selenite Philosophy

"A good tester doesn't write code. They make the code work for them."

Selenite — Because testing doesn't have to be complicated. Made with ❤️, Python, and automation by Filipe Araujo.

🚀 Installation

```bash
git clone [https://github.com/YOUR_USER/selenite.git](https://github.com/YOUR_USER/selenite.git)
cd selenite
pip install -r requirements.txt

---

<details>
<summary>Click to view full HTML documentation</summary>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Selenite – No-Code Selenium Test Hub</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 960px; margin: 40px auto; padding: 0 20px; }
    h1, h2, h3 { color: #24292e; }
    pre, code { background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }
    pre { padding: 16px; overflow: auto; border-radius: 6px; }
    blockquote { margin: 16px 0; padding: 0 1em; color: #6a737d; border-left: 4px solid #dfe2e5; }
    table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    th, td { padding: 8px 12px; border: 1px solid #dfe2e5; text-align: left; }
    th { background-color: #f6f8fa; }
    img { max-width: 100%; height: auto; }
    .badges img { margin-right: 8px; vertical-align: middle; }
    .footer { margin-top: 60px; font-size: 0.9em; color: #586069; text-align: center; }
  </style>
</head>
<body>

<h1>Selenite – No-Code Selenium Test Hub</h1>

<div class="badges">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python"></a>
  <a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-4.25%2B-green" alt="Selenium"></a>
  <a href="https://github.com/filipearaujo"><img src="https://img.shields.io/badge/Made%20in-Brazil-009c3b?style=flat&logo=brazil" alt="Made in Brazil"></a>
</div>

<blockquote>
  <p><strong>Test websites in 3 clicks. No code. Just results.</strong></p>
</blockquote>

<p><strong>Selenite</strong> is a <strong>no-code automation hub</strong> that lets <strong>QAs, testers, and agile teams</strong> run <strong>Selenium tests without writing a single line of Python</strong>.</p>

<blockquote>
  <p><strong>"Type the URL. Choose the plan. Get Excel + Word + Screenshots."</strong></p>
</blockquote>

<hr>

<h2>Features</h2>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>No-Code Interface</strong></td>
      <td>Create test plans via terminal (Option 0)</td>
    </tr>
    <tr>
      <td><strong>YAML Test Plans</strong></td>
      <td>Human-readable, reusable, shareable</td>
    </tr>
    <tr>
      <td><strong>Auto Reports</strong></td>
      <td>Excel (full execution) + Word (only defects)</td>
    </tr>
    <tr>
      <td><strong>Screenshots</strong></td>
      <td>Every step + full HD error evidence</td>
    </tr>
    <tr>
      <td><strong>Universal</strong></td>
      <td>100% English, ready for global teams</td>
    </tr>
    <tr>
      <td><strong>Zero Setup</strong></td>
      <td><code>webdriver-manager</code> handles Chrome</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Installation</h2>

<pre><code>git clone https://github.com/filipearaujo/selenite.git
cd selenite
pip install -r requirements.txt
</code></pre>

<p><strong>Requires:</strong> Python 3.8+</p>

<h3>Quick Start</h3>

<pre><code>python selenite.py
</code></pre>

<h3>Menu Options</h3>

<pre><code>1. Google Search Test
2. GitHub Login (Expected Fail)
3. SauceDemo Full Checkout
...
0. CREATE NEW CUSTOM PLAN (NO-CODE)
</code></pre>

<h3>Option 0 – Create Plan (No-Code)</h3>

<pre><code>Test name: Instagram Login
Website URL: instagram.com
Number of steps: 4

--- STEP 1 ---
Action: fill
Selector: input[name="username"]
Value: selenite_qa

--- STEP 2 ---
Action: fill
Selector: input[name="password"]
Value: wrongpass

--- STEP 3 ---
Action: click
Selector: button[type="submit"]

--- STEP 4 ---
Action: assert_text
Selector: div[role="alert"]
Contains: Incorrect password
</code></pre>

<ul>
  <li><strong>File saved:</strong> <code>testplans/Instagram_Login.yaml</code></li>
  <li><strong>Run now?</strong> <code>y</code> → Test executes instantly</li>
</ul>

<h3>Reports Generated</h3>

<p>After execution:</p>

<pre><code>reports/Login_Test_20251111_071500/
├── Login_Test_EXECUTION_PLAN.xlsx     # Full test log
├── Login_Test_DEFECTS.docx           # Only bugs (ready for Jira)
└── screenshots/
    ├── 00_homepage.png
    ├── 01_fill.png
    └── ERROR_04_assert_text.png
</code></pre>

<h3>Test Plan Examples (<code>testplans/</code>)</h3>

<pre><code># testplans/google_search.yaml
name: "Google Search Smoke Test"
url: "https://google.com"
steps:
  - action: fill
    selector: 'textarea[name="q"]'
    value: "Selenite QA"
  - action: press_end
  - action: assert_text
    selector: "div#search"
    contains: "github.com"
</code></pre>

<hr>

<h2>For Developers</h2>

<h3>Project Structure</h3>

<pre><code>selenite/
├── selenite.py              # Main menu + no-code creator
├── core/
│   └── reporter.py          # Excel + Word reports
├── testplans/               # YAML test plans
├── reports/                 # Auto-generated
├── screenshots/             # Per test
└── requirements.txt
</code></pre>

<h3>Add New Action</h3>

<p>Edit <code>selenite.py</code> → <code>run_plan()</code> → add:</p>

<pre><code>elif step["action"] == "your_action":
    # your code
</code></pre>

<h3>Roadmap</h3>

<table>
  <thead>
    <tr>
      <th>Version</th>
      <th>Feature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>v0.1.0</code></td>
      <td>No-code creator + reports</td>
    </tr>
    <tr>
      <td><code>v0.2.0</code></td>
      <td>Web UI (Flask)</td>
    </tr>
    <tr>
      <td><code>v0.3.0</code></td>
      <td>GitHub Actions CI</td>
    </tr>
    <tr>
      <td><code>v1.0.0</code></td>
      <td>Marketplace + SaaS</td>
    </tr>
  </tbody>
</table>

<h3>Contributing</h3>

<ol>
  <li>Fork it</li>
  <li>Create your feature branch</li>
  <li>Commit your changes</li>
  <li>Push to the branch</li>
  <li>Open a Pull Request</li>
</ol>

<h3>Author</h3>

<p><strong>Filipe Araujo</strong><br>
QA Automation | Python | Open Source</p>

<hr>

<h3>License</h3>

<p><a href="LICENSE">MIT License</a> – Free to use, modify, and distribute.</p>

<hr>

<p class="footer">
  <strong>Selenite</strong> – Because <strong>testing should be simple, fast, and universal</strong>.<br>
  Made with Python, passion, and Brazilian coffee.
</p>

</body>
</html>

</details>
