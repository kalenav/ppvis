from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("custom_widgets.kv")
Window.clearcolor = (1, 1, 1, 1)


class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name='main'))
        self.add_widget(TrainChooseScreen(name='choose'))
        self.add_widget(FileChooserScreen(name='file'))


class MainScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(MainActionBar())


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


class TrainsInfoLayout(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TrainInfoLayout(BoxLayout):

    def __init__(self, train, **kwargs):
        super().__init__(**kwargs)
        