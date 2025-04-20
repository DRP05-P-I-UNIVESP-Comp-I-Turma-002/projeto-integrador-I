# interface/interface_principal.py

import tkinter as tk
from interface.cadastro import cadastrar_aluno
from interface.pesquisa import pesquisar_aluno
from relatorios.gerar_relatorio import gerar_relatorio
from carteirinha.gerar_carteirinha import gerar_carteirinhas

# Tornar visível para os outros módulos, se necessário. Podem ver que ela é declarada no escopo global do módulo. E ela cria janela primcipal na biblioteca Tkinter.
janela = None


def iniciar_interface():
    global janela
    janela = tk.Tk()
    janela.title("Sistema de Transporte Escolar")
    janela.geometry("300x220")

    titulo = tk.Label(janela, text="Menu Principal", font=("Arial", 14))
    titulo.pack(pady=10)

    btn_cadastrar = tk.Button(
        janela, text="Cadastrar Aluno", width=25, command=cadastrar_aluno)
    btn_cadastrar.pack(pady=5)

    btn_relatorio = tk.Button(
        janela, text="Gerar Relatório", width=25, command=gerar_relatorio)
    btn_relatorio.pack(pady=5)

    btn_carteirinha = tk.Button(
        janela, text="Gerar Carteirinhas", width=25, command=gerar_carteirinhas)
    btn_carteirinha.pack(pady=5)

    btn_pesquisar = tk.Button(
        janela, text="Pesquisar Aluno", width=25, command=pesquisar_aluno)
    btn_pesquisar.pack(pady=5)

    janela.mainloop()
