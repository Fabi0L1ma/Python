import sqlite3

banco = sqlite3.connect('clientes.db')


with banco:
    cursor = banco.cursor()

    cursor.execute("CREATE TABLE cliente(codigo integer primary key, nome text, cpf text, data_nascimento text, sexo text, endereco text, cidade text, uf text, telefone text, email text)")

