# selenite.py
import os
import yaml 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import colorama
colorama.init(autoreset=True)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.reporter import TestReporter

def run_plan(yaml_file):
    with open(yaml_file, encoding='utf-8') as f:
        plan = yaml.safe_load(f)

    reporter = TestReporter(plan["name"])
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(plan["url"])
        reporter.save_screenshot(driver, "00_homepage")
        
        for i, step in enumerate(plan["steps"]):
            start = time.time()
            status = True
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
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, step["selector"]))
                    )
                elif step["action"] == "assert_text":
                    elem = driver.find_element(By.CSS_SELECTOR, step["selector"])
                    text = elem.text
                    if step["contains"] not in text:
                        raise Exception(f"Texto esperado não encontrado: {step['contains']}")
                
                # Print de sucesso
                screenshot_path = reporter.save_screenshot(driver, f"{i+1:02d}_{step['action']}")

            except Exception as e:
                status = False
                error = e
                screenshot_path = reporter.save_screenshot(driver, f"ERROR_{i+1:02d}_{step['action']}")

            duration = time.time() - start
            reporter.add_step(
                step_desc=f"{step['action']} → {step.get('selector', '')}",
                status=status,
                duration=duration,
                error=error,
                screenshot_path=screenshot_path
            )

        print(f"\n{Fore.GREEN}TESTE FINALIZADO!{Style.RESET_ALL}")

    finally:
        driver.quit()
        reporter.generate_reports()

if __name__ == "__main__":
    plans = [f for f in os.listdir("testplans") if f.endswith(".yaml")]
    print("SELENITE V2.0 – Testes disponíveis:\n")
    for i, p in enumerate(plans):
        print(f"{i+1}. {p.replace('.yaml', '')}")
    
    escolha = int(input("\nEscolha o número do teste: ")) - 1
    run_plan(f"testplans/{plans[escolha]}")