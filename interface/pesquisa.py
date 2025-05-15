# interface/pesquisa.py

import tkinter as tk
from tkinter import messagebox
from database.conexao import conectar

def pesquisar_aluno():
    janela = tk.Toplevel()
    janela.title("Pesquisar Aluno")
    janela.geometry("400x300")

    tk.Label(janela, text="Digite o nome do aluno:").pack(pady=5)
    entrada = tk.Entry(janela)
    entrada.pack(pady=5)

    lista = tk.Listbox(janela, width=60)
    lista.pack(pady=10)

    def buscar():
        nome = entrada.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Digite um nome de aluno para buscar.")
            return

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, endereco, rota FROM alunos WHERE nome LIKE ?", ('%' + nome + '%',))
            resultados = cursor.fetchall()
            conexao.close()

            lista.delete(0, tk.END)
            if resultados:
                for r in resultados:
                    lista.insert(tk.END, f"Nome: {r[0]} | Endereço: {r[1]} | Rota: {r[2]}")
            else:
                lista.insert(tk.END, "Nenhum aluno encontrado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar: {e}")

    tk.Button(janela, text="Buscar", command=buscar).pack(pady=5)

def pesquisar_usuario():
    janela = tk.Toplevel()
    janela.title("Pesquisar Usuário")
    janela.geometry("400x300")

    tk.Label(janela, text="Digite o nome de usuário:").pack(pady=5)
    entrada = tk.Entry(janela)
    entrada.pack(pady=5)

    lista = tk.Listbox(janela, width=60)
    lista.pack(pady=10)

    def buscar():
        nome_usuario = entrada.get().strip()
        if not nome_usuario:
            messagebox.showwarning("Aviso", "Digite um nome de usuário para buscar.")
            return

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, usuario, funcao FROM usuarios WHERE usuario LIKE ?", ('%' + nome_usuario + '%',))
            resultados = cursor.fetchall()
            conexao.close()

            lista.delete(0, tk.END)
            if resultados:
                for r in resultados:
                    lista.insert(tk.END, f"Nome: {r[0]} | Usuário: {r[1]} | Função: {r[2]}")
            else:
                lista.insert(tk.END, "Nenhum usuário encontrado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar: {e}")

    tk.Button(janela, text="Buscar", command=buscar).pack(pady=5)
