# database/criar_usuarios.py

import sqlite3

def criar_tabela_usuarios():
    conexao = sqlite3.connect("transporte_escolar.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            data_nascimento TEXT,
            rg TEXT,
            cpf TEXT,
            cnh TEXT NOT NULL UNIQUE,
            funcao TEXT,
            endereco TEXT,
            foto TEXT
        )
    ''')

    # Verifica se já existe um usuário padrão 'admin'
    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute('''
            INSERT INTO usuarios (nome, usuario, senha, cnh)
            VALUES (?, ?, ?, ?)''', ("Administrador", "admin", "1234", "00000000000"))

    conexao.commit()
    conexao.close()
