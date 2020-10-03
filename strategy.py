from envelope import Envelope
import random

class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes
        print("was base constructor")

    def getEnvelope(self, i):
        env = Envelope(self.envelopes[i])
        return env

    def play(self):
        print("was play  AAAA   BaseStrategy")
        loop = True
        i = 0
        while loop:
            env = self.envelopes[i]
            money = env.getMoney()
            print(" this envelpoes is", money)
            answer = input("If you want to chose and stop press 1 , to continue press any key  ")
            if answer == "1":
                loop = False
                print("Congratulations you won ", money , " $")
            else:
                i += 1
                if i == 100:
                    print("This is the last envelope. You won ", money, " $ ")
                    loop = False



class Automatic_BaseStrategy(BaseStrategy):
    def play(self):
        print("was play BBBB  Automatic_BaseStrategy")
        loop = True
        countUsed = 0
        while loop:
            i = random.randrange(1, 100)
            env = self.envelopes[i]
            if env.isUsed():
                continue
            else:
                money = env.getMoney()
                countUsed += 1
                if countUsed == 100:
                    print("This is the last envelope. You won ", money, " $ ")
                    loop = False
                else:
                    env.setUsed()
                    print(" This envelpoes is", money , " $ ")
                    answer = input("If you want to chose and stop press 1 , to continue press any key  ")
                    if answer == "1":
                        loop = False
                        print("Congratulations you won ", money, " $")



class N_max_strategy(BaseStrategy):
    def play(self):
        print("was play CCCC  N_max_strategy")

class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        self.envelopes = envelopes
        self.percent = percent

    def play(self):
        print("was play DDDD  More_then_N_percent_group_strategy")

