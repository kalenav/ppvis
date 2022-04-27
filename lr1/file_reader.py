from cgi import print_arguments
from carriage import Carriage
from train import Train
from station import Station
from playarea import PlayArea

class FileReader:
    def __init__(self, path):
        self.file = open(path, 'r')

    def __readIntUntilLimiter(self, string, index, limiters):
        toConvert = ''
        while(index < len(string) and not string[index] in limiters):
            toConvert += string[index]
            index += 1
        return { 'integer': int(toConvert), 'finishedAt': index }

    def readPlayareaFromFile(self):
        inputFileSplit = self.file.read().split('_')
        if(inputFileSplit[0] == ''):
            return

        stationsLines = inputFileSplit[0].strip().split('\n')
        stations = []

        for line in stationsLines:
            currStationIdReadResult = self.__readIntUntilLimiter(line, 0, ['('])
            currStationId = currStationIdReadResult['integer']
            currStationType = self.__readIntUntilLimiter(line, currStationIdReadResult['finishedAt'] + 1, [')'])['integer']
            stations.append(Station(currStationId, currStationType))

        for line in stationsLines:
            currStationIdReadResult = self.__readIntUntilLimiter(line, 0, ['('])
            currStation = stations[currStationIdReadResult['integer'] - 1]
            currStationTypeReadResult = self.__readIntUntilLimiter(line, currStationIdReadResult['finishedAt'] + 1, [')'])
            currSymbolIndex = currStationTypeReadResult['finishedAt'] + 3
            while(currSymbolIndex < len(line)):
                currAdjacentStationIdReadResult = self.__readIntUntilLimiter(line, currSymbolIndex, ['('])
                currAdjacentStation = stations[currAdjacentStationIdReadResult['integer'] - 1]
                currSymbolIndex = currAdjacentStationIdReadResult['finishedAt'] + 1
                currAdjacentStationLinkWeightReadResult = self.__readIntUntilLimiter(line, currSymbolIndex, [')'])
                currAdjacentStationLinkWeight = currAdjacentStationLinkWeightReadResult['integer']
                currSymbolIndex = currAdjacentStationLinkWeightReadResult['finishedAt'] + 3
                currStation.addAdjacent(currAdjacentStation, currAdjacentStationLinkWeight)

