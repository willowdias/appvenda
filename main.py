from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import TwoLineListItem, MDList
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRaisedButton

from kivy.properties import*
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.image import Image
from kivy.config import ConfigParser
import os,sys
from kivymd.uix.button import MDFlatButton, MDIconButton
#import query
from kivymd.uix.dialog import MDDialog
from query import*
from messagem import*
from fotoaquivo import*
from bd import*
from kivy import platform
from kivy.utils import platform

from kivy import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, 
Permission.READ_EXTERNAL_STORAGE])
class JanelnaGerenciado(ScreenManager):
    pass

class Config(Screen):
    pass

    def verificaip(self):
      
        ip=self.ids.ip.text
        banco=bancomysql(ip)
        '''if ip=="":
            self.menu("ip Invalido")
        elif banco.verifica()==False:
            self.menu(f"{ip} ip Invalido")
        else:
            self.menu(f"{ip} ip valido")
            for i in range(101):
                self.ids.progress_bar.value = i'''
        self.manager.current = 'login'
        self.manager.transition.direction="left"
    def menu(self,mesagem):
        popup = MyPopup()
        popup.atualizar_dados(data=mesagem)
class Login(Screen):#logar sistema3
        
    def on_pre_enter(self):
        pass
    def logar(self):
        data = {'nome': f'WW', 'idade': 28}
        self.manager.current = 'Produto'
        self.manager.get_screen('Produto').atualizar_dados(data)
        self.manager.transition.direction="left"
        '''login=str(self.ids.login.text).lower().strip()
        senha=str(self.ids.senha.text).lower().strip()
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM usuario where name='{login}' and senha='{senha}' ")
        resultado = cursor.fetchall()
        if resultado:
            data = {'nome': f'{login}', 'idade': 28}
            self.manager.current = 'Produto'
            self.manager.get_screen('Produto').atualizar_dados(data)
            self.manager.transition.direction="left"
      
            
        else:
            self.menu("usuario incorreto \n ou \n senha")
        self.ids.login.text='' 
        self.ids.senha.text='' '''
    def set_focus(self, next_field):
        next_field.focus = True    
    def menu(self,text):
        popup = MyPopup()
        popup.atualizar_dados(data=text)
       

class ListaPRoduto(Screen):
        def __init__(self, **kwargs):
            super(ListaPRoduto, self).__init__(**kwargs)
            self.items=[] 
              
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
        def fotoSelecionada(self,data):
            self.ids.imagCliente.source=data
        def SelecionaFotos(self):
            self.manager.current = 'PastaFoto'
            self.manager.transition.direction="left"
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
        def carregardados(self):
            db.exporta()
            
           
        def open_popup(self,text):#popus erro sistema
            popup = MyPopup()
            popup.atualizar_dados(data=text)
            
        def adicionaprodutos(self):
            venda_items = BoxLayout(orientation='horizontal', size_hint_y=None, height=48,spacing=10)
            busca=str(self.ids.addprodutos.text).upper()
            

            items=db.select(f"SELECT * FROM estoque WHERE descricao LIKE '%{busca}%' ")
            if busca=='':
                pass
            
            else:
                for item in items: 
                    item_label= TwoLineListItem(text=f'Codigo {item[1]}', secondary_text=f'Descricao {item[2]}',tertiary_text=f'Total R$ {"R$ {:.2f}".format(float(item[4]))}')
                    

            try:
                self.items.append({"valor":item[4]})
                imagens=Image(source='venda.png',size_hint_x=0.3)
                idlb=MDFloatingActionButton(icon='pencil')
                delete_button = MDFloatingActionButton(icon=f'trash-can-outline',on_release=self.remover_venda)
                delete_button.item_text = item_label.text
                
                    
                venda_items.add_widget(imagens)
                
                venda_items.add_widget(item_label)
                venda_items.add_widget(idlb)
                venda_items.add_widget(delete_button)
                self.ids.venda_produto.add_widget(venda_items)
                #item_label.bind(on_release=self.remover_venda)
            except: errorcode  
            self.cacularitens()
       
        def remover_venda(self, instance):
            item_text = instance.item_text
            print(item_text)
            def removeiten():
                self.ids.venda_produto.remove_widget(instance.parent)
                self.cacularitens()
            popup = MyPopup(removeiten,'DESEJA APAGAR ITEM VENDA')#essa funçao returna confirmaçoa baixa iten class
            popup.open()
        def cacularitens(self):
            total = 0
            for item in self.items:
                total += item["valor"]
            self.ids.VAlortotalvenda.text=f'Total R$ {"R$ {:.2f}".format(total)}'
            
            item_count = len(self.ids.venda_produto.children)
            self.ids.quantidaITens.text=f"Quantidade {item_count-1}"     
        #foca objeto
        def set_focus(self, next_field):
            next_field.focus = True    
class vendas(MDApp):
    def build(self):
        DEBUG=1
        Window.size = (400, 600) 
        
        db.criaTabela()
        
        return Builder.load_file('main.kv')
    
 
if __name__ == '__main__':
    vendas().run()
