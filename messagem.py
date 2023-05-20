from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
class MyPopup(MDDialog):
    def __init__(self,confirma3=None,MEnsagem=None ,**kwargs):
        self.confirma3 = confirma3
        super(MyPopup, self).__init__(
            title=f"{MEnsagem}",
            text="Deseja continuar?",
            buttons=[
                MDFlatButton(text="Sim",on_release=self.confirma),
                MDFlatButton(text="Não",on_release=self.cancelar)
            ],
            **kwargs
        )

    def atualizar_dados(self, data):
        dialog = MDDialog(
            title="Sistema Sic",
            text=f"{data}",
            
        )
        dialog.open()  

    def confirma(self,*args):
        self.dismiss()
        self.confirma3()
    def cancelar(self,*args):
        self.dismiss()
    