import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
               {'nome': 'Joãozinho', 'peso': 45})

conexao.commit()

cursor.execute('SELECT * FROM clientes')
cursor.fetchall()

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)

cursor.close()
conexao.close()
