from datetime import date
from utils import *
from banco_de_dados.constantes_tabelas import *
from banco_de_dados.sqlhelper import *



def main():
    lista = []
    lista_ap = []
    eletronica = SQLHELPER(r'dbs\banco.db')
    limpa()
    eletronica.cria_tabela(TABELA_CLIENTE)
    eletronica.cria_tabela(TABELA_APARELHO)
    eletronica.cria_tabela(TABELA_ORCAMENTO)
    menu()
    op2 = input('        : ').lower()
    if op2 == 'c':
        lista.append(input('        Nome: ').title())
        lista.append(input('        Telefone: '))
        lista.append(input('        Endereço: ').title())
        eletronica.inser_cliente(lista)
    elif op2 == 'o':
        eletronica.orcamento()
    elif op2 == 's':
        exit()
    elif op2 == 'l':
        limpa()
        menu2()
        op3 = input('       :').lower()
        if op3 == 'c':
            menu3()
            op4 =input('        :').lower()
            if op4 == 'i':
                limpa()
                opcao = int(input('     Id: '))
                eletronica.lista_cliente(opcao)
            elif op4 == 'n':
                limpa()
                opcao = input('        Nome:')
                eletronica.lista_cliente(opcao.title())
            elif op4 =='t':
                limpa()
                opcao = input('        Telefone: ')
                eletronica.lista_cliente(opcao)
            elif  op4 == 'f':
                limpa()
                eletronica.listar_clientes()
        elif op3 == 'o':
            limpa()
            id_ap = input('       Id: ')
            eletronica.lista_orcamento(id_ap) 
        elif op3 == 'a':
            limpa()
            id_ap = input('       Id: ')
            eletronica.lista_aparelho(id_ap) 
            
        input(f'        {reset_color}\n              Enter pra voltar')
    elif op2 == 'e':
        ope = menu4()
        if ope == 'o':
            eletronica.editar_orcamento()
        elif ope == 'c':
            limpa()
            menu5()
            eletronica.editar_cliente(input('            : ').lower(),int(input('            Id: ')))
    elif op2 == 'a':
        limpa()
        lista_ap.append(input("     Id do cliente     :"))
        lista_ap.append(input("     Tipo do Aparelho  :"))
        lista_ap.append(input("     Marca do Aparelho :"))
        lista_ap.append(input("     Modelo do Aparelho:"))
        lista_ap.append(input("     Acessorios: ") or 'Sem Acessorio')
        lista_ap.append(input("     Observações: ") or 'Sem Observação')
        lista_ap.append(date.today())
        eletronica.cadastrar_aparelho(lista_ap)






if __name__ == '__main__':
    while True:
        main()