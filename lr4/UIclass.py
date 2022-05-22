class UI():

    def __init__(self):
        pass

    def send_train(self, playarea, index):
        train = playarea.getTrains()[index]
        if(train.isEnRoute()):
            return 'en route'
        else:
            if(train.getLocomotive().getSpeed() <= 0):
                return 'overloaded'
            else:
                playarea.sendTrain(index)
                return 'ok'

    def load_train(self, playarea, index):
        train = playarea.getTrains()[index]
        if(train.isEnRoute()):
            return 'en route'
        else:
            train.load()
            return 'ok'

    def unload_train(self, playarea, index):
        train = playarea.getTrains()[index]
        if(train.isEnRoute()):
            return 'en route'
        else:
            train.unload()
            return 'ok'

    def next_turn(self, playarea):
        playarea.nextTurn()