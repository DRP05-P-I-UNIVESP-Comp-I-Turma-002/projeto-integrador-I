# interface/interface_principal.py

import tkinter as tk
from PIL import Image, ImageTk
from interface.cadastro import cadastrar_aluno
from interface.pesquisa import pesquisar_aluno, pesquisar_usuario
from relatorios.gerar_relatorio import gerar_relatorio
from carteirinha.gerar_carteirinha import gerar_carteirinhas
from relatorios.gerar_relatorio_usuarios import gerar_relatorio_usuarios

janela = None  # Visível globalmente, se necessário

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 3
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def iniciar_interface():
    global janela
    janela = tk.Tk()
    janela.title("Sistema de Transporte Escolar")
    janela.configure(bg="#f2f2f2")

    largura, altura = 420, 600
    centralizar_janela(janela, largura, altura)

    # Carrega e redimensiona os brasões
    imagem_sp = ImageTk.PhotoImage(Image.open("interface/brasao_estadoII.png").resize((80, 90)))
    imagem_municipio = ImageTk.PhotoImage(Image.open("interface/brasao_municipioII.png").resize((80, 86)))

    janela.imagem_sp = imagem_sp
    janela.imagem_municipio = imagem_municipio

    # ----- Cabeçalho com brasões -----
    frame_cabecalho = tk.Frame(janela, bg="#f2f2f2")
    frame_cabecalho.pack(pady=(10, 0))

    frame_brasoes = tk.Frame(frame_cabecalho, bg="#f2f2f2")
    frame_brasoes.pack()

    tk.Label(frame_brasoes, image=imagem_sp, bg="#f2f2f2").pack(side="left", padx=15)
    tk.Label(frame_brasoes, image=imagem_municipio, bg="#f2f2f2").pack(side="left", padx=15)

    tk.Label(frame_cabecalho,
             text="Sistema de Transporte Escolar",
             font=("Arial", 14, "bold"),
             bg="#f2f2f2").pack(pady=(8, 10))

    # ----- Título central -----
    tk.Label(janela,
             text="Menu Principal",
             font=("Arial", 18, "bold"),
             bg="#f2f2f2").pack(pady=15)

    # ----- Função para criar botões uniformes -----
    def criar_botao(texto, comando):
        return tk.Button(janela, text=texto, font=("Arial", 11), width=30,
                         height=2, command=comando, bg="#ffffff", relief="raised")

    # ----- Botões do menu -----
    botoes = [
        ("Cadastrar Aluno", cadastrar_aluno),
        ("Gerar Relatório de Alunos", gerar_relatorio),
        ("Gerar Carteirinhas", gerar_carteirinhas),
        ("Pesquisar Aluno", pesquisar_aluno),
        ("Gerar Relatório de Usuário", gerar_relatorio_usuarios),
        ("Pesquisar Usuário", pesquisar_usuario),
    ]

    for i, (texto, comando) in enumerate(botoes):
        espacamento = 6 if i < len(botoes) - 1 else 20  # Último botão ganha espaço extra
        criar_botao(texto, comando).pack(pady=espacamento)

    janela.mainloop()
