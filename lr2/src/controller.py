from kivy.app import App
from view import AppScreenManager
from storage import InMemoryStorage, XMLStorage, XMLWriter
from model import Student

class Controller(App):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.storage = InMemoryStorage([])
        self.screen_manager = AppScreenManager()
        self.skipping = 0
        self.saving = False
        self.filter_config = {}

    def build(self):
        return self.screen_manager

    def add_entry(self, name, course, group, completed, overall, lang):
        data = self.storage.load()
        data.append(Student(name, int(course or 1), group, int(completed or 0), int(overall or 0), lang))
        self.storage.save(data)
        self.display_table(self.find_entries(None))

    def find_entries(self, params_obj):
        if params_obj != None:
            self.filter_config = params_obj
        data = self.storage.load()
        if 'name' in self.filter_config and self.filter_config['name'] != '':
            data = list(filter(lambda stud: self.filter_config['name'] in stud.name, data))
        if 'group' in self.filter_config and self.filter_config['group'] != '':
            data = list(filter(lambda stud: self.filter_config['group'] == stud.group, data))
        if 'course' in self.filter_config and self.filter_config['course'] != '':
            data = list(filter(lambda stud: int(self.filter_config['course']) == stud.course, data))
        if 'completed' in self.filter_config and self.filter_config['completed'] != '':
            data = list(filter(lambda stud: int(self.filter_config['completed']) == stud.completed, data))
        if 'overall' in self.filter_config and self.filter_config['overall'] != '':
            data = list(filter(lambda stud: int(self.filter_config['overall']) == stud.overall, data))
        return data

    def delete_entries(self, params_obj):
        pass

    def next(self):
        if(len(self.storage.load()) - self.skipping < 10):
            return
        self.skipping += 10
        self.display_table(self.find_entries(None))
    
    def previous(self):
        if(self.skipping - 10 < 0):
            return
        self.skipping -= 10
        self.display_table(self.find_entries(None))

    def load(self, filename):
        self.screen_manager.current_screen.display_table([])
        data = XMLStorage(filename[0]).load()
        self.storage.save(data)
        self.display_table(self.find_entries(None))

    def save(self, filename):
        XMLWriter(filename[0]).write(self.storage.load())
        self.saving = False

    def display_table(self, data):
        self.screen_manager.current_screen.display_table(data[(self.skipping):(self.skipping + 10)])

    def clear_filters(self):
        self.display_table(self.find_entries({}))