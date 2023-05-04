from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import TwoLineListItem, MDList
from kivy.uix.popup import Popup
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.button import MDRectangleFlatButton
import os
import sqlite3
import time
class JanelnaGerenciado(ScreenManager):
    pass
class Janelaprincipal(Screen):
    
    def logar(self):
        data = {'nome': 'willow', 'idade': 28}
        self.manager.current = 'janela1'
        self.manager.get_screen('janela1').atualizar_dados(data)
        self.manager.transition.direction="left"
        '''    
        login=str(self.ids.login.text).lower().strip()
        senha=str(self.ids.senha.text).lower().strip()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM usuario where name='{login}' and senha='{senha}' ')
        resultado = cursor.fetchall()
        if resultado:
            data = {'nome': 'willow', 'idade': 28}
            self.manager.current = 'janela1'
            self.manager.get_screen('janela1').atualizar_dados(data)
            self.manager.transition.direction="left"
      
            
        else:
            self.open_popup("usuario incorreto \n ou \n senha")
        self.ids.login.text='' 
        self.ids.senha.text='' '''
    
    def open_popup(self,text):
        popup = Popup(title=f'{text}'.upper(),
                      size_hint=(None, None), size=(300, 400))
        popup.open()       
class Janela1(Screen):
    def __init__(self, **kwargs):
        super(Janela1, self).__init__(**kwargs)
    def valquant(self):#essa funçaomuda numero inteiro pra float
        quant=self.ids.quant.text
        self.ids.quant.text="{:.2f}".format(float(quant))
    def valcusto(self):
        vlcusto=self.ids.vlcusto.text
        self.ids.vlcusto.text="R$ {:.2f}".format(float(vlcusto))
    def valvenda(self):
        vlvendas=self.ids.vlvendas.text
        self.ids.vlvendas.text="R$ {:.2f}".format(float(vlvendas))
    def atualizar_dados(self, data):
        self.ids.label.text=f'Nome: {data["nome"]}, Idade: {data["idade"]}'
    def voltatelaprincinpal(self):
        self.manager.current = 'janelaprincipal'
        self.manager.transition.direction="right"#colcoa direçao
    def adicionarProduto(self):
        codigo=str(self.ids.codigoproduto.text).strip().upper()
        descricao=str(self.ids.descricaoproduto.text).strip().upper()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        if codigo=='' or descricao=='':
            self.open_popup("campo branco")
        else:
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            cursor.execute(f'''SELECT * FROM estoque where codigo='{codigo}' ''')
            resultado = cursor.fetchall()
            if resultado:
                self.open_popup("produto ja exite")#chama funçao
            else:
                cursor.execute(f'''INSERT INTO estoque (codigo,descricao) VALUES ('{codigo}','{descricao}')''')
                conn.commit()
                self.open_popup("Produto Cadastro com sucesso")
            self.ids.codigoproduto.text =""
            self.ids.descricaoproduto.text=""
    def open_popup(self,text):#popus erro sistema
        popup = Popup(title=f'{text}'.upper(),
                      size_hint=(None, None), size=(300, 400))
        popup.open()    
    def verprodutos(self):
        self.manager.current = 'Produto'#chama tela lateral
        self.manager.transition.direction="left"#colcoa direçao
class ListaPRoduto(Screen):
        #def on_pre_enter(self):
            
        def buscaProduto(self):
            busca=str(self.ids.buscarPRoduto.text).upper()
            self.ids.list_view.clear_widgets()
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estoque WHERE descricao LIKE ?", ('%' + busca + '%',))
            items = cursor.fetchall()
        
            if not items:
                self.ids.list_view.clear_widgets()
            else:
                self.ids.list_view.clear_widgets()
                for item in items:
                    list_item = TwoLineListItem(text=item[1], secondary_text=item[2])
                    self.ids.list_view.add_widget(list_item)
                conn.close()
        def voltatelaprincinpal(self):
            self.manager.current = 'janela1'
            self.manager.transition.direction="right"#colcoa direçao

class vendas(MDApp):
    def build(self):
        DEBUG=1
        #Window.size = (300, 600)
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS 
                    usuario (id INTEGER PRIMARY KEY, name varchar(200),senha varchar(200))''')
        cursor.execute(f'''SELECT * FROM usuario ''')
        login = cursor.fetchall()
        if not login:
            cursor.execute('''INSERT INTO usuario (name,senha) VALUES (?,?)''', ('willow','123'))
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS 
                    estoque (id INTEGER PRIMARY KEY, codigo varchar(200),descricao varchar(200))''')
        

        conn.commit()
        conn.close()
    
            
        return Builder.load_file('login.kv')

    
    
if __name__ == '__main__':
    vendas().run()
