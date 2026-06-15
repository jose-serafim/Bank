#clientes.py

from getpass import getpass
from database import (
    username_existe,
    nif_existe,
    criar_cliente_db,
    obter_todos_clientes,
    obter_cliente_por_nif
)
import utils

def criar_cliente(user):

    utils.limpar_ecra()
    print("=================================\n       NOVO CLIENTE\n=================================\n")

    cliente = {
        "nome": utils.pedir_texto("Nome: "),
        "nif": pedir_nif(),
        "morada": input("Morada: "),
        "email": input("Email: "),
        "telefone": input("Telefone: ")
    }

    cliente["username"] = pedir_username()

    cliente["password"] = pedir_password()

    if confirmar_cliente(cliente):
        try:
            criar_cliente_db(cliente)
            print("\nCliente criado com sucesso!")
        except Exception as e:
            print(f"\nErro ao criar cliente: {e}")
    else:
        print("\nCriação de cliente cancelada.")        

    print("\nPrima Enter para voltar ao menu...")
    input()

def pedir_username():

    while True:

        username = utils.pedir_texto("Username: ")

        if not username_existe(username):
            return username

        print("Username já existe.")

def pedir_password():

    while True:

        password = getpass("Password: ")

        if not password:
            print("Password não pode ser vazia.")
            continue

        confirmacao = getpass("Confirmar Password: ")

        if password == confirmacao:
            return password

        print("As passwords não coincidem.")

def pedir_nif():

    while True:

        nif = utils.pedir_texto("NIF: ")

        if not utils.validar_nif(nif):
            print("NIF inválido.")
            continue

        if not nif_existe(nif):
            return nif

        print("Já existe um cliente com esse NIF.")

def confirmar_cliente(cliente):
    utils.limpar_ecra()
    print("\nConfirma a criação do cliente?")
    print(f"Nome: {cliente['nome']}")
    print(f"NIF: {cliente['nif']}")
    print(f"Morada: {cliente['morada'] or '-'}")
    print(f"Email: {cliente['email'] or '-'}")
    print(f"Telefone: {cliente['telefone'] or '-'}")
    print(f"Username: {cliente['username']}")

    while True:
        option = input("\n1. Confirmar\n0. Cancelar\nEscolha uma opção: ")

        match option:
            case "1":
                return True
            case "0":
                return False
            case _:
                print("Opção inválida.")

def consultar_cliente(user):
    utils.limpar_ecra()

    print("=================================")
    print("      CONSULTAR CLIENTE")
    print("=================================\n")

    while True:
        nif = utils.pedir_texto("NIF: ")

        if utils.validar_nif(nif):
            break

        print("NIF inválido.")

    cliente = obter_cliente_por_nif(nif)

    if not cliente:
        print("\nCliente não encontrado.")
    else:
        print("\nDados do cliente:\n")

        print(f"ID: {cliente[0]}")
        print(f"Nome: {cliente[1]}")
        print(f"NIF: {cliente[2]}")
        print(f"Morada: {cliente[3] or '-'}")
        print(f"Email: {cliente[4] or '-'}")
        print(f"Telefone: {cliente[5] or '-'}")
        print(f"Username: {cliente[6]}")

    print("\nPrima Enter para voltar...")
    input()

def listar_clientes(user):
    utils.limpar_ecra()

    print("=================================")
    print("       LISTA DE CLIENTES")
    print("=================================\n")

    clientes = obter_todos_clientes()

    if not clientes:
        print("Não existem clientes registados.")
    else:
        for id_cliente, nome, nif, username in clientes:

            print(f"ID: {id_cliente}")
            print(f"Nome: {nome}")
            print(f"NIF: {nif}")
            print(f"Username: {username}")
            print("---------------------------------")

    print("\nPrima Enter para voltar...")
    input()

def editar_cliente(user):
    pass

def remover_cliente(user):
    pass