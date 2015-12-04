
import sqlite3

conn = sqlite3.connect('mega.db')
cursor = conn.cursor()

with open('mega.txt') as arquivo:
	for linha in arquivo:
		a,b,c,d,e,f = (linha.strip('').strip(','))
		print(a,b,c,d,e,f)

# inserindo dados na tabela
cursor.execute("""
INSERT INTO dezenas (dezena1, dezena2, dezena3, dezena4, dezena5, dezena6)
VALUES (a,b,c,d,e,f)
""")
