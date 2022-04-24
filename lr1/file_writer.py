from playarea import PlayArea

class FileWriter:
    def __init__(self, path, playarea):
        self.file = open(path, 'w')
        self.playarea = playarea

    def writePlayareaToFile(self):
        file = self.file
        stations = self.playarea.getStations()
        trains = self.playarea.getTrains()
        file.write(str(len(stations)) + '\n')
        for station in stations:
            if(len(station.adjacent) == 0):
                continue
            toWrite = ''
            toWrite += str(station.getId()) + '(' + str(station.getType()) + '): '
            for currAdjacentStation in station.adjacent:
                toWrite += str(currAdjacentStation.getId()) + '(' + str(station.getLinkWeight(currAdjacentStation)) + '), '
            file.write(toWrite[:(len(toWrite) - 2)] + '\n')
        file.write('_\n')
        file.write(str(len(trains)) + '\n')
        for train in trains:
            toWrite = ''
            toWrite += str(train.getSpeed()) + ', ' + str(train.getServiceTimeLeft()) + ', ('
            for carriage in train.getCarriages():
                toWrite += 'Y' if carriage.isCargo() else 'N'
                toWrite += '/'
                toWrite += 'Y' if carriage.isLoaded() else 'N'
                toWrite += ', '
            toWrite = toWrite[:(len(toWrite) - 2)] + ('), (')
            for station in train.getPath():
                toWrite += str(station.id) + ', '
            file.write(toWrite[:len(toWrite) - 2] + ')\n')
