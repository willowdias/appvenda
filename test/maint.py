from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.permissions import Permission
from kivy.utils import platform
# Load the kv file
Builder.load_string(
    """
<MainLayout>
    orientation: "vertical"

    MDToolbar:
        title: "MDFileManager Permission Example"

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: "48dp"

        MDRaisedButton:
            text: "Open FileManager"
            on_release: app.open_file_manager()
"""
)


class MainLayout(BoxLayout):
    pass


class PermissionApp(MDApp):
    file_manager = ObjectProperty()

    def build(self):
        return MainLayout()

    def open_file_manager(self):
        if Permission.WRITE_EXTERNAL_STORAGE in Permission.get_permissions():
            self.show_file_manager()
        else:
            Permission.request_permissions([Permission.WRITE_EXTERNAL_STORAGE], self.on_permission_result)

    def show_file_manager(self):
        self.file_manager = MDFileManager(exit_manager=self.exit_file_manager)
        self.file_manager.show()  # You can specify a path as an argument to show a specific directory

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def on_permission_result(self, permissions, grant_results):
        if all(grant_results):
            self.show_file_manager()
        else:
            toast("Storage permission denied!")


if __name__ == "__main__":
    PermissionApp().run()
