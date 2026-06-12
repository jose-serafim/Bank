from getpass import getpass
from time import sleep
from database import username_existe
from database import criar_cliente_db
from database import obter_todos_clientes
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

    while True:
        cliente['username'] = input("Username: ")
        if not username_existe(cliente['username']):
            break
        print("Username já existe.")
        sleep(1)

    while True:
        password = getpass("Password: ")
        confirmacao = getpass("Confirmar Password: ")

        if password == confirmacao:
            cliente['password'] = password
            break

        print("As passwords não coincidem.")

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
        for cliente in clientes:   
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"NIF: {cliente[2]}")
            print(f"Username: {cliente[3]}")
            print("---------------------------------")

    print("\nPrima Enter para voltar...")
    input()

def editar_cliente(user):
    pass

def remover_cliente(user):
    pass