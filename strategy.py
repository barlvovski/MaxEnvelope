from envelope import Envelope

class Strategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes
        print("was base constructor")

    def getEnvelope(self, i):
        env = Envelope(self.envelopes[i])
        return env










class BaseStrategy(Strategy):
    pass

class Automatic_BaseStrategy(Strategy):
    pass

class N_max_strategy(Strategy):
    pass

class More_then_N_percent_group_strategy(Strategy):
    def __init__(self, envelopes, percent):
        super.__init__(envelopes)
        self.percent = percent
