from playarea import PlayArea

class FileWriter:
    def __init__(self, path, playarea):
        self.file = open(path, 'w')
        self.playarea = playarea

    def writePlayareaToFile(self):
        file = self.file
        stations = self.playarea.getStations()
        trains = self.playarea.getTrains()
        file.write(str(len(stations)))
        for station in stations:
            if(len(station.adjacent) == 0):
                continue
            file.write(station.getId() + '(' + station.getType() + '): ')
            for currAdjacentStation in station.adjacent:
                file.write(currAdjacentStation.getId() + '(' + station.getLinkWeight(currAdjacentStation) + '), ')
        file.write('_')
        file.write(str(len(trains)))
        for train in trains:
            file.write(train.getSpeed() + ', ' + train.getServiceTimeLeft() + ', (')
            for carriage in train.getCarriages():
                file.write('Y' if carriage.isCargo() else 'N')
                file.write('/')
                file.write('Y' if carriage.isLoaded() else 'N')
                file.write(', ')
            file.write(', (')
            for station in train.getPath():
                file.write(station.id + ', ')
            file.write(')')
