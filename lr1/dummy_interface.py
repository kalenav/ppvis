from carriage import Carriage
from train import Train
from station import Station
from playarea import PlayArea
from file_writer import FileWriter
from file_reader import FileReader

def inputFail():
    print("This is not even a possible choice. What were you thinking? Will you ever be able to clear yourself from this shame? I certainly hope so. Anyway, please choose something from the list provided.")

station1 = Station(1, 1)
station2 = Station(2, 1)
station3 = Station(3, 0)
station1.addAdjacent(station2, 3)
station2.addAdjacent(station1, 5)
station2.addAdjacent(station3, 10)
station3.addAdjacent(station2, 1)
stations = [station1, station2, station3]

carriage1_1 = Carriage(True, True)
carriage1_2 = Carriage(False, True)
carriage2_1 = Carriage(False, True)

train1 = Train(5, 500, [carriage1_1, carriage1_2], [station1, station2])
train2 = Train(3, 200, [carriage2_1], [station2, station3])
trains = [train1, train2]

playarea = PlayArea(stations, trains)

while True:
    print("\nWhat would you like to do?")
    print("1. Show current play area state")
    print("2. Show train info")
    print("3. Send/load/unload a train")
    print("4. Continue to the next turn")
    print("5. End game\n")

    choice = int(input())
    if(choice == 1):
        print("=======================================================")
        stations = playarea.getStations()
        stations_quantity = len(stations)
        graph = []
        for i in range(stations_quantity):
            graph.append([0] * stations_quantity)
        for index in range(stations_quantity):
            curr_station = stations[index]
            for adjacentIndex in range(stations_quantity):
                curr_adjacent_station = stations[adjacentIndex]
                if(curr_station.isAdjacentTo(curr_adjacent_station)):
                    graph[index][adjacentIndex] = curr_station.getLinkWeight(curr_adjacent_station)
        print("The play area graph has the following appearance:")
        for i in range(stations_quantity):
            curr_row = ""
            for j in range(stations_quantity):
                curr_row += (str(graph[i][j]) + " ")
            print(curr_row)
        print("\nThe stations are as follows:")
        for station in stations:
            curr_str = "Station " + str(station.getId()) + ": "
            if(station.type == 0):
                curr_str += "cargo"
            elif(station.type == 1):
                curr_str += "passenger"
            else:
                curr_str += "cargo/passenger"
            print(curr_str)
        trains = playarea.getTrains()
        print("\nThe trains are as follows:")
        for index in range(len(trains)):
            curr_str = "Train " + str(index) + " "
            curr_train = trains[index]
            if(curr_train.isEnRoute()):
                curr_str += "en route to station " + str(curr_train.getCurrDestination().getId()) + "; " + str(curr_train.turnsLeftToDestination()) + " turns left"
            else:
                curr_str += "is waiting at station " + str(curr_train.getCurrStation().getId()) + "; next station is " + str(curr_train.getCurrDestination().getId())
            print(curr_str)
        print("=======================================================")

    elif(choice == 2):
        print("Input train index: ")
        index = int(input())
        train = playarea.getTrains()[index]
        if(train.isEnRoute()):
            print("Currently en route to station " + str(train.getCurrDestination().getId()))
        else:
            print("Currently waiting at station " + str(train.getCurrStation().getId()) + "; next destination is station " + str(train.getCurrDestination().getId()))
        print("Current speed: " + str(train.getLocomotive().getSpeed()))
        print("Service time left: " + str(train.getServiceTimeLeft()))
        carriages = train.getCarriages()
        print("Has " + str(len(carriages)) + " carriages")
        for index in range(len(carriages)):
            carriageInfo = "Carriage "
            carriageInfo += str(index + 1) + ": "
            if(carriages[index].isCargo()): 
                carriageInfo += "cargo; "
            else:
                carriageInfo += "passenger; "
            if(carriages[index].isLoaded()):
                carriageInfo += "loaded"
            else:
                carriageInfo +="empty"
            print(carriageInfo)

    elif(choice == 3):
        print("Input train index: ")
        index = int(input())
        train = playarea.getTrains()[index]
        print("\nWhat would you like to do?")
        print("1. Send to the next station")
        print("2. Load")
        print("3. Unload")
        print("4. I changed my mind, this train is the embodiment of perfection and I would never do something as horrendously inappropriate and flatout stupid as changing its characteristics is")
        choice = int(input())
        if(choice == 1):
            if(train.isEnRoute()):
                print("This train is already on its way. It'll get there when it'll get there. Show some patience.")
            else:
                if(train.getLocomotive().getSpeed() <= 0):
                    print("This train is overloaded. Consider unloading some of its carriages.")
                else:
                    playarea.sendTrain(index)
                    print("This train is now en route to its destination. Look at it go! Oh, right, you can't, it's a command line style interface. My bad.")
        elif(choice == 2):
            if(train.isEnRoute()):
                print("This train is en route to its destination. It's not like you can load it on the fly. There's also nothing to load, it's somewhere in the steppes or in a forest, probably.")
            else:
                train.load()
                print("Empty carriages corresponding with current station type have been loaded.")
        elif(choice == 3):
            if(train.isEnRoute()):
                print("This train is en route to its destination. It's not like you can unload it on the fly. There's also nohwere to unload, it's somewhere in the steppes or in a forest, probably. Unless you want to get rid of the cargo, which is utter nonsense.")
            else:
                train.unload()
                print("Loaded carriages corresponding with current station type have been unloaded.")
        elif(choice == 4):
            pass
        else:
            inputFail()
    elif(choice == 4):
        playarea.nextTurn()

    elif(choice == 5):
        fr = FileReader('E:\\Important\\uchoba\\ppvis\\lr1\\examples\\pa1.txt')
        fr.readPlayareaFromFile()
        # fw = FileWriter('E:\\Important\\uchoba\\ppvis\\lr1\\examples\\pa1.txt', playarea)
        # fw.writePlayareaToFile()
        break
    else:
        inputFail()
            
