import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from fpdf import FPDF
import os

#estas duas linhas criam os diretorios (pastas) realtorios e carteririnhas de forma automatica
os.makedirs("relatorios", exist_ok=True)
os.makedirs("carteirinhas", exist_ok=True)

#função cria o banco de dados.
def criar_banco():
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        endereco TEXT,
                        rota TEXT,
                        motorista TEXT,
                        nome_pais TEXT,
                        telefone TEXT,
                        observacoes TEXT)''')
    conexao.commit()
    conexao.close()

# As funções vão aqui abixo e são elas (verificar_coluna_foto, cadastrar_aluno, gerar_relatorio, gerar_carteirinha)
# Garante que a coluna 'foto' exista no banco
def verificar_coluna_foto():
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA table_info(alunos)")
    colunas = [col[1] for col in cursor.fetchall()]
    if "foto" not in colunas:
        cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")
    conexao.commit()
    conexao.close()

# Chamar a verificação assim que o programa iniciar
verificar_coluna_foto()

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

        conexao = sqlite3.connect("transporte_escolar.db")
        cursor = conexao.cursor()

        try:
            cursor.execute('''INSERT INTO alunos 
                (nome, endereco, rota, motorista, nome_pais, telefone, observacoes, foto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (nome, endereco, rota, motorista, nome_pais, telefone, observacoes, foto))
            conexao.commit()
            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
            janela_cadastro.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")
        finally:
            conexao.close()
    
    
    # Janela de cadastro
    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.title("Cadastrar Aluno")
    janela_cadastro.geometry("350x450")

    # Campos de entrada
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
    btn_foto = tk.Button(frame_foto, text="Selecionar", command=selecionar_foto)
    btn_foto.pack(side=tk.LEFT)

    tk.Button(janela_cadastro, text="Salvar", command=salvar_aluno).pack(pady=10)



def gerar_relatorio():
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Relatório de Transporte Escolar", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)

    for aluno in alunos:
        pdf.cell(200, 10, f"Nome: {aluno[1]}", ln=True)
        pdf.cell(200, 10, f"Endereço: {aluno[2]}", ln=True)
        pdf.cell(200, 10, f"Rota: {aluno[3]}", ln=True)
        pdf.cell(200, 10, f"Motorista: {aluno[4]}", ln=True)
        pdf.cell(200, 10, f"Pais: {aluno[5]}", ln=True)
        pdf.cell(200, 10, f"Telefone: {aluno[6]}", ln=True)
        pdf.cell(200, 10, f"Observações: {aluno[7]}", ln=True)
        pdf.ln(10)

    pdf.output("relatorios/relatorio_transporte.pdf")
    messagebox.showinfo("Relatório", "Relatório gerado com sucesso!")


def gerar_carteirinha():
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, rota, foto FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    for aluno in alunos:
        nome = aluno[0]
        rota = aluno[1]
        foto = aluno[2]

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(200, 10, "Carteirinha de Transporte Escolar", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)

        if foto and os.path.exists(foto):
            try:
                pdf.image(foto, x=10, y=40, w=30, h=30)
                pdf.ln(35)
            except RuntimeError:
                pdf.cell(200, 10, "Erro ao carregar imagem.", ln=True)

        pdf.cell(200, 10, f"Nome: {nome}", ln=True)
        pdf.cell(200, 10, f"Rota: {rota}", ln=True)

        nome_arquivo = f"carteirinha_{nome.replace(' ', '_')}.pdf"
        pdf.output(f"carteirinhas/{nome_arquivo}")

    messagebox.showinfo("Carteirinhas", "Carteirinhas geradas com sucesso!")

# Atualização da funcao pesquisar_aluno

def pesquisar_aluno():
    janela_pesquisa = tk.Toplevel(janela)
    janela_pesquisa.title("Pesquisar Aluno")
    janela_pesquisa.geometry("420x400")

    def buscar():
        nome = entry_nome.get()
        rota = entry_rota.get()

        conexao = sqlite3.connect("transporte_escolar.db")
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
            conexao = sqlite3.connect("transporte_escolar.db")
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

        conexao = sqlite3.connect("transporte_escolar.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno,))
        aluno = cursor.fetchone()
        conexao.close()

        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado.")
            return

        janela_edicao = tk.Toplevel(janela)
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
            conexao = sqlite3.connect("transporte_escolar.db")
            cursor = conexao.cursor()
            cursor.execute('''UPDATE alunos SET nome=?, endereco=?, rota=?, motorista=?, nome_pais=?, telefone=?, observacoes=? WHERE id=?''',
                           (*novos_dados, id_aluno))
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


# Criar janela principal e botões do menu principal
janela = tk.Tk()
janela.title("Sistema de Transporte Escolar")
janela.geometry("300x220")

# Título (escolhi uma letra padrão Arial)
titulo = tk.Label(janela, text="Menu Principal", font=("Arial", 14))
titulo.pack(pady=10)

# Botões (fiquem a vontade para dimensionar o tamanho e formato deles)
btn_cadastrar = tk.Button(janela, text="Cadastrar Aluno", width=25, command=cadastrar_aluno)
btn_cadastrar.pack(pady=5)

btn_relatorio = tk.Button(janela, text="Gerar Relatório", width=25, command=gerar_relatorio)
btn_relatorio.pack(pady=5)

btn_carteirinha = tk.Button(janela, text="Gerar Carteirinhas", width=25, command=gerar_carteirinha)
btn_carteirinha.pack(pady=5)

btn_pesquisar = tk.Button(janela, text="Pesquisar Aluno", width=25, command=pesquisar_aluno)
btn_pesquisar.pack(pady=5)


# Iniciar a interface
janela.mainloop()
