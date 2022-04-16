class PlayArea:
    def __init__(self, stations, trains):
        self.stations = stations
        self.trains = trains

    def getStations(self):
        return self.stations

    def getTrains(self):
        return self.trains

    def sendTrain(self, index):
        self.trains[index].send()

    def stopTrain(self, index):
        self.trains[index].stop()
        self.trains[index].setCurrStationType(self.trains[index].getCurrStation().getType())
        self.trains[index].setCurrDistanceToDestination(self.trains[index].getCurrStation().getLinkWeight(self.trains[index].getCurrDestination()))

    def nextTurn(self):
        for index in range(len(self.trains)):
            train = self.trains[index]
            if(train.isEnRoute()):
                speed = train.getLocomotive().getSpeed()
                train.getLocomotive().reduceServiceTimeLeftBy(speed)
                if(train.getServiceTimeLeft() < 0):
                    train.disintegrate()
                    continue
                train.setCurrDistanceToDestination(train.getCurrDistanceToDestination() - speed)
                if(train.getCurrDistanceToDestination() <= 0):
                    self.stopTrain(index)

    def addTrain(self, train):
        self.trains.append(train)

    def addStation(self, station):
        self.stations.append(station)