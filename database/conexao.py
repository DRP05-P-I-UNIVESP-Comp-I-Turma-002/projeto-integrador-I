# database/conexao.py
import sqlite3

def conectar():
    return sqlite3.connect("transporte_escolar.db")
