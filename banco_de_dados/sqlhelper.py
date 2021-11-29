import sqlite3
from sqlite3 import Error
from utils import *





class SQLHELPER():
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.cursor = self.conn.cursor()
        

    def cria_tabela(self,tabela):
        try:
            self.cursor.execute(tabela)
        except Error as e:
            print(f"  {red}Erro ao tentar criar tabela\n -> {e}{reset_color}")

    
    def inser_cliente(self,lista):
        try:
            self.cursor.execute("INSERT INTO cliente(nome, telefone, endereco)\
                VALUES(?,?,?)",(lista))
            logo()
            print(f"""
  {reset_color}DADOS CLIENTE(A)
  SALVAR {lista[0]} ? S/N{blue}
  ============={'='*len(lista[0])}{reset_color}
  {blue}Nome     {green}:{reset_color} {lista[0]}
  {blue}Telefone {green}:{reset_color} {lista[1]}
  {blue}Endereço {green}:{reset_color} {lista[2]}

                """)
            op1 = input('  : ').lower()
            if op1 == 's':
                self.conn.commit()
                print(f'Cliente(a) {lista[0]} cadastrado(a) com sucesso!!')
        except Error as e:
            print(f'{red}  Erro ao tentar inserir registro!\n -> {e}{reset_color}')

    def listar_clientes(self):
        logo()
        for i in self.cursor.execute('select * from cliente'):
            print(f'    {blue}Id      {green} ->{reset_color} {i[0]}{blue}' )
            print(f'    Nome     {green}->{reset_color} {i[1]}{blue}'   )
            print(f'    Telefone {green}->{reset_color} {i[2]}{blue}'   )
            print(f'    Endereço {green}->{reset_color} {i[3]}{blue}')
            print('    '+'='*38,reset_color)

    def editar_cliente(self,campo,id):
        logo()
        try:
            if campo == '1':
                nome = input("  Nome: ").title()
                self.cursor.execute(f"update cliente set nome = '{nome}' where id='{id}'")
            elif campo == '2':
                tel = input("  Telefone: ")
                self.cursor.execute(f"update cliente set telefone = '{tel}' where id='{id}'")
            elif campo == '3':
                endereco = input("  Endereco: ").title()
                self.cursor.execute(f"update cliente set endereco = '{endereco}' where id='{id}'")
            self.conn.commit()
        except:
            print(f' {red} Opção invalida!{reset_color}')
        
    
    def cadastrar_aparelho(self,lista):
        logo()
        self.cursor.execute("insert into aparelho(id_cliente, tipo, marca, modelo, acessorios, observacao, data_entrada)values\
            (?,?,?,?,?,?,?)",(lista))
        for c in self.cursor.execute(f"select nome from cliente where id ='{lista[0]}'"):
            Cliente = c
        logo()
        print(f"""
                    {blue}DADOS DO APARELHO{reset_color}
                    ================={blue}
  Id do cliente       {green}->{reset_color} {lista[0]}{blue}
  cliente             {green}->{reset_color} {str(Cliente).replace("(",'').replace(")",'').replace(",",'').replace("'",'')}{blue}
  Tipo do Aparelho    {green}->{reset_color} {lista[1]}{blue}
  Marca do Aparelho   {green}->{reset_color} {lista[2]}{blue}
  Modelo do Aparelho  {green}->{reset_color} {lista[3]}{blue}
  Acessorios          {green}->{reset_color} {lista[4]}{blue}
  Observações         {green}->{reset_color} {lista[5]}{reset_color}

  Salvar ? S/N
        """)

        op = input('  : ').lower()
        if op == 's':
            self.conn.commit()
            print('  Aparelho cadastrado com sucesso!!')

    def lista_cliente(self,opcao):
        try:
                self.cursor.execute(f"select * from cliente where id='{opcao}'")
                logo()
                for c in self.cursor.fetchall():
                    print(f"""
  {blue}ID       {green}->{reset_color} {c[0]}{blue}
  Nome     {green}->{reset_color} {c[1]}{blue}
  Telefone {green}->{reset_color} {c[2]}{blue}
  Endereço {green}->{reset_color} {c[3]}{blue} 
                                """)
                self.cursor.execute(f"select * from cliente where nome like '%{opcao}%'")
                for c in self.cursor.fetchall():
                    print(f"""
  {blue}ID {green}->{reset_color} {c[0]}{blue}
  Nome     {green}->{reset_color} {c[1]}{blue}
  Telefone {green}->{reset_color} {c[2]}{blue}
  Endereço {green}->{reset_color} {c[3]}{blue} 
                                """)
                self.cursor.execute(f"select * from cliente where telefone='{opcao}'")
                for c in self.cursor.fetchall():
                    print(f"""
  ID       {green}->{reset_color} {c[0]}{blue}
  Nome     {green}->{reset_color} {c[1]}{blue}
  Telefone {green}->{reset_color} {c[2]}{blue}
  Endereço {green}->{reset_color} {c[3]} 
                                """)
        except:
            print(f'{red} Opção invalida!{reset_color}')

    

    def lista_orcamento(self,id_aparelho):
            logo()
            lts = []
            try:
                orc = self.cursor.execute(f"""select *from orcamento
                where orcamento.id_aparelho ='{id_aparelho}'""")
                res = [c for c in str(list(orc.fetchall())).split(",")]
                for c in res:
                    lts.append(c.replace("[","").replace("]","").replace("(","").replace(")","").replace("'",""))
                ordem_servico = lts[0]
                defeito_reclamado = lts[1]
                defeito = lts[2]
                componentes = lts[3]
                gasto = lts[4]
                mao = lts[5]
                aprovado = lts[6]
                pago = lts[7]
                pronto = lts[8]
                saida = lts[9]
                print(f"""{blue}
                
  Ordem de serviço {green}->{reset_color}  {ordem_servico}{blue}
  Defeito reclamado{green}->{reset_color} {defeito_reclamado}{blue}
  Defeito          {green}->{reset_color} {defeito}{blue}
  Componentes      {green}->{reset_color} {componentes}{blue}
  Gasto            {green}->{reset_color}  R${gasto}{blue}
  Mão de obra      {green}->{reset_color}  R${mao}{blue}
  Aprovado         {green}->{reset_color} {aprovado}{blue}
  Pago             {green}->{reset_color} {pago}{blue}
  Pronto           {green}->{reset_color} {pronto}{blue}
  Data de saida    {green}->{reset_color} {saida}{blue}
  ========================================={reset_color}""")
            except Exception as e:
                print(f"""  {red}NÃO A APARELHO ORÇADO COM ESSA ORDEM DE SERVIÇO!{reset_color}""")
    #================================

    def lista_aparelho(self,id_aparelho):
            logo()
            try:

                for c in self.cursor.execute(f"select nome from cliente where id ='{id_aparelho}'"):
                    Cliente = c
                for a in self.cursor.execute(f"select * from aparelho where id_cliente = '{id_aparelho}' "):
                    print(f"""
 {blue}Os         {green}->{reset_color} {a[0]}{blue}
 Cliente    {green}->{reset_color} {str(Cliente).replace(",","").replace("(","").replace(")","").replace("'","")}{blue}
 Tipo       {green}->{reset_color} {a[2]}{blue}
 Marca      {green}->{reset_color} {a[3]}{blue}
 Modelo     {green}->{reset_color} {a[4]}{blue}
 Acessorios {green}->{reset_color} {a[5]}{blue}
 Observação {green}->{reset_color} {a[6]}{blue}
 Data       {green}->{reset_color} {a[7]}{blue}
 ===========================================
                
  {reset_color}""")
            except TypeError as e:
                print(f"""  {red}NÃO A APARELHO CADASTRADO EM NOME DE -> {str(Cliente).replace(",","")
                .replace("(","").replace(")","").replace("'","").upper()}{reset_color}!""")



