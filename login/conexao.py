import mysql.connector as conn


#conexão com o banco de dados

def conectar():
    return conn.connect(
    host="localhost",
    user="bucefalo",
    password="123456",
    database="sistema_login";
)
