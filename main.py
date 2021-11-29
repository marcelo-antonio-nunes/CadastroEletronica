from datetime import date
from utils import *
from banco_de_dados.constantes_tabelas import *
from banco_de_dados.sqlhelper import *


def main():
    lista = []
    lista_ap = []
    Path = 'dbs'
    if not os.path.exists(Path):
        os.makedirs(Path)
    if platform.system() == 'Windows':
        eletronica = SQLHELPER(r'dbs\\banco.db')
    else:
        eletronica = SQLHELPER(r'dbs/banco.db')
    logo()
    eletronica.cria_tabela(TABELA_CLIENTE)
    eletronica.cria_tabela(TABELA_APARELHO)
    eletronica.cria_tabela(TABELA_ORCAMENTO)
    menu_plincipal()
    op2 = input('  : ').lower()
    if op2 == '1':
        lista.append(input('  Nome: ').title())
        lista.append(input('  Telefone: '))
        lista.append(input('  Endereço: ').title())
        eletronica.inser_cliente(lista)
    elif op2 == '5':
        eletronica.orcamento()
    elif op2 == 's':
        eletronica.close_db()
        exit()
    elif op2 == '2':
        menu_listar()
        op3 = input('  :').lower()
        if op3 == '1':
            menu_listar_por()
            op4 = input('  :').lower()
            if op4 == '1':
                eletronica.listar_clientes()
            elif op4 == '2':
                opcao = int(input('  Id: '))
                eletronica.lista_cliente(opcao)
            elif op4 == '3':
                opcao = input('  Nome:')
                eletronica.lista_cliente(opcao.title())
            elif op4 == '4':
                opcao = input('  Telefone: ')
                eletronica.lista_cliente(opcao)
        elif op3 == '2':
            id_ap = input('  Id: ')
            eletronica.lista_aparelho(id_ap)
        elif op3 == '3':
            id_ap = input('  Id: ')
            eletronica.lista_orcamento(id_ap)
        input(f'  {reset_color}\n  Enter pra voltar')
    elif op2 == '3':
        ope = menu_editar()
        if ope == '2':
            eletronica.editar_orcamento()
        elif ope == '1':
            menu_editar_por()
            eletronica.editar_cliente(
                input('  :').lower(), int(input('  Id:')))
        elif ope == '3':
            eletronica.editar_aparelho()

    elif op2 == '4':
        logo()
        lista_ap.append(input("  Id do cliente     :"))
        lista_ap.append(input("  Tipo do Aparelho  :"))
        lista_ap.append(input("  Marca do Aparelho :"))
        lista_ap.append(input("  Modelo do Aparelho:"))
        lista_ap.append(input("  Acessorios: ") or 'Sem Acessorio')
        lista_ap.append(input("  Observações: ") or 'Sem Observação')
        lista_ap.append(date.today().strftime('%d/%m/%Y'))
        eletronica.cadastrar_aparelho(lista_ap)


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            limpa()
            print(f'   {red}Programa interrompido pelo usuario!{reset_color}')
            db = SQLHELPER(r'dbs\\banco.db')
            db.close_db()
            input('   Enter')
            break
