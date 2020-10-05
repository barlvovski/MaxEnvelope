class Envelope:
    def __init__(self, money):
        '''
        Constructor of envelope
        :param money:
        sets used as false
        '''
        self.used = False
        self.money = money

    def getMoney(self):
        '''
        getMoney function
        :return:
        function returns money of this envelope
        '''
        return self.money

    def isUsed(self):
        '''
        isUsed function
        :return: if envelope is used

        '''
        return self.used

    def setUsed(self):
        '''
        sets used as true

        '''
        self.used = True