#==================================
    def orcamento(self):
        logo()
        lista =[]
        try:
            lista.append(int(input(f'{blue}  Ordem de serviço: ')))
            ap = self.cursor.execute(f"select * from aparelho where id='{lista[0]}' ") #ok
            for i in ap.fetchall():
                id_cliente = i[1]
                tipo = i[2]
                marca = i[3]
                modelo = i[4]
            cl = self.cursor.execute(f"select * from cliente where id='{id_cliente}' ") #ok
            for j in ap.fetchall():
                clt = j[1]
            print(f"  {blue}Cliente {green}- {reset_color}{clt} ")
            print(f"  {blue}Aparelho {green}- {reset_color}{tipo} ")
            print(f"  {blue}Marca {green}- {reset_color}{marca} ")
            print(f"  {blue}Modelo {green}- {reset_color}{modelo} ")
            lista.append(input(f'{blue}  Defeito reclamado{red}:{reset_color}  '))
            lista.append(input(f'{blue}  Defeito{red}:{reset_color} ') or f'Em analise!')
            lista.append(input(f'{blue}  Componentes{red}:{reset_color} ') or 'Agrardando analise!')
            lista.append(input(f'{blue}  Gastos{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}  Mão de obra{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}  Aprovado{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}  Pago{red}:{reset_color} ')or 'Ainda não!')
            lista.append(input(f'{blue}  Pronto{red}:{reset_color} ')or 'Ainda não!')
            lista.append(input(f'{blue}  Data de saida{red}:{reset_color} ')or 'Ainda sem previsão')
            self.cursor.execute("insert into orcamento(id_aparelho, defeito_reclamado, defeito,\
            componentes, gastos, mao_de_obra, aprovado, pronto, pago, saida)VALUES(?,?,?,?,?,?,?,?,?,?)",(lista))
            ops = input('  DESEJA SALVAR OS DADOS? S/N\n\n:').lower()
            if ops !='n':
                self.conn.commit()
                logo()
                print(f"  {green}DADOS SALVOS COM SUCESSO!!{reset_color}")
                input('  Enter pra voltar')
        except sqlite3.IntegrityError as e:
            print(f"  {red}JA FOI CRIADO O ORÇAMENTO DESTE APARELHO\n\
        TENTE EDITAR O ORÇAMENTO SE NECESSARIO!{reset_color}")
        except sqlite3.Error as e:
                    print(f'Error -> {e}')
        except UnboundLocalError:
                    print(f'  {red}Error -> Cliente ou aparelho não cadastrado!{reset_color}')
        input('  Enter pra voltar')

    def editar_orcamento(self):
        logo()
        id = int(input("  Id:"))
        campo = input(f"""  {blue}1{reset_color})Editar defeito
  {blue}2{reset_color})Editar componentes
  {blue}3{reset_color})Editar gastos
  {blue}4{reset_color})Editar mão-de-obra
  {blue}5{reset_color})Editar aprovado
  {blue}6{reset_color})Editar pronto
  {blue}7{reset_color})Editar pago
  {blue}8{reset_color})Editar data de saida\n\n
  :""")

        try:
            if campo == '1':
                self.cursor.execute(f"update orcamento set defeito = '{input('  Defeito:')}' where id_aparelho ='{id}'  ")
            elif campo == '2':
                component = input('  Componentes:')
                self.cursor.execute(f"update orcamento set componentes = '{component}'where id_aparelho ='{id}'   ")
            elif campo == '3':
                gasto = input('  Gastos:')
                self.cursor.execute(f"update orcamento set gastos = '{gasto}' where id_aparelho ='{id}'  ")
            elif campo == '4':
                mao =input('  Mão_de-Obra:')
                self.cursor.execute(f"update orcamento set mao-de-obra = '{mao}' where id_aparelho ='{id}'   ")
            elif campo == '5':
                apv = input('  Aprovado:')
                self.cursor.execute(f"update orcamento set aprovado = '{apv}' where id_aparelho ='{id}'   ")
            elif campo == '6':
                pt = input('  Pronto:')
                self.cursor.execute(f"update orcamento set pronto = '{pt}' where id_aparelho ='{id}'  ")
            elif campo == '7':
                pt = input('  Pronto:')
                self.cursor.execute(f"update orcamento set pronto = '{pt}' where id_aparelho ='{id}'  ")
            elif campo == '8':
                sd =input('  Data-Saida:')
                self.cursor.execute(f"update orcamento set saida = '{sd}' where id_aparelho ='{id}'  ")
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'{red}Error -> {e}{reset_color}')
            input('Enter')
        

    def editar_aparelho(self):
        logo()
        id=input('  ID:')
        logo()
        print(f"""
        {blue}1{reset_color}){green}Editar id cliente
        {blue}2{reset_color}){green}Editar Tipo de aparelho
        {blue}3{reset_color}){green}Editar Marca
        {blue}4{reset_color}){green}Editar Modelo
        {blue}5{reset_color}){green}Editar acessorios
        {blue}6{reset_color}){green}Editar Observações
        {blue}7{reset_color}){green}Editar Data de entrada{reset_color}
    """)
        campo = input('  :')
        if campo == '1':
            self.cursor.execute(f"update aparelho set id_cliente = '{input('  id_cliente:')}' where id ='{id}'  ")
        elif campo == '2':
            tipo = input('  Tipo:')
            self.cursor.execute(f"update aparelho set tipo = '{tipo}'where id ='{id}'   ")
        elif campo == '3':
            marca = input('  Marca:')
            self.cursor.execute(f"update aparelho set marca = '{marca}' where id ='{id}'  ")
        elif campo == '4':
            modelo =input('  Modelo:')
            self.cursor.execute(f"update aparelho set modelo = '{modelo}' where id ='{id}'   ")
        elif campo == '5':
            acessorios = input('  Acessorios:')
            self.cursor.execute(f"update aparelho set acessorios = '{acessorios}' where id ='{id}'   ")
        elif campo == '6':
            observacao = input('  Observacao:')
            self.cursor.execute(f"update aparelho set observacao = '{observacao}' where id ='{id}'  ")
        elif campo == '7':
            data_entrada =input('  Data-Entrada:')
            self.cursor.execute(f"update aparelho set data_entrada = '{data_entrada}' where id ='{id}'  ")
        try:
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'{red}Error -> {e}{reset_color}')
            input('Enter')



    def close_db(self):
    	self.conn.close()