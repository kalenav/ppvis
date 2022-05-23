from UIclass import UI
from file_reader import FileReader
from file_writer import FileWriter
from kivy.app import App
from view import AppScreenManager


class Controller(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = AppScreenManager()
        self.ui = UI()
        self.train_action = 'none'
        self.saving = False

    def build(self):
        return self.screen_manager

    def clear_screen(self):
        self.screen_manager = AppScreenManager()

    def show_playarea_state(self):
        if self.playarea == None:
            pass
        PLAYAREA_DICT = {
            'trains': list(map(lambda train: {
                'speed': train.getSpeed(),
                'service': train.getServiceTimeLeft(),
                'carriages': list(map(lambda carriage: {
                    'is_cargo': carriage.isCargo(),
                    'is_loaded': carriage.isLoaded(),
                }, train.getCarriages())),
                'path': list(map(lambda station: station.getId(), train.getPath()))
            }, self.playarea.getTrains())),
            'stations': self.playarea.getStations(),
        }
        self.screen_manager.current_screen.display_playarea_state(PLAYAREA_DICT)

    def show_train_info(self, index):
        if self.playarea == None:
            pass

    def send_train(self, index):
        if self.playarea == None:
            pass
        RESULT = self.ui.send_train(self.playarea, index)
        if RESULT == 'en route':
            print('en route')
        if RESULT == 'overloaded':
            print('overloaded')
        if RESULT == 'ok':
            print('ok')

    def load_train(self, index):
        if self.playarea == None:
            pass
        RESULT = self.ui.load_train(self.playarea, index)
        if RESULT == 'en route':
            pass
        if RESULT == 'ok':
            pass

    def unload_train(self, index):
        if self.playarea == None:
            pass
        RESULT = self.ui.unload_train(self.playarea, index)
        if RESULT == 'en route':
            pass
        if RESULT == 'ok':
            pass

    def next_turn(self):
        if self.playarea == None:
            pass
        self.ui.next_turn()

    def load(self, filename):
        self.playarea = FileReader(filename).readPlayareaFromFile()

    def save(self, filename):
        if self.playarea == None:
            pass
        FileWriter(filename, self.playarea).writePlayareaToFile()

