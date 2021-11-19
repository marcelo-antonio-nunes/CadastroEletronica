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
            print(f"Erro ao tentar criar tabela\n -> {e}")

    
    def inser_cliente(self,lista):
        try:
            self.cursor.execute("INSERT INTO cliente(nome, telefone, endereco)\
                VALUES(?,?,?)",(lista))
            limpa()
            print(f"""
            {blue}DADOS CLIENTE(A)
            SALVAR {lista[0]} ? S/N{cyan}
            ============={'='*len(lista[0])}{reset_color}
            {blue}Nome     {green}:{reset_color} {lista[0]}
            {blue}Telefone {green}:{reset_color} {lista[1]}
            {blue}Endereço {green}:{reset_color} {lista[2]}

                """)
            op1 = input('           : ').lower()
            if op1 == 's':
                self.conn.commit()
                print(f'Cliente(a) {lista[0]} cadastrado(a) com sucesso!!')
        except Error as e:
            print(f'Erro ao tentar inserir registro!\n -> {e}')

    def listar_clientes(self):
        limpa()
        for i in self.cursor.execute('select * from cliente'):
            print(f'    {blue}Id      {green} ->{reset_color} {i[0]}{blue}' )
            print(f'        Nome     {green}->{reset_color} {i[1]}{blue}'   )
            print(f'    Telefone {green}->{reset_color} {i[2]}{blue}'   )
            print(f'    Endereço {green}->{reset_color} {i[3]}{cyan}')
            print('    '+'='*30,reset_color)

    def editar_cliente(self,campo,id):
        try:
            if campo == 'n':
                nome = input("            Nome: ").title()
                self.cursor.execute(f"update cliente set nome = '{nome}' where id='{id}'")
            elif campo == 't':
                tel = input("            Telefone: ")
                self.cursor.execute(f"update cliente set telefone = '{tel}' where id='{id}'")
            elif campo == 'e':
                endereco = input("            Endereco: ").title()
                self.cursor.execute(f"update cliente set endereco = '{endereco}' where id='{id}'")
            self.conn.commit()
        except:
            print('     Opção invalida!')
        
    
    def cadastrar_aparelho(self,lista):
        self.cursor.execute("insert into aparelho(id_cliente, tipo, marca, modelo, acessorios, observacao, data_entrada)values\
            (?,?,?,?,?,?,?)",(lista))
        for c in self.cursor.execute(f"select nome from cliente where id ='{lista[0]}'"):
            Cliente = c
        limpa()
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

        op = input('        : ').lower()
        if op != 'n':
            self.conn.commit()
            print('             Aparelho cadastrado com sucesso!!')

    def lista_cliente(self,opcao):
        try:
                self.cursor.execute(f"select * from cliente where id='{opcao}'")
                limpa()
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
            {blue}ID       {green}->{reset_color} {c[0]}{blue}
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
            print('         Opção invalida!')

    

    def lista_orcamento(self,id_aparelho):
            limpa()
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
                pronto = lts[7]
                saida = lts[8]
                print(f"""
                
                ==========================ORÇAMENTO========================={blue}
                # Ordem de serviço {green}->{reset_color} {ordem_servico}{blue}
                # Defeito reclamado{green}->{reset_color} {defeito_reclamado}{blue}
                # Defeito          {green}->{reset_color} {defeito}{blue}
                # Componentes      {green}->{reset_color} {componentes}{blue}
                # Gasto            {green}->{reset_color} {gasto}{blue}
                # Mão de obra      {green}->{reset_color} {mao}{blue}
                # Pronto           {green}->{reset_color} {pronto}{blue}
                # Data de saida    {green}->{reset_color} {saida}{cyan}
                # ======================================={reset_color}""")
            except Exception as e:
                print(f"""              {red}NÃO A APARELHO ORÇADO COM ESSA ORDEM DE SERVIÇO!""")
    #========================================================================================

    def lista_aparelho(self,id_aparelho):
            limpa()
            try:

                for c in self.cursor.execute(f"select nome from cliente where id ='{id_aparelho}'"):
                    Cliente = c
                for a in self.cursor.execute(f"select * from aparelho where id_cliente = '{id_aparelho}' "):
                    print(f"""
                {blue}Os               {green}->{reset_color} {a[0]}{blue}
                Cliente          {green}->{reset_color} {str(Cliente).replace(",","").replace("(","").replace(")","").replace("'","")}{blue}
                Tipo             {green}->{reset_color} {a[2]}{blue}
                Marca            {green}->{reset_color} {a[3]}{blue}
                Modelo           {green}->{reset_color} {a[4]}{blue}
                Acessorios       {green}->{reset_color} {a[5]}{blue}
                Observação       {green}->{reset_color} {a[6]}{blue}
                Data de entrada  {green}->{reset_color} {a[7]}{cyan}
                
                ========={'='*len(str(Cliente))}{reset_color}""")
            except TypeError as e:
                print(f"""              {red}NÃO A APARELHO CADASTRADO EM NOME DE -> {str(Cliente).replace(",","")
                .replace("(","").replace(")","").replace("'","").upper()}{reset_color}!""")



