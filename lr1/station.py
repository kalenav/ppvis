class Station:
    def __init__(self, id_IN, type_IN):
        self.id = id_IN
        self.type = type_IN
        self.adjacent = []
        self.weights = []

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def isAdjacentTo(self, adjacent):
        for currAdjacent in self.adjacent:
            if(currAdjacent == adjacent): 
                return True
        return False

    def getLinkWeight(self, adjacent):
        for index in len(self.adjacent):
            if(self.adjacent[index] == adjacent):
                return self.weights[index]

    def addAdjacent(self, adjacent, weight):
        self.adjacent.push(adjacent)
        self.weights.push(weight)