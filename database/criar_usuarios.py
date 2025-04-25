import sqlite3  # Importa o módulo para conectar ao banco de dados SQLite

def criar_tabela_usuarios():
    # Estabelece conexão com o banco de dados
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()

    # Cria a tabela 'usuarios' se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chave primária automática
            usuario TEXT NOT NULL UNIQUE,           -- Nome de usuário (único)
            senha TEXT NOT NULL                     -- Senha (pode ser criptografada futuramente)
        )
    ''')

    # Verifica se já existe um usuário 'admin'
    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if cursor.fetchone() is None:
        # Insere o usuário padrão somente se ele ainda não existir
        cursor.execute("INSERT INTO usuarios (nome, usuario, senha) VALUES (?, ?, ?)", ("Administrador", "admin", "1234"))


    # Salva as alterações e encerra a conexão
    conexao.commit()
    conexao.close()
