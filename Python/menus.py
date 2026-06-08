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
                        menu_admin(user)
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
    print("1. Login\n2. Criar Cliente\n3. Criar Conta\n0. Sair\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n--- Login ---\n")
                sleep(2)
                menu_admin(user)
            case "2":
                limpar_ecra()
                print("\n--- Criar Cliente ---\n")
                sleep(2)
                novo_cliente()
            case "3":
                limpar_ecra()
                print("\n--- Criar Conta ---\n")
                sleep(2)
                nova_conta(user)
            case "0":
                limpar_ecra()
                print("\n--- Sair ---\n")
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