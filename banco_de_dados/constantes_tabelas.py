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



"""
    Tabela Aparelho

    -> id
    -> id do cliente
    -> tipo
    -> modelo
    -> acessorios
    -> observações
    -> data de entrada
"""

TABELA_APARELHO = """ CREATE TABLE IF NOT EXISTS aparelho(
    id INTEGER PRIMARY KEY AUTOINCREMENT,id_cliente INTEGER NOT NULL,
     tipo VARCHAR(10) NOT NULL, marca VARCHAR(20) NOT NULL, modelo VARCHAR(20),
     acessorios VARCHAR(50), observacao VARCHAR(200), data_entrada DATE)
    """

TABELA_ORCAMENTO = """CREATE TABLE IF NOT EXISTS orcamento(id_aparelho INTEGER NOT NULL unique,
    defeito_reclamado VARCHAR(100) NOT NULL, defeito VARCHAR(100), componentes VARCHAR(100), gastos REAL,
    mao_de_obra REAL, aprovado VARCHAR(4), pronto VARCHAR(4), saida DATE)"""

