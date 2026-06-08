import sqlite3
import hashlib

def conectar():
    return sqlite3.connect("banco.db")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def criar_admin_default():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM utilizadores WHERE username = ?
    """, ("admin",))

    admin = cursor.fetchone()

    if not admin:
        cursor.execute("""
            INSERT INTO utilizadores (username, password_hash, tipo)
            VALUES (?, ?, ?)
        """, (
            "admin",
            hash_password("admin"),
            "admin"
        ))

        conn.commit()

    conn.close()