import sqlite3
import hashlib
from getpass import getpass
from database import conectar
 
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login():

    username = input("Utilizador: ")
    password = getpass("Password: ")

    password_hash = hash_password(password)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, tipo
        FROM utilizadores
        WHERE username = ? AND password_hash = ?
    """, (username, password_hash))

    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "id": user[0],
            "username": user[1],
            "tipo": user[2]
        }

    return None