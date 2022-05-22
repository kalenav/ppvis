from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("custom_widgets.kv")
Window.clearcolor = (1, 1, 1, 1)


class MainScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name='main'))


class MainScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(MainActionBar())


class MainActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)