from getpass import getpass
 
def login():

    username = input("Utilizador: ")
    password = getpass("Password: ")

    if username == "admin" and password == "admin":
        return True
    else:
        return False