class Locomotive():

    def __init__(self, speed_IN, service_time_left_IN):
        self.speed = self.speed_IN
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
