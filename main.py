# This is a sample Python script.

# Comments


from envelope import Envelope

from strategy import Strategy, BaseStrategy, Automatic_BaseStrategy, N_max_strategy, More_then_N_percent_group_strategy

if __name__ == '__main__':
    env1 = Envelope(5)
    env = []
    for i in range(100):
        env.append(Envelope(10))
    '''this is my comment'''
    '''this is my comment'''

    '''this is my comment'''


    '''str1 = BaseStrategy(env)

    str2 = Automatic_BaseStrategy(env)'''

    str1 = BaseStrategy(env)



    '''str3 = More_then_N_percent_group_strategy(env, 0.75) '''



