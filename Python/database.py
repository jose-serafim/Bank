#database.py

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

def username_existe(username):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM utilizadores WHERE username = ?
    """, (username,))

    result = cursor.fetchone()
    conn.close()

    return result is not None

def nif_existe(nif):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM clientes
        WHERE nif = ?
    """, (nif,))

    result = cursor.fetchone()

    conn.close()

    return result is not None

def criar_cliente_db(cliente):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO clientes (
            nome,
            nif,
            morada,
            email,
            telefone
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            cliente["nome"],
            cliente["nif"],
            cliente["morada"],
            cliente["email"],
            cliente["telefone"]
        )
    )

    cliente_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO utilizadores (
            cliente_id,
            username,
            password_hash,
            role
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            cliente_id,
            cliente["username"],
            hash_password(cliente["password"]),
            "cliente"
        )
    )

    conn.commit()
    conn.close()

def remover_cliente_db(cliente_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
    """, (cliente_id,))

    conn.commit()
    conn.close()

def atualizar_cliente_db(cliente):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE clientes
        SET
            nome = ?,
            morada = ?,
            email = ?,
            telefone = ?
        WHERE id = ?
    """, (
        cliente["nome"],
        cliente["morada"],
        cliente["email"],
        cliente["telefone"],
        cliente["id"]
    ))

    conn.commit()
    conn.close()

def obter_todos_clientes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.id,
            c.nome,
            c.nif,
            u.username
        FROM clientes c
        JOIN utilizadores u
            ON u.cliente_id = c.id
        ORDER BY c.nome
    """)

    clientes = cursor.fetchall()

    conn.close()

    return clientes

def obter_cliente_por_nif(nif):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.id,
            c.nome,
            c.nif,
            c.morada,
            c.email,
            c.telefone,
            u.username
        FROM clientes c
        JOIN utilizadores u
            ON u.cliente_id = c.id
        WHERE c.nif = ?
    """, (nif,))

    cliente = cursor.fetchone()

    conn.close()

    return cliente