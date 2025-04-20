# interface/pesquisa.py

import tkinter as tk
from tkinter import messagebox
from database.conexao import conectar

# Esta função será chamada pelo botão "Pesquisar Aluno"
def pesquisar_aluno():
    janela_pesquisa = tk.Toplevel()
    janela_pesquisa.title("Pesquisar Aluno")
    janela_pesquisa.geometry("420x400")

    def buscar():
        nome = entry_nome.get()
        rota = entry_rota.get()

        conexao = conectar()
        cursor = conexao.cursor()

        query = "SELECT id, nome, endereco, rota, motorista, telefone FROM alunos WHERE 1=1"
        parametros = []

        if nome:
            query += " AND nome LIKE ?"
            parametros.append('%' + nome + '%')
        if rota:
            query += " AND rota LIKE ?"
            parametros.append('%' + rota + '%')

        cursor.execute(query, parametros)
        resultados = cursor.fetchall()
        conexao.close()

        lista_resultado.delete(0, tk.END)

        if resultados:
            for r in resultados:
                lista_resultado.insert(tk.END, f"{r[0]} - Nome: {r[1]} | End: {r[2]} | Rota: {r[3]} | Mot: {r[4]} | Tel: {r[5]}")
        else:
            lista_resultado.insert(tk.END, "Nenhum aluno encontrado.")

    def excluir():
        selecionado = lista_resultado.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um aluno para excluir.")
            return

        linha = lista_resultado.get(selecionado[0])
        id_aluno = linha.split("-")[0].strip()

        confirmacao = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este aluno?")
        if confirmacao:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Aluno excluído com sucesso.")
            buscar()

    def editar():
        selecionado = lista_resultado.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um aluno para editar.")
            return

        linha = lista_resultado.get(selecionado[0])
        id_aluno = linha.split("-")[0].strip()

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno,))
        aluno = cursor.fetchone()
        conexao.close()

        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado.")
            return

        janela_edicao = tk.Toplevel()
        janela_edicao.title("Editar Aluno")
        janela_edicao.geometry("350x450")

        campos = ["Nome", "Endereço", "Rota", "Motorista", "Nome dos Pais", "Telefone", "Observações"]
        entradas = []

        for i, campo in enumerate(campos):
            tk.Label(janela_edicao, text=f"{campo}:").pack()
            entry = tk.Entry(janela_edicao, width=40)
            entry.insert(0, aluno[i+1])
            entry.pack()
            entradas.append(entry)

        def salvar_alteracoes():
            novos_dados = [e.get() for e in entradas]
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute('''UPDATE alunos SET nome=?, endereco=?, rota=?, motorista=?, nome_pais=?, telefone=?, observacoes=? WHERE id=?''', (*novos_dados, id_aluno))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Alteracões salvas com sucesso!")
            janela_edicao.destroy()
            buscar()

        tk.Button(janela_edicao, text="Salvar Alterações", command=salvar_alteracoes).pack(pady=10)

    tk.Label(janela_pesquisa, text="Nome do aluno:").pack(pady=5)
    entry_nome = tk.Entry(janela_pesquisa, width=40)
    entry_nome.pack(pady=5)

    tk.Label(janela_pesquisa, text="Rota:").pack(pady=5)
    entry_rota = tk.Entry(janela_pesquisa, width=40)
    entry_rota.pack(pady=5)

    tk.Button(janela_pesquisa, text="Buscar", command=buscar).pack(pady=5)

    lista_resultado = tk.Listbox(janela_pesquisa, width=60)
    lista_resultado.pack(pady=10)

    frame_acoes = tk.Frame(janela_pesquisa)
    frame_acoes.pack(pady=5)

    tk.Button(frame_acoes, text="Editar", command=editar).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_acoes, text="Excluir", command=excluir).pack(side=tk.LEFT, padx=10)