import mysql.connector
from mysql.connector import errorcode
class bancomysql:
    def __init__(self,ip=None):
        self.mydb = mysql.connector.connect(
        host=f"{ip}",
        user="root",
        password="",
        database="app",
        port='3306'
        )
        self.conn=self.mydb.cursor()
        
        self.creattabela()
    def select(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"{query} " )
        result = mycursor.fetchall()
        return result
    def insert(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"{query} " )
        
        return self.mydb.commit()
    def creattabela(self):
        mycursor = self.mydb.cursor()
        estoque = '''
        CREATE TABLE IF NOT EXISTS estoque 
        (id INTEGER PRIMARY KEY, codigo varchar(200),
        descricao varchar(200),quant int, vl_custo NUMERIC,vl_venda NUMERIC);
        '''
        mycursor.execute(estoque)
        usuario = '''
        CREATE TABLE IF NOT EXISTS 
        usuario (id INTEGER PRIMARY KEY, name varchar(200),senha varchar(200));
        '''
        mycursor.execute(usuario)
        return self.mydb.commit()
     
'''
banco=bancomysql()
lista=["INSERT INTO usuario(id,name,senha)VALUES (1, 'willow', 123)","INSERT INTO app.usuario(id,name,senha)VALUES (2, 'elias', '123');"]
for i in lista:
    banco.insert(i)'''