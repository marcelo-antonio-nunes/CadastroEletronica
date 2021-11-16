import sqlite3
from sqlite3 import Error
from utils import *




class SQLHELPER():
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.cursor = self.conn.cursor()
        

    def cria_tabela(self,tabela):
        '''
            Função que cria uma tabela apartir 
            da constante recebida como parametro
        '''
        try:
            self.cursor.execute(tabela)
        except Error as e:
            print(f"Erro ao tentar criar tabela\n -> {e}")

    
    def inser_cliente(self,lista):
        try:
            '''
            lista deve conter os parametros, nome, telefone, endereco
            '''
            self.cursor.execute("INSERT INTO cliente(nome, telefone, endereco)\
                VALUES(?,?,?)",(lista))
            limpa()
            print(f"""
Os dados estão corretos? deseja inserir o cliente(a) {lista[0]} ? S/N
==============================================================================={'='*len(lista[0])+50}

Nome     : {lista[0]}
Telefone : {lista[1]}
Endereço : {lista[2]}

                """)
            op1 = input(': ').lower()
            if op1 == 's':
                self.conn.commit()
                print(f'Cliente(a) {lista[0]} cadastrado(a) com sucesso!!')
        except Error as e:
            print(f'Erro ao tentar inserir registro!\n -> {e}')

    def listar_clientes(self):
        for i in self.cursor.execute('select * from cliente'):
            print(f'Id       -> {i[0]}')
            print(f'Nome     -> {i[1]}')
            print(f'Telefone -> {i[2]}')
            print(f'Endereço -> {i[3]}')
            print('='*40)

