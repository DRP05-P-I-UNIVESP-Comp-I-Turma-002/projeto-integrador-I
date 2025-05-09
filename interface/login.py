import tkinter as tk
from tkinter import messagebox
from interface.interface_principal import iniciar_interface
from interface.cadastro_usuario import cadastrar_usuario  # <- Nova Lib adicionada
from database.estrutura import inicializar_banco


def mostrar_login():
    inicializar_banco()  # Garante que o banco e as tabelas estejam criados

    login = tk.Tk()
    login.title("Login")
    login.geometry("300x220")

    tk.Label(login, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(login)
    entry_usuario.pack()

    tk.Label(login, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(login, show="*")
    entry_senha.pack()

    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        from database.conexao import conectar
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            login.destroy()
            iniciar_interface()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    tk.Button(login, text="Entrar", command=autenticar).pack(pady=10)

    # Novo botão para cadastrar usuários, adicionadoa  pedido do Secretariado
    tk.Button(login, text="Cadastrar Novo Usuário",
              command=cadastrar_usuario).pack()

    login.mainloop()
