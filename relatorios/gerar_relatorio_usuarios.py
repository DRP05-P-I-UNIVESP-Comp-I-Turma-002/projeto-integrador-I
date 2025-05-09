# relatorios/gerar_relatorio_usuarios.py

from fpdf import FPDF
from tkinter import messagebox
from database.conexao import conectar

class PDFRelatorioUsuarios(FPDF):
    def header(self):
        self.image("relatorios/brasao_estado.png", 10, 8, 20)
        self.image("relatorios/brasao_municipio.png", 180, 8, 20)
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

def gerar_relatorio_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, usuario, data_nascimento, rg, cpf, cnh, funcao, endereco FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()

    pdf = PDFRelatorioUsuarios()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Relatório de Usuários - Sistema de Transporte", ln=True, align="C")
    pdf.ln(5)

    for user in usuarios:
        campos = ["Nome", "Usuário", "Data de Nascimento", "RG", "CPF", "CNH", "Função", "Endereço"]
        pdf.set_font("Arial", "", 11)
        for i, campo in enumerate(campos):
            pdf.set_font("Arial", "B", 11)
            pdf.cell(40, 8, f"{campo}:")
            pdf.set_font("Arial", "", 11)
            pdf.cell(0, 8, str(user[i]), ln=True)
        pdf.ln(5)

    output_path = "relatorios_gerados/relatorio_usuarios.pdf"
    pdf.output(output_path)

    messagebox.showinfo("Relatório", f"Relatório de usuários salvo em:\n{output_path}")
