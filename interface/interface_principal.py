import tkinter as tk
from interface.cadastro import cadastrar_aluno
from interface.pesquisa import pesquisar_aluno, pesquisar_usuario
from relatorios.gerar_relatorio import gerar_relatorio
from carteirinha.gerar_carteirinha import gerar_carteirinhas
from relatorios.gerar_relatorio_usuarios import gerar_relatorio_usuarios  # <- adicionado relatorio de usuarios aqui


# Tornar visível para os outros módulos, se necessário. Podem ver que ela é declarada no escopo global do módulo. E ela cria janela primcipal na biblioteca Tkinter.
janela = None


def iniciar_interface():
    global janela
    janela = tk.Tk()
    janela.title("Sistema de Transporte Escolar")
    janela.geometry("300x300")

    titulo = tk.Label(janela, text="Menu Principal", font=("Arial", 14))
    titulo.pack(pady=10)

    tk.Button(janela, text="Cadastrar Aluno", width=25,
              command=cadastrar_aluno).pack(pady=3)
    tk.Button(janela, text="Gerar Relatório", width=25,
              command=gerar_relatorio).pack(pady=3)
    tk.Button(janela, text="Gerar Carteirinhas", width=25,
              command=gerar_carteirinhas).pack(pady=3)
    tk.Button(janela, text="Pesquisar Aluno", width=25,
              command=pesquisar_aluno).pack(pady=3)

    # Novos botões de Gerar Rel. Usuario e de PEsquisar Usuario:
    tk.Button(janela, text="Gerar Relatório de Usuário", width=25,
              command=gerar_relatorio_usuarios).pack(pady=3)
    tk.Button(janela, text="Pesquisar Usuário", width=25,
              command=pesquisar_usuario).pack(pady=3)
    

    janela.mainloop()
