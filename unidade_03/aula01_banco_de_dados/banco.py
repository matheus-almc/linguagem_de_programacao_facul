import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
create_table_sql = '''
CREATE TABLE IF NOT EXISTS Produtos (
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
preco REAL NOT NULL,
estoque INTEGER
);
'''
# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table_sql)

# 5. Confirmar as alterações (commit)

conn.commit()

# 6. Fechar a conexão com o banco de dados

conn.close()

import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

novo_produto = ('Camiseta', 19.99, 500)

inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

cursor.execute(inserir_produto, novo_produto)

conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"

cursor.execute(selecionar_produtos)

produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

    conn.close()

    import sqlite3

    conn = sqlite3.connect('exemplo.db')

    cursor = conn.cursor()

    novo_preco = 24.99

    produto_id = 1

    atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

    cursor.execute(atualizar_preco, (novo_preco, produto_id))

    conn.commit()

    conn.close()

    import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

produto_id = 2

excluir_produto = "DELETE FROM Produtos WHERE id = ?"

cursor.execute(excluir_produto, (produto_id,))

conn.commit()

conn.close()