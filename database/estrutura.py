# database/estrutura.py

from database.conexao import conectar
from database.criar_usuarios import criar_tabela_usuarios

def verificar_coluna_foto():
    conexao = conectar()
    cursor = conexao.cursor()

    # Cria a tabela 'alunos' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            rota TEXT,
            motorista TEXT,
            nome_pais TEXT,
            telefone TEXT,
            observacoes TEXT
        )
    ''')

    # Verifica se a coluna 'foto' existe e adiciona se necessário
    cursor.execute("PRAGMA table_info(alunos)")
    colunas = [col[1] for col in cursor.fetchall()]
    if "foto" not in colunas:
        cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")

    conexao.commit()
    conexao.close()

def inicializar_banco():
    verificar_coluna_foto()
    criar_tabela_usuarios()  # Agora puxando da lógica certa
