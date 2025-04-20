# carteirinha/gerar_carteirinha.py

from fpdf import FPDF
import sqlite3
import os
from database.conexao import conectar

def gerar_carteirinhas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, rota, foto FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    for aluno in alunos:
        nome = aluno[0]
        rota = aluno[1]
        foto = aluno[2]

        pdf = FPDF()
        pdf.add_page()

        # Cabeçalho vermelho
        pdf.set_fill_color(204, 0, 0)  # Vermelho
        pdf.rect(0, 0, 210, 20, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", 'B', 16)
        pdf.set_xy(10, 5)
        pdf.cell(190, 10, "Carteirinha de Transporte Escolar", 0, 1, 'C')

        # Fundo cinza claro
        pdf.set_fill_color(240, 240, 240)
        pdf.rect(10, 30, 190, 100, 'F')

        # Inserir imagem (ajustada)
        if foto and os.path.exists(foto):
            try:
                pdf.image(foto, x=20, y=40, w=35, h=35)
            except RuntimeError:
                pass  # Silencia erro de imagem

        # Textos
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 12)
        pdf.set_xy(65, 40)
        pdf.cell(0, 10, "Nome:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.set_x(65)
        pdf.cell(0, 10, nome, ln=True)

        pdf.set_font("Arial", 'B', 12)
        pdf.set_x(65)
        pdf.cell(0, 10, "Rota:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.set_x(65)
        pdf.cell(0, 10, rota, ln=True)

        # Borda inferior preta
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(1)
        pdf.line(10, 140, 200, 140)

        # Salvar carteirinha
        nome_arquivo = f"carteirinhas_geradas/carteirinha_{nome.replace(' ', '_')}.pdf"
        pdf.output(nome_arquivo)

    from tkinter import messagebox
    messagebox.showinfo("Carteirinhas", "Carteirinhas geradas com sucesso!")