#======================================================================================
    def orcamento(self):
        lista =[]
        try:
            lista.append(int(input(f'{blue}        Ordem de serviço: ')))
            ap = self.cursor.execute(f"select * from aparelho where id='{lista[0]}' ") #ok
            for i in ap.fetchall():
                id_cliente = i[1]
                tipo = i[2]
                marca = i[3]
                modelo = i[4]
            cl = self.cursor.execute(f"select * from cliente where id='{id_cliente}' ") #ok
            for j in ap.fetchall():
                clt = j[1]
            print(f"        {blue}Cliente {green}- {reset_color}{clt} ")
            print(f"        {blue}Aparelho {green}- {reset_color}{tipo} ")
            print(f"        {blue}Marca {green}- {reset_color}{marca} ")
            print(f"        {blue}Modelo {green}- {reset_color}{modelo} ")
            lista.append(input(f'{blue}        Defeito reclamado{red}:{reset_color}  '))
            lista.append(input(f'{blue}        Defeito{red}:{reset_color} ') or f'Em analise!')
            lista.append(input(f'{blue}        Componentes{red}:{reset_color} ') or 'Agrardando analise!')
            lista.append(input(f'{blue}        Gastos{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}        Mão de obra{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}        Aprovado{red}:{reset_color} ')or 'Agrardando analise!')
            lista.append(input(f'{blue}        Pronto{red}:{reset_color} ')or 'Ainda não!')
            lista.append(input(f'{blue}        Data de saida{red}:{reset_color} ')or 'Ainda sem previsão')
            self.cursor.execute("insert into orcamento(id_aparelho, defeito_reclamado, defeito,\
            componentes, gastos, mao_de_obra, aprovado, pronto, saida)VALUES(?,?,?,?,?,?,?,?,?)",(lista))
            ops = input('       DESEJA SALVAR OS DADOS? S/N\n\n:').lower()
            if ops !='n':
                self.conn.commit()
                limpa()
                print(f"        {green}DADOS SALVOS COM SUCESSO!!{reset_color}")
                input('         Enter pra voltar')
        except sqlite3.IntegrityError as e:
            print(f"        {red}JA FOI CRIADO O ORÇAMENTO DESTE APARELHO\n\
        TENTE EDITAR O ORÇAMENTO SE NECESSARIO!{reset_color}")
            input('         Enter pra voltar')

    def editar_orcamento(self):
        id = int(input("        Id:"))
        campo = input(f"""        {blue}D{reset_color})Editar defeito
        {blue}C{reset_color})Editar componentes
        {blue}G{reset_color})Editar gastos
        {blue}M{reset_color})Editar mão-de-obra
        {blue}A{reset_color})Editar aprovado
        {blue}P{reset_color})Editar pronto
        {blue}S{reset_color})Editar data de saida\n\n
        :""")

        
        if campo == 'd':
            self.cursor.execute(f"update orcamento set defeito = '{input('         Defeito:')}' where id_aparelho ='{id}'  ")
        elif campo == 'c':
            component = input('     Componentes:')
            self.cursor.execute(f"update orcamento set componentes = '{component}'where id_aparelho ='{id}'   ")
        elif campo == 'g':
            gasto = input('      Gastos:')
            self.cursor.execute(f"update orcamento set gastos = '{gasto}' where id_aparelho ='{id}'  ")
        elif campo == 'M':
            mao =input('      Mão_de-Obra:')
            self.cursor.execute(f"update orcamento set mao-de-obra = '{mao}' where id_aparelho ='{id}'   ")
        elif campo == 'A':
            apv = input('      Aprovado:')
            self.cursor.execute(f"update orcamento set aprovado = '{apv}' where id_aparelho ='{id}'   ")
        elif campo == 'P':
            pt = input('      Pronto:')
            self.cursor.execute(f"update orcamento set pronto = '{pt}' where id_aparelho ='{id}'  ")
        elif campo == 'S':
            sd =input('      Data-Saida:')
            self.cursor.execute(f"update orcamento set saida = '{sd}' where id_aparelho ='{id}'  ")
        self.conn.commit()
        

