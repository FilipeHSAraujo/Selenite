#Imports
import os
import pandas as pd
from datetime import datetime
from docx import Document
from docx.shared import Inches
from colorama import Fore, Style, init

init(autoreset=True)

#Functions
class TestReporter:
    def __init__(self, plan_name, plan_url=""):
        self.plan_name = plan_name.replace(" ", "_").replace("/", "_")
        self.plan_url = plan_url
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results = []
        self.report_dir = f"reports/{self.plan_name}_{self.timestamp}"
        os.makedirs(self.report_dir, exist_ok=True)
        os.makedirs(f"{self.report_dir}/screenshots", exist_ok=True)

    def add_step(self, step_desc, status, duration=None, error=None, screenshot_path=None):
        result = {
            "Passo": step_desc,
            "Status": "PASS" if status else "FAIL",
            "Duração (s)": round(duration, 3) if duration else "-",
            "Erro": str(error) if error else "-",
            "Print": os.path.basename(screenshot_path) if screenshot_path else "-"
        }
        self.results.append(result)

    def save_screenshot(self, driver, name):
        safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "_", "-")).rstrip()
        path = f"{self.report_dir}/screenshots/{safe_name}.png"
        driver.save_screenshot(path)
        return path

    def generate_excel(self):
        df = pd.DataFrame(self.results)
        excel_path = f"{self.report_dir}/{self.plan_name}_PLAN.xlsx"
        df.to_excel(excel_path, index=False)
        print(f"{Fore.GREEN}PLAN → {excel_path}{Style.RESET_ALL}")

    def generate_word_defects(self):
        # Só gera Word se tiver pelo menos 1 FAIL
        if not any(r["Status"] == "FAIL" for r in self.results):
            print(f"{Fore.YELLOW}Sem erros! Relatório de defeitos não gerado.{Style.RESET_ALL}")
            return

        doc = Document()
        doc.add_heading("RELATÓRIO DE DEFEITOS - SELENITE", 0)
        doc.add_paragraph(f"Projeto: {self.plan_name}")
        doc.add_paragraph(f"URL: {self.plan_url}")
        doc.add_paragraph(f"Executado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        doc.add_paragraph("")

        bug_count = 0
        for i, res in enumerate(self.results):
            if res["Status"] == "FAIL":
                bug_count += 1
                doc.add_heading(f"BUG {bug_count} - {res['Passo']}", level=1)

                # Passos para reproduzir
                p = doc.add_paragraph()
                p.add_run("Passos para reproduzir:\n").bold = True
                for j, passo in enumerate(self.results[:i + 1]):
                    status_emoji = "PASS" if passo["Status"] == "PASS" else "FAIL"
                    p.add_run(f"{j + 1}. {passo['Passo']} [{status_emoji}]\n")

                # Erro técnico
                if res["Erro"] != "-":
                    doc.add_paragraph(f"Erro: {res['Erro']}", style="Intense Quote")

                # Evidência
                doc.add_paragraph("Evidência:", style="Intense Quote")
                if res["Print"] != "-":
                    img_path = f"{self.report_dir}/screenshots/{res['Print']}"
                    if os.path.exists(img_path):
                        doc.add_picture(img_path, width=Inches(6.5))
                        doc.add_paragraph(f"Print: {res['Print']}")

                doc.add_page_break()

        word_path = f"{self.report_dir}/{self.plan_name}_DEFEITOS.docx"
        doc.save(word_path)
        print(f"{Fore.RED}DEFEITOS → {word_path}{Style.RESET_ALL}")

    def generate_reports(self):
        self.generate_excel()
        self.generate_word_defects()
        print(f"{Fore.MAGENTA}RELATÓRIOS PRONTOS → {self.report_dir}{Style.RESET_ALL}")