import os

from kivy.core.window import Window

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen,ScreenManager
class Fotos(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        #self.manager_open = False
        self.file_manager = MDFileManager(
            preview=True,
          exit_manager=self.exit_manager, select_path=self.select_path  
        )

        #exit_manager=self.exit_manager, select_path=self.select_path
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        #self.manager_open = True

    def select_path(self, path: str):
        
        print(path)
        self.exit_manager()
        toast(path)
        self.manager.current = 'Produto'
        self.manager.transition.direction="left"
        self.manager.get_screen('Produto').fotoSelecionada(path)
    def menuInicial(self):
        self.manager.current = 'Produto'
        self.manager.transition.direction="left" 
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

