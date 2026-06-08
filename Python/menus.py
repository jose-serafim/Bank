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
                if login():
                    print("\n--- LOGIN COM SUCESSO ---\n")
                    sleep(2)
                    menu_admin()
                else:
                    print("\n--- LOGIN FALHADO ---\n")
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

def menu_admin():
    limpar_ecra()
    print("=================================\n       SISTEMA BANCÁRIO\n=================================\n")
    print("1. Login\n2. Criar Cliente\n3. Criar Conta\n0. Sair\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n--- Login ---\n")
                sleep(2)
                menu_admin()
            case "2":
                limpar_ecra()
                print("\n--- Criar Cliente ---\n")
                sleep(2)
                novo_cliente()
            case "3":
                limpar_ecra()
                print("\n--- Criar Conta ---\n")
                sleep(2)
                nova_conta()
            case "0":
                limpar_ecra()
                print("\n--- Sair ---\n")
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_admin()

def novo_cliente():
    limpar_ecra()
    print("=================================\n       NOVO CLIENTE\n=================================\n")
    print("1. \n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n---     ---\n")
                sleep(2)
                novo_cliente()
            case "0":
                limpar_ecra()
                print("\n--- Voltar ---\n")
                sleep(2)
                menu_admin()
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                novo_cliente()

def nova_conta():
    limpar_ecra()
    print("=================================\n       NOVA CONTA\n=================================\n")
    print("1. \n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n---     ---\n")
                sleep(2)
                nova_conta()
            case "0":
                limpar_ecra()
                print("\n--- Voltar ---\n")
                sleep(2)
                menu_admin()
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                nova_conta()                


#menu_principal()