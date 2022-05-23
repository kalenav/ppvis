from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("custom_widgets.kv")
Window.clearcolor = (1, 1, 1, 1)

BLACK = (0, 0, 0, 1)

class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset()

    def reset(self):
        self.clear_widgets()
        self.add_widget(MainScreen(name='main'))
        self.add_widget(TrainChooseScreen(name='choose'))
        self.add_widget(FileChooserScreen(name='file'))


class MainScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(MainActionBar())

    def display_playarea_state(self, playarea_dict):
        self.add_widget(PlayareaInfoLayout(playarea_dict))


class TrainChooseScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(TrainChooseActionBar())
        self.add_widget(TrainChooseLayout())


class FileChooserScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(FileChooserActionBar())
        self.add_widget(FileChooserIconView())


class MainActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TrainChooseActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FileChooserActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TrainChooseLayout(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PlayareaInfoLayout(BoxLayout):

    def __init__(self, playarea_dict, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TrainsInfoLayout(playarea_dict['trains']))
        self.add_widget(StationsInfoLayout(playarea_dict['stations']))


class TrainsInfoLayout(StackLayout):

    def __init__(self, trains, **kwargs):
        super().__init__(**kwargs)
        for train in trains:
            self.add_widget(TrainInfoLayout(train))


class TrainInfoLayout(BoxLayout):

    def __init__(self, train_dict, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BlackTextLabel(text=f'Current speed: {train_dict["speed"]}'))
        self.add_widget(BlackTextLabel(text=f'Service time left: {train_dict["service"]}'))
        CARRIAGES = train_dict['carriages']
        self.add_widget(BlackTextLabel(text=f'{len(CARRIAGES)} carriage(s)'))
        for index in range(len(CARRIAGES)):
            CARRIAGE = CARRIAGES[index]
            self.add_widget(BlackTextLabel(text=f'Carriage {index}: {"cargo" if CARRIAGE["is_cargo"] else "passenger"}, {"loaded" if CARRIAGE["is_loaded"] else "unloaded"}'))
        path_str = ''
        for station_id in train_dict['path']:
            path_str += f'{station_id} '
        self.add_widget(BlackTextLabel(text=f'Path: {path_str}'))


class StationsInfoLayout(StackLayout):

    def __init__(self, stations, **kwargs):
        super().__init__(**kwargs)
        for station in stations:
            self.add_widget(StationInfoLayout(station))


class StationInfoLayout(BoxLayout):

    def __init__(self, station, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BlackTextLabel(text=f'Id: {station["id"]}'))
        adjacent_text = "Adjacent: "
        for index in range(len(station['adjacent'])):
            adjacent_text += f'{station["adjacent"][index]}({station["weights"][index]})'
            if index < len(station['adjacent']) - 1:
                adjacent_text += ','
            adjacent_text += ' '
        self.add_widget(BlackTextLabel(text=adjacent_text))


class BlackTextLabel(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = BLACK
        