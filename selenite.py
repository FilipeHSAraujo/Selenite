# selenite.py
# -*- coding: utf-8 -*-
"""
SELENITE V1.1 – No-Code Selenium Test Hub
Author: Filipe Araujo
GitHub: https://github.com/FilipeHSAraujo/Selenite
"""
# IMPORTS

import os
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from colorama import Fore, Style, init
from utils.reporter import TestReporter

init(autoreset=True)


# CREATE CUSTOM TEST PLAN 
def create_custom_plan():
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{' CREATING NEW TEST PLAN – NO-CODE MODE ':-^60}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    name = input(f"{Fore.YELLOW}Test name: {Style.RESET_ALL}").strip() or "Custom_Test"
    url = input(f"{Fore.YELLOW}Website URL: {Style.RESET_ALL}").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        steps_count = int(input(f"{Fore.YELLOW}Number of steps (default 5): {Style.RESET_ALL}") or "5")
    except:
        steps_count = 5

    steps = []
    valid_actions = ["fill", "click", "press_enter", "wait", "wait_visible", "assert_text"]
    print(f"\n{Fore.MAGENTA}Enter {steps_count} steps:{Style.RESET_ALL}\n")

    for i in range(steps_count):
        print(f"{Fore.CYAN}--- STEP {i+1}/{steps_count} ---{Style.RESET_ALL}")
        print("Actions: fill | click | press_enter | wait | wait_visible | assert_text")
        action = input(f"Action: {Fore.GREEN}").strip().lower() or "click"
        if action not in valid_actions:
            action = "click"
            print(f"{Fore.RED}→ Invalid action → using 'click' as default{Style.RESET_ALL}")

        step = {"action": action}

        if action in ["fill", "click", "wait_visible", "assert_text"]:
            selector = input(f"Selector (CSS/XPath): {Fore.GREEN}").strip() or "#element"
            step["selector"] = selector

        if action == "fill":
            value = input(f"Value to type: {Fore.GREEN}").strip() or "test123"
            step["value"] = value

        if action == "assert_text":
            text = input(f"Expected text (contains): {Fore.GREEN}").strip() or "Success"
            step["contains"] = text

        if action == "wait":
            try:
                sec = int(input(f"Wait seconds: {Fore.GREEN}") or "3")
            except:
                sec = 3
            step["seconds"] = sec

        steps.append(step)
        print(f"{Fore.GREEN}Step {i+1} saved!{Style.RESET_ALL}\n")

    # Build final plan
    plan = {
        "name": name.replace(" ", "_"),
        "url": url,
        "timeout": 20,
        "steps": steps
    }

    # Save YAML file
    filename = f"testplans/{name.replace(' ', '_').replace('/', '_')}.yaml"
    with open(filename, "w", encoding="utf-8") as f:
        yaml.dump(plan, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\n{Fore.MAGENTA}TEST PLAN CREATED SUCCESSFULLY!{Style.RESET_ALL}")
    print(f"File → {filename}\n")
    print(f"{Fore.CYAN}{yaml.dump(plan, default_flow_style=False, allow_unicode=True)}{Style.RESET_ALL}")

    run_now = input(f"\n{Fore.YELLOW}Run this test now? (y/N): {Style.RESET_ALL}").strip().lower()
    if run_now in ["y", "yes", "s", "sim"]:
        run_plan(filename)
    else:
        print(f"{Fore.YELLOW}Cool! Just run 'python selenite.py' and select it later.{Style.RESET_ALL}")


# EXECUTE TEST PLAN
def run_plan(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as f:
        plan = yaml.safe_load(f)

    # Initialize reporter with URL for defect report
    reporter = TestReporter(plan["name"], plan.get("url", "URL not provided"))
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(plan["url"])
        reporter.save_screenshot(driver, "00_homepage")

        for i, step in enumerate(plan["steps"]):
            start_time = time.time()
            success = True
            error = None

            try:
                if step["action"] == "fill":
                    driver.find_element(By.CSS_SELECTOR, step["selector"]).send_keys(step["value"])
                elif step["action"] == "click":
                    driver.find_element(By.CSS_SELECTOR, step["selector"]).click()
                elif step["action"] == "press_enter":
                    driver.switch_to.active_element.send_keys(Keys.ENTER)
                elif step["action"] == "wait":
                    time.sleep(step["seconds"])
                elif step["action"] == "wait_visible":
                    WebDriverWait(driver, 15).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, step["selector"]))
                    )
                elif step["action"] == "assert_text":
                    elem = driver.find_element(By.CSS_SELECTOR, step["selector"])
                    actual = elem.text
                    expected = step.get("contains", "")
                    if expected and expected not in actual:
                        raise Exception(f"Expected '{expected}' → Found: '{actual}'")

                # Success screenshot
                screenshot_path = reporter.save_screenshot(driver, f"{i+1:02d}_{step['action']}")

            except Exception as e:
                success = False
                error = e
                screenshot_path = reporter.save_screenshot(driver, f"ERROR_{i+1:02d}_{step['action']}")

            duration = time.time() - start_time
            reporter.add_step(
                step_desc=f"{step['action']} → {step.get('selector', 'no selector')}",
                status=success,
                duration=duration,
                error=error,
                screenshot_path=screenshot_path
            )

        print(f"\n{Fore.GREEN}TEST COMPLETED SUCCESSFULLY!{Style.RESET_ALL}")

    finally:
        driver.quit()
        reporter.generate_reports()


# MAIN MENU
if __name__ == "__main__":
    if not os.path.exists("testplans"):
        os.makedirs("testplans")

    plans = [f for f in os.listdir("testplans") if f.endswith(".yaml")]

    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{' SELENITE V2.0 – NO-CODE TEST HUB ':-^60}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    if plans:
        for i, p in enumerate(plans):
            clean_name = p.replace('.yaml', '').replace('_', ' ')
            print(f"{Fore.CYAN}{i+1}. {Style.RESET_ALL}{clean_name}")

    print(f"\n{Fore.YELLOW}0. CREATE NEW CUSTOM PLAN (NO-CODE){Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'—'*60}{Style.RESET_ALL}")

    choice = input(f"\n{Fore.GREEN}Enter option: {Style.RESET_ALL}").strip()

    if choice == "0":
        create_custom_plan()
    elif choice.isdigit() and 1 <= int(choice) <= len(plans):
        run_plan(f"testplans/{plans[int(choice)-1]}")
    else:
        print(f"{Fore.RED}Invalid option! Try again.{Style.RESET_ALL}")