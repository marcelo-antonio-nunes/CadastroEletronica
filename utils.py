import os, platform

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

def menu():
    limpa()
    print(f"""
            {blue}ELETRONICA JN{reset_color}

        {blue}C{reset_color}){red} -> {reset_color}Cadastrar cliente
        {blue}L{reset_color}){red} -> {reset_color}Listar clientes
        {blue}E{reset_color}){red} -> {reset_color}Editar 
        {blue}A{reset_color}){red} -> {reset_color}Cadastrar Aparelo
        {blue}O{reset_color}){red} -> {reset_color}Orçar
        {blue}s{reset_color}){red} -> {reset_color}sair
    """)

def menu2():
    limpa()
    print(f"""
        {magenta}C{reset_color}){green}->{reset_color}Listar Clientes
        {magenta}A{reset_color}){green}->{reset_color}Listar Aparelho
        {magenta}O{reset_color}){green}->{reset_color}Listar Orçamento
    """)

def menu3():
    limpa()
    print(f"""
        {magenta}F{reset_color}){green}->{reset_color}Listar todos clientes
        {magenta}I{reset_color}){green}->{reset_color}Localizar por Id
        {magenta}N{reset_color}){green}->{reset_color}Localizar por Nome
        {magenta}T{reset_color}){green}->{reset_color}Localizar por Telefone
    """)


def menu4():
    limpa()
    res = input(f"""        {magenta}C{reset_color}){green}->{reset_color}Edditar clientes
        {magenta}O{reset_color}){green}->{reset_color}Editar Orçamento
        {magenta}A{reset_color}){green}->{reset_color}Editar Aparelho
    
        :""")
    return res

def menu5():
    print(f"""            {blue}N{reset_color}){green}Editar Nome
            {blue}T{reset_color}){green}Editar Telefone
            {blue}E{reset_color}){green}Editar Endereço{reset_color}
    """)