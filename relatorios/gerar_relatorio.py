# relatorios/gerar_relatorio.py

from fpdf import FPDF
from tkinter import messagebox
import os
from database.conexao import conectar

class PDFRelatorio(FPDF):
    def header(self):
        # Brasões
        self.image("relatorios/brasao_estado.png", 10, 8, 20)   # Caminho relativo
        self.image("relatorios/brasao_municipio.png", 180, 8, 20)

        # Título central
        self.set_font("Arial", "B", 12)
        self.cell(0, 6, "ESTADO DE SÃO PAULO", align="C", ln=True)
        self.set_font("Arial", "", 11)
        self.cell(0, 6, "PREFEITURA MUNICIPAL DE ARAÇOIABA", align="C", ln=True)
        self.cell(0, 6, "SECRETARIA MUNICIPAL DA EDUCAÇÃO", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Av. Luane Milanda Oliveira, 108-600 - Jd N Sra Salete, Araçoiaba da Serra - SP, 18190-000", 0, 0, "C")

def gerar_relatorio():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    pdf = PDFRelatorio()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Relatório de Alunos - Transporte Escolar", ln=True, align="C")
    pdf.ln(5)

    for aluno in alunos:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Nome:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[1], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Endereço:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[2], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Rota:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[3], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Motorista:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[4], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Pais:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[5], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Telefone:")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, aluno[6], ln=True)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(30, 8, "Observações:")
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 8, aluno[7])

        pdf.ln(5)

    output_path = "relatorios_gerados/relatorio_oficial_prefeitura.pdf"
    pdf.output(output_path)

    messagebox.showinfo("Relatório", f"Relatório oficial salvo em:\n{output_path}")
