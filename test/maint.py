import platform
from kivymd.app import MDApp
from android.permissions import Permission, request_permissions


class MyApp(MDApp):
    def on_start(self):
        if platform.system() == "Android":
            permissions = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
            request_permissions(permissions, self.on_permissions_granted)
        else:
            # Código a ser executado para outras plataformas
            pass

    def on_permissions_granted(self, permissions, grant_results):
        if all(grant_results):
            # Permissões concedidas, mostrar o gerenciador de arquivos
            self.file_manager.show(os.path.expanduser("~"))
        else:
            # Permissões negadas
            pass

    def build(self):
        # Código para criar a interface do aplicativo
        pass


if __name__ == "__main__":
    MyApp().run()
