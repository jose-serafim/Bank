#contas.py
from database import (
    criar_conta_db,
    obter_todas_contas,
    obter_conta_por_nif,
    obter_cliente_por_nif
)
import utils

def criar_conta(user):

    utils.limpar_ecra()

    print("=================================")
    print("         NOVA CONTA")
    print("=================================\n")

    nif = utils.pedir_nif_valido()

    cliente = obter_cliente_por_nif(nif)

    if not cliente:
        print("\nCliente não encontrado.")
        input("\nPrima Enter para voltar...")
        return

    while True:
        try:
            saldo = float(input("Saldo Inicial: "))

            if saldo < 0:
                print("O saldo não pode ser negativo.")
                continue

            break

        except ValueError:
            print("Valor inválido.")

    conta = {
        "cliente_id": cliente[0],
        "saldo": saldo
    }

    if utils.pedir_confirmacao("Confirmar criação da conta?"):
        try:
            criar_conta_db(conta)
            print("\nConta criada com sucesso!")
        except Exception as e:
            print(f"\nErro ao criar conta: {e}")
    else:
        print("\nCriação de conta cancelada.")

    input("\nPrima Enter para voltar ao menu...")
