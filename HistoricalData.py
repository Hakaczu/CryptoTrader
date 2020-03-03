from pycoingecko import CoinGeckoAPI

class HistoricalData:

    def __init__(self, curr, vs_curr):
        self.curr = curr
        self.vs_curr = vs_curr
    
    