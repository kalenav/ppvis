from locomotive import Locomotive

class Train():

    def __init__(self, locomotive_speed_IN, locomotive_service_time_left_IN, carriages_IN, path_IN):
        self.locomotive = Locomotive(locomotive_speed_IN, locomotive_service_time_left_IN)
        self.carriages = []
        for curr_carriage in carriages_IN:
            self.carriages.append(curr_carriage)
        self.path = path_IN.copy()
        self.curr_station_in_path_index = 0
        self.broken = False

    def setCurrStation(self, input):
        self.curr_station = input

    def setCurrStationType(self, input):
        self.curr_station_type = input

    def setCurrDestination(self, input):
        self.curr_destination = input

    def setCurrDistanceToDestination(self, input):
        self.curr_distance_to_destination = input

    def send(self):
        self.en_route = True

    def stop(self):
        self.en_route = False
        self.advance()

    def advance(self):
        self.curr_station = self.curr_destination
        self.curr_station_in_path_index = (self.curr_station_in_path_index + 1) % len(self.path)
        self.curr_destination = self.path[(self.curr_station_in_path_index + 1) % len(self.path)]

    def load(self):
        for carriage in self.carriages:
            if(carriage.isCargo() and not carriage.isLoaded() and self.curr_station_type != 1):
                carriage.load()
                self.locomotive.decreaseSpeedByOne()
            if(not carriage.isCargo() and not carriage.isLoaded() and self.curr_station_type != 0):
                carriage.load()
                self.locomotive.decreaseSpeedByOne()
    
    def unload(self):
        for carriage in self.carriages:
            if(carriage.isCargo() and carriage.isLoaded() and self.curr_station_type != 1):
                carriage.unload()
                self.locomotive.increaseSpeedByOne()
            if(not carriage.isCargo() and carriage.isLoaded() and self.curr_station_type != 0):
                carriage.unload()
                self.locomotive.increaseSpeedByOne()

    def disintegrate(self):
        self.broken = True
    
    def getLocomotive(self):
        return self.locomotive

    def getCarriages(self):
        return self.carriages

    def getPath(self):
        return self.path

    def isEnRoute(self):
        return self.en_route

    def isBroken(self):
        return self.broken

    def getCurrStation(self):
        return self.curr_station

    def getCurrStationType(self):
        return self.curr_station_type
    
    def getCurrDestination(self):
        return self.curr_station_type

    def getCurrDistanceToDestination(self):
        return self.curr_distance_to_destination

    def getServiceTimeLeft(self):
        return self.locomotive.getServiceTimeLeft()