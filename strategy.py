from envelope import Envelope
import random

class BaseStrategy:

    def __init__(self, envelopes):
        '''
        constructor of base strategy class
        :param envelopes: the list of envelopes
        '''
        self.envelopes = envelopes


    def getEnvelope(self, i):
        '''
        get specific envelope
        :param i:  the index of the envelope
        :return: the envelope
        '''
        env = Envelope(self.envelopes[i])
        return env

    def display(self):
        '''
        :return: returns the strategy name
        '''
        print("BaseStrategy")

    def play(self):
        '''
        the play function : choosing the envelope according to the base strategy
        according to the user choice
        :return: money from your chosen envelope
        '''
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

    def display(self):
        '''
        :return: returns the strategy name
        '''
        print("Automatic_BaseStrategy")


    def play(self):
        '''
        the function of Automatic_BaseStrategy :
        random choice of envelope + choice according to the users choice
        :return:
        '''
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
                    print(" This envelope is", money, " $ ")
                    answer = input("If you want to chose and stop press 1 , to continue press any key  ")
                    if answer == "1":
                        loop = False
                        print("Congratulations you won ", money, " $")


''' N Max Strategy '''
class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        '''
        constructor of nmax strategy
        :param envelopes:
        '''
        self.envelopes = envelopes
        self.N = 3

    def display(self):
        '''
        :return: returns the strategy name
        '''
        print("N_max_strategy")

    def play(self):
        '''
        Find the max value envelopes after n max values
        default value is 3 + printing max envelope
        '''
        print("was play CCCC  N_max_strategy")
        mymax = 0
        timetostop = 0

        for i in range(1, 100):
            env = self.envelopes[i]
            money = env.getMoney()
            if money > mymax:
                mymax = money
                timetostop += 1
                if timetostop == self.N:
                    break
        print("Congratulations you won ", money, " $")


class More_then_N_percent_group_strategy(BaseStrategy):
    def display(self):
        '''
        :return: returns the strategy name
        '''
        print("More_then_N_percent_group_strategy")

    def __init__(self, envelopes, percent):
        '''
        constructor of More_then_N_percent_group_strategy
        :param envelopes:
        :param percent: the percent of first find group
        '''
        self.envelopes = envelopes
        self.percent = float(0.25)


    def play(self):
        '''
        1.finding max envelope in X% of first envelopes (according to percent)
        2. finding thr first envelopes that greater than we found in 1)
        3. printing max envelops
        
        '''
        print("was play DDDD  More_then_N_percent_group_strategy")
        loop1 = int(100 * float(self.percent))
        print(loop1)
        mymax = 0
        indmax = 0
        for i in range(1, loop1):
            env = self.envelopes[i]
            money = env.getMoney()
            if money > mymax:
                mymax = money
                indmax = i
        for i in range(loop1 + 1, 100):
            env = self.envelopes[i]
            money = env.getMoney()
            if money > mymax:
                mymax = money
                indmax = i
                break

        print("Congratulations you won ", money,  " $ ", "in envelope number ", indmax )
