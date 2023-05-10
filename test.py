from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTextField:
        id: text_field1
        hint_text: "Digite seu nome"
        on_text_validate: app.set_focus(text_field2)

    MDTextField:
        id: text_field2
        hint_text: "Digite seu sobrenome"
        on_text_validate: app.set_focus(text_field3)

    MDTextField:
        id: text_field3
        hint_text: "Digite sua idade"
'''

class MyApp(MDApp):

    def build(self):
        self.root = Builder.load_string(KV)
        return self.root

    def set_focus(self, next_field):
        next_field.focus = True

MyApp().run()
