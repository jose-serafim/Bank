from database import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(utilizadores)")

for coluna in cursor.fetchall():
    print(coluna)

conn.close()
