import streamlit as st 
import mysql.connector as sql

conexao = mysql.connector.connect(
    host="localhost",
    user="",
    password="123456",
    database="login_db";
)

if conexao.is_connected():
    st.suceces("banco de dados conectado com sucesso!")
    else:
        st.error("banco de dados não esta conectado")
conexao.close()