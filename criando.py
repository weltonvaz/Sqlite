# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('mega.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE dezenas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        dezena1 TEXT NOT NULL,
        dezena2 TEXT NOT NULL,
        dezena3 TEXT NOT NULL,
        dezena4 TEXT NOT NULL,
        dezena5 TEXT NOT NULL,
        dezena6 TEXT NOT NULL 
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
