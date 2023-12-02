import sqlite3

banco = sqlite3.connect('produtos.db')
'''
with banco:
    cursor = banco.cursor()
    
    cursor.execute("CREATE TABLE produto(ID integer primary key, NOME text, MODELO text, PRECO float, ANO text, COR text, FILIAL text, DATA_ENTRARDA text, DATA_SAIDA text)")
'''

def inserir_informacao(i):
    with banco: 
        cursor = banco.cursor()
        query = "INSERT INTO produto(ID, NOME, MODELO, PRECO, ANO, COR, FILIAL, DATA_ENTRARDA, DATA_SAIDA) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)
        

def mostar_informacao():
    lista = []
    with banco: 
        cursor = banco.cursor()
        query = "SELECT * FROM produto"
        cursor.execute(query)
        informacao = cursor.fetchall()
        
        for i in informacao:
            lista.append(i)
            
    return lista


def alterar_informacao(i):
    with banco:
        cursor =banco.cursor()
        query = "UPDATE produto SET  NOME=?, MODELO=?, PRECO=?, ANO=?, COR=?, FILIAL=?, DATA_ENTRARDA=?, DATA_SAIDA=? WHERE ID=?"
        cursor.execute(query, i)
        

def deletar_informacao(i):
    with banco:
        cursor = banco.cursor()
        query = "DELETE FROM produto WHERE ID=?"
        cursor.execute(query, i)