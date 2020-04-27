from pycoingecko import CoinGeckoAPI
import numpy
class CoinGecko:

    def __init__(self):
        self.api = CoinGeckoAPI()
        ping = self.api.ping()
        print(ping['gecko_says'])
    
    def get48Data(self, maincrypto, tradingcrypto):
        rawdata = self.api.get_coin_market_chart_by_id(id = tradingcrypto, vs_currency = maincrypto, days = 2)
        rawdata = rawdata['prices']
        data = []
        for record in rawdata:
            data.append(record[1])
        
        self.data48 = data
        self.avg48 = numpy.round_(numpy.average(self.data48), decimals=8)
        self.max48 = numpy.round_(numpy.max(self.data48), decimals=8)
        self.min48 = numpy.round_(numpy.min(self.data48), decimals=8)

        print("48h historical for " + tradingcrypto)
        print("Average: " + str(self.avg48) + " " + maincrypto)
        print("Maximum: " + str(self.max48) + " " + maincrypto)
        print("Minimum: " + str(self.min48) + " " + maincrypto)
    
    def getPrice(self, maincrypto, tradingcrypto):
        price = self.api.get_price(ids = tradingcrypto, vs_currencies = maincrypto)
        price = price[tradingcrypto][maincrypto]
        price = numpy.round_(price, decimals=8)
        return price



if __name__ == "__main__":
    api = CoinGecko()
    api.get48Data(maincrypto = 'eth', tradingcrypto = 'bitcoin')
    print(api.max48)
    print(api.min48)
    print(api.avg48)

    prc = api.getPrice(maincrypto = 'eth', tradingcrypto = 'bitcoin')
    print(prc)