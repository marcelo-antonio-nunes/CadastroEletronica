import os
import platform

# Cores

reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"


def limpa():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')


def menu_plincipal():
  logo()
  print(f"""
  {blue}1{reset_color}){red} -> {reset_color}Cadastrar cliente
  {blue}2{reset_color}){red} -> {reset_color}Listar
  {blue}3{reset_color}){red} -> {reset_color}Editar 
  {blue}4{reset_color}){red} -> {reset_color}Cadastrar Aparelho
  {blue}5{reset_color}){red} -> {reset_color}Orçar
  {blue}s{reset_color}){red} -> {reset_color}sair
    """)


def menu_listar():
  logo()
  print(f"""
  {magenta}1{reset_color}){green}->{reset_color}Listar Clientes
  {magenta}2{reset_color}){green}->{reset_color}Listar Aparelho
  {magenta}3{reset_color}){green}->{reset_color}Listar Orçamento
    """)


def menu_listar_por():
  logo()
  print(f"""
  {magenta}1{reset_color}){green}->{reset_color}Listar todos clientes
  {magenta}2{reset_color}){green}->{reset_color}Localizar por Id
  {magenta}3{reset_color}){green}->{reset_color}Localizar por Nome
  {magenta}4{reset_color}){green}->{reset_color}Localizar por Telefone
    """)


def menu_editar():
  logo()
  res = input(f"""
  {magenta}1{reset_color}){green}->{reset_color}Editar clientes
  {magenta}2{reset_color}){green}->{reset_color}Editar Orçamento
  {magenta}3{reset_color}){green}->{reset_color}Editar Aparelho
  :""")
  return res


def menu_editar_por():
  logo()
  print(f"""  
  {blue}1{reset_color}){green}Editar Nome
  {blue}2{reset_color}){green}Editar Telefone
  {blue}3{reset_color}){green}Editar Endereço{reset_color}
    """)

def logo():
  limpa()
  print(f"""  
                 ELETRONICA{blue}

  ========================================={reset_color}
     SELECIONE O NUMERO DA OPÇÃO DESEJADA
     EM SEGUIDA APERTE O ENTER !{blue}
  ========================================={reset_color}
  """)