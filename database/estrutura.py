# database/estrutura.py

from database.conexao import conectar

def verificar_coluna_foto():
    conexao = conectar()
    cursor = conexao.cursor()

    # Cria a tabela se ela não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        endereco TEXT,
                        rota TEXT,
                        motorista TEXT,
                        nome_pais TEXT,
                        telefone TEXT,
                        observacoes TEXT
                    )''')

    # Verifica se a coluna "foto" já existe e adiciona se necessário
    cursor.execute("PRAGMA table_info(alunos)")
    colunas = [col[1] for col in cursor.fetchall()]
    if "foto" not in colunas:
        cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")

    conexao.commit()
    conexao.close()
