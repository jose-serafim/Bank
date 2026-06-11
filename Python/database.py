import sqlite3
from security import hash_password

def conectar():
    conn = sqlite3.connect("banco.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = conectar()
    cursor = conn.cursor()
    criar_tabela_clientes(cursor)
    criar_tabela_utilizadores(cursor)
    conn.commit()
    conn.close()

def criar_tabela_clientes(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nif TEXT UNIQUE NOT NULL,
            morada TEXT,
            email TEXT,
            telefone TEXT
        )
    """)
    

def criar_tabela_utilizadores(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL,

            FOREIGN KEY (cliente_id)
                REFERENCES clientes(id)
                ON DELETE CASCADE
        )
    """)


def criar_admin_default():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM utilizadores WHERE username = ?
    """, ("admin",))

    admin = cursor.fetchone()

    if not admin:
        cursor.execute("""
            INSERT INTO utilizadores (username, password_hash, role)
            VALUES (?, ?, ?)
        """, (
            "admin",
            hash_password("admin"),
            "admin"
        ))

        conn.commit()

    conn.close()