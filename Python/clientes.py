from getpass import getpass
from database import (
    username_existe,
    criar_cliente_db,
    obter_todos_clientes
)
from utils import limpar_ecra

def criar_cliente(user):

    limpar_ecra()
    print("=================================\n       NOVO CLIENTE\n=================================\n")

    cliente = {
        "nome": input("Nome: "),
        "nif": input("NIF: "),
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

        username = input("Username: ").strip()

        if not username:
            print("Username não pode ser vazio.")
            continue

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

def confirmar_cliente(cliente):
    limpar_ecra()
    print("\nConfirma a criação do cliente?")
    print(f"Nome: {cliente['nome']}")
    print(f"NIF: {cliente['nif']}")
    print(f"Morada: {cliente['morada']}")
    print(f"Email: {cliente['email']}")
    print(f"Telefone: {cliente['telefone']}")
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
    pass

def listar_clientes(user):
    limpar_ecra()

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