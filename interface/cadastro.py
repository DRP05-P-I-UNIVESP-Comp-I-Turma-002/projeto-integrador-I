import tkinter as tk
from tkinter import messagebox, filedialog
from database.conexao import conectar

def cadastrar_aluno():
    def selecionar_foto():
        caminho = filedialog.askopenfilename(
            title="Selecione a foto do aluno",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
        )
        entry_foto.delete(0, tk.END)
        entry_foto.insert(0, caminho)

    def salvar_aluno():
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        rota = entry_rota.get()
        motorista = entry_motorista.get()
        nome_pais = entry_pais.get()
        telefone = entry_telefone.get()
        observacoes = entry_obs.get()
        foto = entry_foto.get()

        if nome == "":
            messagebox.showwarning("Aviso", "O campo nome é obrigatório.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute('''
                INSERT INTO alunos (nome, endereco, rota, motorista, nome_pais, telefone, observacoes, foto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, endereco, rota, motorista, nome_pais, telefone, observacoes, foto))
            conexao.commit()
            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
            janela_cadastro.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")
        finally:
            conexao.close()

    # Criação da interface de cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastrar Aluno")
    janela_cadastro.geometry("350x450")

    # Campos
    tk.Label(janela_cadastro, text="Nome:").pack()
    entry_nome = tk.Entry(janela_cadastro, width=40)
    entry_nome.pack()

    tk.Label(janela_cadastro, text="Endereço:").pack()
    entry_endereco = tk.Entry(janela_cadastro, width=40)
    entry_endereco.pack()

    tk.Label(janela_cadastro, text="Rota:").pack()
    entry_rota = tk.Entry(janela_cadastro, width=40)
    entry_rota.pack()

    tk.Label(janela_cadastro, text="Motorista:").pack()
    entry_motorista = tk.Entry(janela_cadastro, width=40)
    entry_motorista.pack()

    tk.Label(janela_cadastro, text="Nome dos Pais:").pack()
    entry_pais = tk.Entry(janela_cadastro, width=40)
    entry_pais.pack()

    tk.Label(janela_cadastro, text="Telefone:").pack()
    entry_telefone = tk.Entry(janela_cadastro, width=40)
    entry_telefone.pack()

    tk.Label(janela_cadastro, text="Observações:").pack()
    entry_obs = tk.Entry(janela_cadastro, width=40)
    entry_obs.pack()

    tk.Label(janela_cadastro, text="Foto do Aluno:").pack()
    frame_foto = tk.Frame(janela_cadastro)
    frame_foto.pack()
    entry_foto = tk.Entry(frame_foto, width=28)
    entry_foto.pack(side=tk.LEFT)
    tk.Button(frame_foto, text="Selecionar", command=selecionar_foto).pack(side=tk.LEFT)

    tk.Button(janela_cadastro, text="Salvar", command=salvar_aluno).pack(pady=10)
