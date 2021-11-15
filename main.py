from utils import *
from banco_de_dados.constantes_tabelas import *
from banco_de_dados.sqlhelper import *



def main():
    lista = []
    eletronica = SQLHELPER(r'dbs\banco.db')
    limpa()
    eletronica.cria_tabela(TABELA_CLIENTE)
    eletronica.cria_tabela(TABELA_APARELHO)
    menu()
    op2 = input(': ').lower()
    if op2 == 'c':
        lista.append(input('Nome: ').title())
        lista.append(input('Telefone: '))
        lista.append(input('Endereço: ').title())
        eletronica.inser_cliente(lista)
    elif op2 == 's':
        exit()
    elif op2 == 'l':
        limpa()
        eletronica.listar_clientes()
        input('\nEnter pra voltar')






if __name__ == '__main__':
    while True:
        main()