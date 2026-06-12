from getpass import getpass
from database import conectar
from security import hash_password

def login():

    username = input("Utilizador: ")
    password = getpass("Password: ")

    password_hash = hash_password(password)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, role
        FROM utilizadores
        WHERE username = ? AND password_hash = ?
    """, (username, password_hash))

    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "id": user[0],
            "username": user[1],
            "role": user[2]
        }

    return None