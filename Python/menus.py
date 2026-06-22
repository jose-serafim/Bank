#menus.py

from time import sleep
from utils import limpar_ecra
from auth import login
import clientes
import contas



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
                    limpar_ecra()
                    print(f"Bem-vindo {user['username']}")
                    sleep(1)
                    if user["role"] == "admin":
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
                #sleep(2)
                return
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_principal() 

def menu_admin(user):
    limpar_ecra()
    print("=================================\n       ADMINISTRAÇÃO\n=================================\n")
    print("1. Gestão de Utilizadores\n2. Gestão de Clientes\n3. Gestão de Contas\n4. Operações Bancárias\n5. Relatórios\n0. Logout\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                print("\n--- Gestão de Utilizadores ---\n")
                sleep(2)
                menu_admin(user)
            case "2":
                limpar_ecra()
                #print("\n--- Gestão de Clientes ---\n")
                #sleep(2)
                gestao_clientes(user)
            case "3":
                limpar_ecra()
                #print("\n--- Gestão de Contas ---\n")
                #sleep(2)
                gestao_contas(user)
            case "4":
                limpar_ecra()
                print("\n--- Operações Bancárias ---\n")
                sleep(2)
                menu_admin(user)
            case "5":
                limpar_ecra()
                print("\n--- Relatórios ---\n")
                sleep(2)
                menu_admin(user)
            case "0":
                limpar_ecra()
                print("\n--- Logout ---\n")
                #sleep(1)
                menu_principal()
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_admin(user)

def gestao_clientes(user):
    limpar_ecra()
    print("=================================\n       GESTÃO DE CLIENTES\n=================================\n")
    print("1. Novo Cliente\n2. Consultar Cliente\n3. Listar Clientes\n4. Editar Clientes\n5. Remover Cliente\n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                #print("\n--- Novo Cliente ---\n")
                #sleep(2)
                clientes.criar_cliente(user)
                gestao_clientes(user)
            case "2":
                limpar_ecra()
                #print("\n--- Consultar Cliente ---\n")
                #sleep(2)
                clientes.consultar_cliente(user)
                gestao_clientes(user)
            case "3":
                limpar_ecra()
                #print("\n--- Listar Clientes ---\n")
                #sleep(2)
                clientes.listar_clientes(user)
                gestao_clientes(user)
            case "4":
                limpar_ecra()
                #print("\n--- Editar Clientes ---\n")
                #sleep(2)
                clientes.editar_cliente(user)
                gestao_clientes(user)
            case "5":
                limpar_ecra()
                #print("\n--- Remover Cliente ---\n")
                #sleep(2)
                clientes.remover_cliente(user)
                gestao_clientes(user)
            case "0":
                limpar_ecra()
                #print("\n--- Voltar ---\n")
                menu_admin(user)
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                gestao_clientes(user)

def gestao_contas(user):
    limpar_ecra()
    print("=================================\n       GESTÃO DE CONTAS\n=================================\n")
    print("1. Nova Conta\n2. Consultar Conta\n3. Listar Contas\n4. Editar Contas\n5. Remover Conta\n0. Voltar\n")
    option = input("Escolha uma opção: ")
    match option:
            case "1":
                limpar_ecra()
                #print("\n--- Nova Conta ---\n")
                #sleep(2)
                contas.criar_conta(user)
                gestao_contas(user)
            case "2":
                limpar_ecra()
                print("\n--- Consultar Conta ---\n")
                sleep(2)
                gestao_contas(user)

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
                sleep(1)
                menu_principal()
            case _:
                limpar_ecra()
                print("\n--- Opção inválida ---\n")
                sleep(2)
                menu_client(user)           

#menu_principal()
