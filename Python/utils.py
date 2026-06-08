import os

def limpar_ecra():
    os.system('clear' if os.name == 'posix' else 'cls')