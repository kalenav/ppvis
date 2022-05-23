from playarea import PlayArea
from carriage import Carriage
from train import Train
from station import Station
from file_writer import FileWriter
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '..\\lr1\\examples\\pa1.txt')

station1 = Station(0, 0)
station2 = Station(1, 0)
station3 = Station(2, 2)

station1.addAdjacent(station2, 3)
station2.addAdjacent(station1, 5)
station2.addAdjacent(station3, 1)
station3.addAdjacent(station1, 5)

c1_1 = Carriage(True, True)
c1_2 = Carriage(False, True)
train1 = Train(5, 500, [c1_1, c1_2], [station1, station2])

c2_1 = Carriage(False, False)
train2 = Train(3, 100, [c2_1], [station2, station3, station1])

playarea = PlayArea([station1, station2, station3], [train1, train2])

FileWriter(filename, playarea).writePlayareaToFile()