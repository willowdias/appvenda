from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem

KV = '''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'My App'

        ScrollView:
            MDList:
                id: my_list

                OneLineListItem:
                    text: 'Item 1'
                    on_press: app.print_row(root, self)

                OneLineListItem:
                    text: 'Item 2'
                    on_press: app.print_row(root, self)

'''

class MainScreen(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

    def print_row(self, screen, list_item):
        row_text = list_item.text
        print(f"Selected row: {row_text}")

if __name__ == '__main__':
    TestApp().run()
