#from train import Train

class PlayArea:
    def __init__(self, stations_IN, trains_IN):
        self.stations = stations_IN
        self.trains = trains_IN

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