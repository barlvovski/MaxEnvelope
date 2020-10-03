# This is a sample Python script.

# Comments

import random
from envelope import Envelope




from strategy import BaseStrategy, Automatic_BaseStrategy, N_max_strategy, More_then_N_percent_group_strategy

if __name__ == '__main__':




    '''def cls():
        print( & quot;\


        n & quot;
    *20) '''
    envelopes = []
    for i in range(100):
        money = random.randrange(1, 5000)
        envelopes.append(Envelope(money))
    '''
    for i in range(100):
        print(envelopes[i].getMoney())
    '''
    strategies = []
    strategies.append(BaseStrategy(envelopes))
    '''
    strategies[0].play()
    '''
    strategies.append(Automatic_BaseStrategy(envelopes))
    strategies[1].play()
    '''
    strategies.append(N_max_strategy(envelopes))
    strategies[2].play()

    strategies.append(More_then_N_percent_group_strategy(envelopes, 0.25))
    strategies[3].play()
    '''
    '''
    # user select manually envelopes
    strategies.append(Automatic_BaseStrategy(envelopes))
    # random selection of envelop
    strategies.append(N_max_strategy(envelopes))
    # return envelope after N max values (defualt N=3)
    strategies.append(More_then_N_percent_group_strategy(envelopes,0.25)
    '''





