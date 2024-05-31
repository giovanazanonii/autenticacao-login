import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="login"
    )
    return conexao