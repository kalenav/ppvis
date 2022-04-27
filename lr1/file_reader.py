from carriage import Carriage
from locomotive import Locomotive
from train import Train
from station import Station
from playarea import PlayArea

class FileReader:
    def __init__(self, path):
        self.file = open(path, 'r')

    def readPlayareaFromFile(self):
        inputFileSplit = self.file.read().split('_')
        stations = inputFileSplit[0].join().split('\n')
        trains = inputFileSplit[1].join().split('\n')
