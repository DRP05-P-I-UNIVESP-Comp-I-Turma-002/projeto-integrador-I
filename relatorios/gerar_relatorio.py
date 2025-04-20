# relatorios/gerar_relatorio.py

from fpdf import FPDF
from tkinter import messagebox
from database.conexao import conectar

def gerar_relatorio():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Título principal foi alterado para letra arial com BOld
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Relatório de Transporte Escolar", ln=True, align='C')
    pdf.ln(10)

    for aluno in alunos:
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Nome:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[1], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Endereço:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[2], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Rota:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[3], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Motorista:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[4], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Pais:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[5], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Telefone:")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, aluno[6], ln=True)

        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(30, 10, "Observações:")
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, aluno[7])  # Usa multi_cell para observações longas

        pdf.ln(5)  # Espaço entre alunos

    pdf.output("relatorios_gerados/relatorio_transporte.pdf")
    messagebox.showinfo("Relatório", "Relatório gerado com sucesso!")
