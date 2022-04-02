class Station:
    def __init__(self, id_IN, type_IN, adjacentInfo_IN):
        self.id = id_IN
        self.type = type_IN
        self.adjacent = []
        self.weights = []
        for currAdjacent in adjacentInfo_IN:
            self.adjacent.push(currAdjacent[0])
            self.weights.push(currAdjacent[1])

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