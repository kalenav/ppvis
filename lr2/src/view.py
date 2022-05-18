ENTRY_LABEL_COUNT = 6
WHITE = (1, 1, 1, 1)
BLACK = (0, 0, 0, 1)
SINGLE_PAGE_MAX_ENTRY_COUNT = 10

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionBar
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from kivy.lang import Builder
from model import Student

Builder.load_file("custom_widgets.kv")
Window.clearcolor = WHITE

class MainView(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Table([]))
        self.add_widget(MainActionBar())
    
    def display_table(self, students):
        self.remove_widget(self.children[1])
        self.add_widget(Table(students))


class FileChooserView(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(FileChooserIconView())
        self.add_widget(FileChooserActionBar())


class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainView(name='main'))
        self.add_widget(FileChooserView(name='file_choose'))
        


class Table(StackLayout):

    def __init__(self, students, **kwargs):
        super().__init__(**kwargs)  
        self.orientation = 'tb-lr'
        for student in students:
            self.add_widget(Entry(student))


class Entry(BoxLayout):

    def __init__(self, student, **kwargs):
        super().__init__(**kwargs)  
        self.orientation = 'horizontal'
        self.size_hint_y = 1 / SINGLE_PAGE_MAX_ENTRY_COUNT
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.name}'))
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.course}'))
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.group}'))
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.completed}'))
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.overall}'))
        self.add_widget(EntryLabel(self.width / ENTRY_LABEL_COUNT, text=f'{student.lang}'))


class EntryLabel(Label):

    def __init__(self, width, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.color = BLACK

class MainActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FileChooserActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
