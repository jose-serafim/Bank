#utils.py

import os

def limpar_ecra():
    os.system('clear' if os.name == 'posix' else 'cls')

def pedir_texto(mensagem):

    while True:

        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Campo obrigatório.")

def pedir_confirmacao(mensagem):
    while True:
        opcao = input(f"{mensagem} (S/N): ").strip().upper()

        if opcao in ("S", "N"):
            return opcao == "S"

        print("Opção inválida.")

def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9

def pedir_nif_valido():

    while True:

        nif = pedir_texto("NIF: ")

        if validar_nif(nif):
            return nif

        print("NIF inválido.")