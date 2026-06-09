import os
from time import sleep
from utils import limpar_ecra
from auth import login



def menu_principal():
    limpar_ecra()
    print("=================================\n       BANCO SERAFIM\n=================================\n")
    print("1. Login \n0. Sair\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                user = login()
                if user:
                    print(f"Bem-vindo {user['username']}")
                    if user["tipo"] == "admin":
                        menu_admin(user)
                    else:
                        menu_client(user)
                else:
                    print("Credenciais inválidas")
                    sleep(2)
                    menu_principal()
                    
            case "0":
                limpar_ecra()
                print("\n--- SAIR ---\n")
                sleep(2)
                return
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_principal() 

def menu_admin(user):
    limpar_ecra()
    print("=================================\n       SISTEMA BANCÁRIO\n=================================\n")
    print("1. Gestão de Clientes\n2. Gestão de Contas\n3. Operações Bancárias\n4. Relatórios\n0. Logout\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n--- Gestão de Clientes ---\n")
                sleep(2)
                menu_admin(user)
            case "2":
                limpar_ecra()
                print("\n--- Gestão de Contas ---\n")
                sleep(2)
                menu_admin(user)
            case "3":
                limpar_ecra()
                print("\n--- Operações Bancárias ---\n")
                sleep(2)
                menu_admin(user)
            case "4":
                limpar_ecra()
                print("\n--- Relatórios ---\n")
                sleep(2)
                menu_admin(user)
            case "0":
                limpar_ecra()
                print("\n--- Logout ---\n")
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_admin(user)

def menu_client(user):
    limpar_ecra()
    print("=================================\n       SISTEMA BANCÁRIO\n=================================\n")
    print("1. Consultar Saldo\n2. Depositar\n3. Levantar\n4. Transferir\n5. Histórico\n6. Alterar Password\n0. Logout\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n--- Consultar Saldo ---\n")
                sleep(2)
                menu_client(user)
            case "2":
                limpar_ecra()
                print("\n--- Depositar ---\n")
                sleep(2)
                menu_client(user)
            case "3":
                limpar_ecra()
                print("\n--- Levantar ---\n")
                sleep(2)
                menu_client(user)
            case "4":
                limpar_ecra()
                print("\n--- Transferir ---\n")
                sleep(2)
                menu_client(user)
            case "5":
                limpar_ecra()
                print("\n--- Histórico ---\n")
                sleep(2)
                menu_client(user)
            case "6":
                limpar_ecra()
                print("\n--- Alterar Password ---\n")
                sleep(2)
                menu_client(user)
            case "0":
                limpar_ecra()
                print("\n--- Logout ---\n")
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_admin(user)

def novo_cliente(user):
    limpar_ecra()
    print("=================================\n       NOVO CLIENTE\n=================================\n")
    print("1. \n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n---     ---\n")
                sleep(2)
                novo_cliente(user)
            case "0":
                limpar_ecra()
                print("\n--- Voltar ---\n")
                sleep(2)
                menu_admin(user)
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                novo_cliente(user)

def nova_conta(user):
    limpar_ecra()
    print("=================================\n       NOVA CONTA\n=================================\n")
    print("1. \n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n---     ---\n")
                sleep(2)
                nova_conta(user)
            case "0":
                limpar_ecra()
                print("\n--- Voltar ---\n")
                sleep(2)
                menu_admin(user)
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                nova_conta(user)                


#menu_principal()
