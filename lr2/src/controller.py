from kivy.app import App
from view import AppScreenManager
from storage import InMemoryStorage, XMLStorage
from model import Student

class Controller(App):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.storage = InMemoryStorage([])
        self.screen_manager = AppScreenManager()

    def build(self):
        return self.screen_manager

    def add_entry(self, name, course, group, completed, overall, lang):
        data = self.storage.load()
        data.append(Student(name, int(course), group, int(completed), int(overall), lang))
        self.storage.save(data)
        self.display_table()

    def find_entry(self, params_obj):
        pass

    def delete_entry(self, params_obj):
        pass

    def load(self, filename):
        self.screen_manager.current_screen.display_table([])
        data = XMLStorage(filename[0]).load()
        self.storage.save(data)
        self.display_table()

    def display_table(self):
        self.screen_manager.current_screen.display_table(self.storage.load()[:10])