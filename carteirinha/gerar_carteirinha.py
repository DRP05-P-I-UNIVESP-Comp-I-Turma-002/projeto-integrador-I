# relatorios/gerar_carteirinha.py

from fpdf import FPDF
from tkinter import messagebox
import os
from database.conexao import conectar

def gerar_carteirinhas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, rota, foto FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    for aluno in alunos:
        nome, rota, foto = aluno

        pdf = FPDF("P", "mm", (90, 60))  # Formato tipo cartão
        pdf.set_auto_page_break(False)   # ✅ Desativa quebra automática, pois estava empurrando o rodapé
        pdf.set_margins(0, 0, 0)         # ✅ Remove margens padrão, pois estava empurrando o rodapé
        pdf.add_page()

        # Fundo e borda
        pdf.set_fill_color(255, 255, 255)
        pdf.rect(2, 2, 86, 56, style='D')

        # Faixa SP
        pdf.set_fill_color(200, 0, 0)
        pdf.rect(2, 2, 86, 8, style='F')
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(2, 10, 86, 3, style='F')
        pdf.set_fill_color(130, 130, 130)
        pdf.rect(2, 13, 86, 3, style='F')

        # Título
        pdf.set_xy(2, 17)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(86, 5, "CARTEIRINHA DE TRANSPORTE ESCOLAR", align="C")

        # Foto
        if foto and os.path.exists(foto):
            try:
                pdf.image(foto, x=5, y=23, w=18, h=22)  # ajustado a imagem, que tambpem estava empurrando o rodapé
            except:
                pdf.set_xy(5, 23)
                pdf.set_font("Arial", size=8)
                pdf.cell(18, 10, "Erro")

        # Dados
        pdf.set_xy(26, 23)
        pdf.set_font("Arial", "B", 7.5)
        pdf.cell(20, 4, "Nome:", ln=0)
        pdf.set_font("Arial", size=7.5)
        pdf.cell(0, 4, nome[:28])

        pdf.set_xy(26, 27.5)  # ⬅ posiciona na linha seguinte
        pdf.set_font("Arial", "B", 7.5)
        pdf.cell(20, 4, "Rota:", ln=0)
        pdf.set_font("Arial", size=7.5)
        pdf.cell(0, 4, rota[:28])  # ⚠️ SEM ln aqui para não empurrar o rodapé

        # Rodapé (ajustado!)
        pdf.set_xy(2, 51.5)  # ⬅ Agora seguro! Estava em 36 antes, pois o numero 36 por algum motivo empurra o rodapé para outra pagina
        pdf.set_font("Arial", size=6)
        pdf.cell(86, 4, "Prefeitura Municipal de Araçoiaba - Secretaria da Educação", align="C")

        # Linha azul debug opcional (limite inferior), preferimos não coloca-lo, pois ele serve apenas como referencia para o rodapé
        # pdf.set_draw_color(0, 0, 255)
        # pdf.line(0, 58, 90, 58)

        # Salvar
        nome_arquivo = f"carteirinhas_geradas/carteirinha_{nome.replace(' ', '_')}.pdf"
        pdf.output(nome_arquivo)

    messagebox.showinfo("Carteirinhas", "Carteirinhas geradas com sucesso!")
