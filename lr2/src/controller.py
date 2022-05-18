from kivy.app import App
from view import AppScreenManager
from storage import InMemoryStorage, XMLStorage

class Controller(App):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.storage = InMemoryStorage([])
        self.screen_manager = AppScreenManager()

    def build(self):
        return self.screen_manager

    def add_entry(self, student):
        pass

    def find_entry(self, params_obj):
        pass

    def delete_entry(self, params_obj):
        pass

    def load(self, filename):
        data = XMLStorage(filename[0]).load()
        self.storage.save(data)
        self.screen_manager.current_screen.display_table(self.storage.load()[:10])