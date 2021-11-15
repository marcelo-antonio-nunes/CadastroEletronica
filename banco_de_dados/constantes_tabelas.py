"""
Tabela Cliente
===============
-> id
-> nome
-> telefone
-> endereço
"""

TABELA_CLIENTE = """CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL, 
    telefone VARCHAR(100) NOT NULL, endereco VARCHAR(200) NOT NULL)"""

