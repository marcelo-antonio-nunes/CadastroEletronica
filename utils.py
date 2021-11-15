import os, platform


def limpa():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')

def menu():
    print("""
C)Cadastrar cliente
S)sair
    """)
