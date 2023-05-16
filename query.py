
import sqlite3
import io  
import json
import os
class sqlite_db:
    def __init__(self,banco=None):
        self.conn =None
        self.curso = None
        
        if banco:
            self.open(banco)
        self.criaTabela()
    def open(self,banco):#essa funçao configura banco pra recebe inforçao
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            
        except:
           print("banco Off")     
    def adicionar(self,query):#adicionar item
        cur = self.cursor
        cur.execute(query)
        return self.conn.commit() 
    def select(self,query): #selecionar item  
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
    def update(self,query):#upadte
        cur = self.cursor
        cur.execute(query)
        self.conn.commit() 
    def criaTabela(self):
        cur = self.cursor
        cur.execute('''CREATE TABLE IF NOT EXISTS 
                        usuario (id INTEGER PRIMARY KEY, name varchar(200),senha varchar(200))''')
        login=self.select(f'''SELECT * FROM usuario ''')
        if not login:
            self.adicionar('''INSERT INTO usuario (name,senha) VALUES ('willow','123')''')    
        cur.execute('''CREATE TABLE IF NOT EXISTS 
            estoque (id INTEGER PRIMARY KEY, codigo varchar(200),
            descricao varchar(200),quant int, vl_custo NUMERIC,vl_venda NUMERIC)''')

db=sqlite_db("app.db")
