import tkinter as tk
from tkinter import messagebox, filedialog
from database.conexao import conectar

def cadastrar_usuario():
    janela = tk.Toplevel()
    janela.title("Cadastrar Novo Usuário")
    janela.geometry("300x420")

    # Labels e Entradas
    campos = {
        "Nome Completo:": tk.StringVar(),
        "Usuário (login):": tk.StringVar(),
        "Senha:": tk.StringVar(),
        "Data de Nascimento (DD-MM-YYYY):": tk.StringVar(),
        "R.G.:": tk.StringVar(),
        "CPF:": tk.StringVar(),
        "CNH:": tk.StringVar(),
        "Função:": tk.StringVar(),
        "Endereço:": tk.StringVar(),
        "Foto:": tk.StringVar()
    }

    for texto, var in campos.items():
        tk.Label(janela, text=texto).pack()
        if texto == "Foto:":
            frame = tk.Frame(janela)
            frame.pack(pady=2)
            entrada_foto = tk.Entry(frame, textvariable=campos["Foto:"], width=25)
            entrada_foto.pack(side=tk.LEFT)
            tk.Button(frame, text="Selecionar", command=lambda: selecionar_foto(campos["Foto:"])).pack(side=tk.LEFT)
        else:
            tk.Entry(janela, textvariable=var, show="*" if "Senha" in texto else "").pack(pady=2)

    def salvar_usuario():
        dados = [var.get().strip() for var in campos.values()]

        if any(dado == "" for dado in dados):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO usuarios (
                    nome, usuario, senha, data_nascimento, rg,
                    cpf, cnh, funcao, endereco, foto
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, dados)
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro ao cadastrar usuário", str(e))

    def selecionar_foto(var_foto):
        caminho = filedialog.askopenfilename(
            title="Selecione uma foto",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if caminho:
            var_foto.set(caminho)

    tk.Button(janela, text="Salvar", command=salvar_usuario).pack(pady=10)
