from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDIconButton


class TelaVenda(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Título da tela
        title_label = MDLabel(text='Tela de Vendas', halign='center', theme_text_color='Secondary')
        self.add_widget(title_label)

        # Conteúdo da tela
        content_box = BoxLayout(orientation='vertical')
        self.add_widget(content_box)

        # Lista de vendas
        self.vendas_list = MDList()
        content_box.add_widget(self.vendas_list)

        # Botão de adicionar venda
        add_button = MDFlatButton(text='Adicionar Venda', on_release=self.adicionar_venda)
        content_box.add_widget(add_button)

    def adicionar_venda(self, instance):
        # Função chamada quando o botão de adicionar venda é pressionado
        venda_item = BoxLayout(orientation='horizontal', size_hint_y=None, height=48)

        item_label = OneLineListItem(text='Nova Venda')
        delete_button = MDIconButton(icon='trash-can-outline', on_release=self.remover_venda)
        venda_item.add_widget(item_label)
        venda_item.add_widget(delete_button)
        self.vendas_list.add_widget(venda_item)

    def remover_venda(self, instance):
        # Função chamada quando o botão de exclusão de venda é pressionado
        venda_item = instance.parent
        self.vendas_list.remove_widget(venda_item)


class MyApp(MDApp):
    def build(self):
        return TelaVenda()


if __name__ == '__main__':
    MyApp().run()
