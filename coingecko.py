from pycoingecko import CoinGeckoAPI
import numpy
api = CoinGeckoAPI()

price=api.get_price(ids = 'bitcoin', vs_currencies = 'eth')
print(price)
rawdata = api.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency= 'usd', days='2')
rawdata = rawdata['prices']
data = []
for record in rawdata:
    data.append(record[1])
print(len(data))
avg = numpy.average(data)
maximum = numpy.max(data)
print(maximum)
print(avg)
