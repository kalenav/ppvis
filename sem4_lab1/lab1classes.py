from operator import truediv

class Carriage(object):
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





