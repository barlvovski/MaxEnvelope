class Envelope:
    def __init__(self, money):
        self.used = False
        self.money = money
        '''print("was here")
        print() '''

    def __init__(self):
        self.used = False
        self.money = 0

    def getMoney(self):
        return self.money
