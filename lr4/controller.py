from UIclass import UI
from file_reader import FileReader
from file_writer import FileWriter
from kivy.app import App
from view import MainScreenManager


class Controller(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = MainScreenManager()
        self.ui = UI()

    def build(self):
        return self.screen_manager

    def show_playarea_state(self):
        pass

    def show_train_info(self, index):
        pass

    def load_train(self, index):
        UI.loadTrain(self.playarea, index)

    def unload_train(self, index):
        UI.unloadTrain(self.playarea, index)

    def next_turn(self):
        pass

    def load(self, filename):
        self.playarea = FileReader(filename).readPlayareaFromFile()

    def save(self, filename):
        FileWriter(filename, self.playarea).writePlayareaToFile()

