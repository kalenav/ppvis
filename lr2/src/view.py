ENTRY_LABEL_COUNT = 6
WHITE = (1, 1, 1, 1)
BLACK = (0, 0, 0, 1)
SINGLE_PAGE_MAX_ENTRY_COUNT = 10
BOTTOM_PADDING = 50

from tkinter.font import BOLD
from typing import Text
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
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
        self.add_widget(MainActionBar())
        self.add_widget(Table([]))
    
    def display_table(self, students):
        self.remove_widget(self.children[0])
        self.add_widget(Table(students))


class FileChooserView(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(FileChooserIconView())
        self.add_widget(FileChooserActionBar())


class NewEntryView(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(NewEntryPromptBlock())
        self.add_widget(AddEntryActionBar())


class FilterView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(NewEntryPromptBlock())
        self.add_widget(FilterActionBar())


class DeleteView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(NewEntryPromptBlock())
        self.add_widget(DeleteActionBar())


class AppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainView(name='main'))
        self.add_widget(FileChooserView(name='file_choose'))
        self.add_widget(NewEntryView(name='new_entry'))
        self.add_widget(FilterView(name='filter'))
        self.add_widget(DeleteView(name='delete'))
        


class Table(StackLayout):

    def __init__(self, students, **kwargs):
        super().__init__(**kwargs)  
        self.orientation = 'tb-lr'
        self.padding = [0, 0, 0, BOTTOM_PADDING]
        for student in students:
            self.add_widget(Entry(student))


class Entry(BoxLayout):

    def __init__(self, student, **kwargs):
        super().__init__(**kwargs)  
        self.orientation = 'horizontal'
        self.size_hint_y = 1 / SINGLE_PAGE_MAX_ENTRY_COUNT
        ENTRY_WIDTH = self.width / ENTRY_LABEL_COUNT
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.name}'))
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.course}'))
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.group}'))
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.completed}'))
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.overall}'))
        self.add_widget(EntryLabel(ENTRY_WIDTH, text=f'{student.lang}'))


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


class AddEntryActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FilterActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
class DeleteActionBar(ActionBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NewEntryPromptBlock(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = [0, 0, 0, BOTTOM_PADDING]
        self.rows = ENTRY_LABEL_COUNT
        self.cols = 2

        self.add_widget(NewEntryPromptLabel(text='Student name: '))
        self.name = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(NewEntryPromptLabel(text='Course: '))
        self.course = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.course)

        self.add_widget(NewEntryPromptLabel(text='Group: '))
        self.group = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.group)

        self.add_widget(NewEntryPromptLabel(text='Completed: '))
        self.completed = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.completed)

        self.add_widget(NewEntryPromptLabel(text='Overall: '))
        self.overall = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.overall)

        self.add_widget(NewEntryPromptLabel(text='Programming language: '))
        self.lang = NewEntryPromptTextInput(multiline=False)
        self.add_widget(self.lang)


class NewEntryPromptLabel(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 20
        self.color = BLACK

class NewEntryPromptTextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 20