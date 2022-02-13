from operator import truediv
from turtle import distance

class Carriage():

    def __init__(self, cargo, loaded):
        self.isCargo = cargo
        self.isLoaded = loaded

    def load(self):
        self.isLoaded = True

    def unload(self):
        self.isLoaded = False

    def isCargoCarriage(self):
        return self.isCargo

    def isLoadedCarriage(self):
        return self.isLoaded


class Locomotive():

    def __init__(self, speed_IN, service_time_left_IN):
        self.speed = speed_IN
        self.service_time_left = service_time_left_IN

    def increaseSpeedByOne(self):
        self.speed += 1
    
    def decreaseSpeedByOne(self):
        self.speed -= 1

    def reduceServiceTimeLeftBy(self, input):
        self.service_time_left -= input

    def getSpeed(self):
        return self.speed
    
    def getServiceTimeLeft(self):
        return self.service_time_left

class Train():

    en_route = False
    curr_station_in_path_index = 0
    broken = False

    def __init__(self, locomotive_speed_IN, locomotive_service_time_left_IN, carriage_info_IN, path_IN):
        self.locomotive = Locomotive(locomotive_speed_IN, locomotive_service_time_left_IN)
        for curr_carriage_info in carriage_info_IN:
            self.carriages.append(Carriage(curr_carriage_info[0], curr_carriage_info[1]))
        self.path = path_IN.copy()
        self.curr_station = self.path[0]
        self.curr_destination = self.path[1]

    def setStationType(self, station_type_IN):
        self.curr_station_type = station_type_IN

    def setCurrDistanceToDestination(self, distance_IN):
        self.curr_distance_to_destination = distance_IN

    def send(self):
        self.en_route = True

    def stop(self):
        self.en_route = False
        self.advance()

    def advance(self):
        self.curr_station = self.curr_destination
        self.curr_station_in_path_index = (self.curr_station_in_path_index + 1) % len(self.path)
        self.curr_destination = self.path[(self.curr_station_in_path_index + 1) % len(self.path)]

    def breakdown(self):
        self.broken = True

    def load(self):
        for carriage in self.carriages:
            if(carriage.isCargo() and not carriage.isLoaded() and self.curr_station_type != 1):
                carriage.load()
                self.locomotive.decreaseSpeedByOne()
            if(not carriage.isCargo() and not carriage.isLoaded() and self.curr_station_type != 0):
                carriage.load()
                self.locomotive.decreaseSpeedByOne()

    def reduceServiceTimeLeftBy(self, input):
        self.locomotive.reduceServiceTimeLeftBy(input)

    
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
        return self.curr_destination

    def getCurrDistanceToDestination(self):
        return self.curr_distance_to_destination

    def getServiceTimeLeft(self):
        return self.locomotive.getServiceTimeLeft()

class PlayArea():
    def __init__(self, string_IN):
        return 1



