from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import TwoLineListItem, MDList
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import subprocess
#import query
from kivymd.uix.dialog import MDDialog
from query import*
from messagem import*
import socket
import re
 
class JanelnaGerenciado(ScreenManager):
    pass
class Config(Screen):
    pass

    def verificaip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.ids.ip.text=ip_address
        for i in range(101):
            self.ids.progress_bar.value = i
        self.manager.current = 'login'
        self.manager.transition.direction="left"
    def menu(self):
        popup = MyPopup()
        popup.atualizar_dados(data="Olá, mundo!")
class Login(Screen):#logar sistema3
        
    def on_pre_enter(self):
        pass
    def logar(self):
     
        login=str(self.ids.login.text).lower().strip()
        senha=str(self.ids.senha.text).lower().strip()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM usuario where name='{login}' and senha='{senha}' ")
        resultado = cursor.fetchall()
        if resultado:
            data = {'nome': 'willow', 'idade': 28}
            self.manager.current = 'Produto'
            self.manager.get_screen('Produto').atualizar_dados(data)
            self.manager.transition.direction="left"
      
            
        else:
            self.menu("usuario incorreto \n ou \n senha")
        self.ids.login.text='' 
        self.ids.senha.text='' 
    def set_focus(self, next_field):
        next_field.focus = True    
    def menu(self,text):
        popup = MyPopup()
        popup.atualizar_dados(data=text)
       

class ListaPRoduto(Screen):
        def __init__(self, **kwargs):
            super(ListaPRoduto, self).__init__(**kwargs)
                        
        def buscaProduto(self):
            busca=str(self.ids.buscarPRoduto.text).upper()
         
            items=db.select(f"SELECT * FROM estoque WHERE descricao LIKE '%{busca}%' ")            
            if not items:
                pass
            else:
                self.ids.list_view.clear_widgets()
                for item in items:
                    #TwoLineListItem
                    list_item = TwoLineListItem(text=f'{item[1]}', secondary_text=f'{item[2]}')
                    #list_item = OneLineListItem(text=item[2])
                    self.ids.list_view.add_widget(list_item)
                
                list_item.bind(on_release=self.selecionaitem)
        def selecionaitem(self,instance):
            
            def edita():
                print(instance.text)
                self.ids.btm_tab.switch_tab('cadastro')
            popup = MyPopup(edita)
            popup.open()
     

        def update_database(self):
            self.ids.list_view.selection = [0].text
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
            self.manager.current = 'login'
            self.manager.transition.direction="right"#colcoa direçao
        def adicionarProduto(self):
            codigo=str(self.ids.codigoproduto.text).strip().upper()
            descricao=str(self.ids.descricaoproduto.text).strip().upper()
            quant=self.ids.quant.text
            vlcusto=self.ids.vlcusto.text
            vlvendas=self.ids.vlvendas.text
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            while True:
                if codigo=='':
                    self.ids.codigoproduto.focus = True
                    self.open_popup("Campo codigo em branco")
                    break
                if descricao=='':
                    self.ids.descricaoproduto.focus = True
                    self.open_popup("Campo descricao em branco")
                    break
                if quant=='':
                    self.ids.quant.focus = True
                    self.open_popup("Campo quantida em branco")
                    break
                if vlcusto=='':
                    self.ids.vlcusto.focus = True
                    self.open_popup("Campo valor custo em branco")
                    break
                if vlvendas=='':
                    
                    self.ids.vlvendas.focus = True
                    self.open_popup("Campo valor venda em branco")
                    break
                
                else:
                   
                    resultado=db.select(f'''SELECT * FROM estoque where codigo='{codigo}' ''')

                    if resultado:
                        self.open_popup("produto ja exite")#chama funçao
                    else:
                        db.adicionar(f'''INSERT INTO estoque (codigo,descricao,quant,vl_custo,vl_venda) 
                                    VALUES ('{codigo}','{descricao}','{quant}','{vlcusto}','{vlvendas}')''')
                        self.open_popup("Produto Cadastro com sucesso")
                    self.ids.codigoproduto.text =""
                    self.ids.descricaoproduto.text=""
                    self.ids.quant.text=""
                    self.ids.vlcusto.text=""
                    self.ids.vlvendas.text=""
                
                break
      
        def open_popup(self,text):#popus erro sistema
            popup = MyPopup()
            popup.atualizar_dados(data=text)
       
class vendas(MDApp):
    def build(self):
        DEBUG=1
        Window.size = (400, 600)
        db.criaTabela()
            
        return Builder.load_file('main.kv')
    
if __name__ == '__main__':
    vendas().run()
