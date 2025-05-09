# interface/pesquisa.py

import tkinter as tk
from tkinter import messagebox
from database.conexao import conectar

def pesquisar_aluno():  # já existente
    # sua lógica para pesquisar alunos
    pass

def pesquisar_usuario():  # NOVA FUNÇÃO
    janela = tk.Toplevel()
    janela.title("Pesquisar Usuário")
    janela.geometry("400x300")

    tk.Label(janela, text="Digite o nome de usuário:").pack(pady=5)
    entrada = tk.Entry(janela)
    entrada.pack(pady=5)

    lista = tk.Listbox(janela, width=60)
    lista.pack(pady=10)

    def buscar():
        nome_usuario = entrada.get()
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, usuario, funcao FROM usuarios WHERE usuario LIKE ?", ('%' + nome_usuario + '%',))
        resultados = cursor.fetchall()
        conexao.close()

        lista.delete(0, tk.END)
        for r in resultados:
            lista.insert(tk.END, f"Nome: {r[0]} | Usuário: {r[1]} | Função: {r[2]}")

    tk.Button(janela, text="Buscar", command=buscar).pack(pady=5)
