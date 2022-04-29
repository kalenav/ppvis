from kivy.app import App
from kivy.lang.builder import Builder

def getEntriesKV(entries):
    result = ''
    for entry in entries:
        result += f'''
        BoxLayout:
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                color: 0, 0, 0, 1
                text: '{entry['petName']}'
                size_hint: (0.2, 1)
            Label:
                color: 0, 0, 0, 1
                text: '{entry['dob']['day']}.{entry['dob']['month']}.{entry['dob']['year']}'
                size_hint: (0.2, 1)
            Label:
                color: 0, 0, 0, 1
                text: '{entry['lastVisit']['day']}.{entry['lastVisit']['month']}.{entry['lastVisit']['year']}'
                size_hint: (0.2, 1)
            Label:
                color: 0, 0, 0, 1
                text: '{entry['vetName']}'
                size_hint: (0.2, 1)
            Label:
                color: 0, 0, 0, 1
                text: '{entry['diagnosis']}'
                size_hint: (0.2, 1)
'''
    return result

def makeMainWindowKVString(entries):
    KV = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1, 0.9)'''
    KV += getEntriesKV(entries)
    KV += '''
    BoxLayout:
        orientation: 'horizontal'
        size_hint: (1, 0.1)
        Button:
            text: 'Add entry'
            size_hint: (0.33, 1)
        Button:
            text: 'Search for entries'
            size_hint: (0.33, 1)
        Button:
            text: 'Delete entries'
            size_hint: (0.33, 1)'''
    return KV

class UI(App):
    def build(self):
        return Builder.load_string(makeMainWindowKVString([
            {
                'petName': 'hi',
                'dob': {
                    'day': '10',
                    'month': '05',
                    'year': '2005'
                },
                'lastVisit': {
                    'day': '25',
                    'month': '04',
                    'year': '2021'
                },
                'vetName': 'hi2',
                'diagnosis': 'hi3'
            },
            {
                'petName': 'hi',
                'dob': {
                    'day': '10',
                    'month': '05',
                    'year': '2005'
                },
                'lastVisit': {
                    'day': '25',
                    'month': '04',
                    'year': '2021'
                },
                'vetName': 'hi2',
                'diagnosis': 'hi3'
            }]))

UI().run()