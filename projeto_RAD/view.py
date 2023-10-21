import sqlite3

banco = sqlite3.connect('clientes.db')

# CRIAR

def inserir_informacao(i):   
    with banco:
        cursor = banco.cursor()
        query = "INSERT INTO cliente(codigo, nome, cpf, data_nascimento, sexo, endereco, cidade, uf, telefone, email) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query,i)
        

# VISUALIZAR

def mostrar_informacao():
    lista = []
    with banco:
        cursor = banco.cursor()
        query = "SELECT * FROM cliente"
        cursor.execute(query)
        informacao = cursor.fetchall()
        
        for i in informacao:
            lista.append(i)
            
    return lista
            
    

# ATUALIZAR 

def alterar_informacao(i):
    with banco:
        cursor = banco.cursor()
        query = "UPDATE cliente SET nome=?, cpf=?, data_nascimento=?, sexo=?, endereco=?, cidade=?, uf=?, telefone=?, email=? WHERE codigo=?"
        cursor.execute(query,i)
        
        
# DELETAR

def deletar_informacao(i):
    with banco:
        cursor = banco.cursor()
        query = "DELETE FROM cliente WHERE codigo=?"
        cursor.execute(query,i)
