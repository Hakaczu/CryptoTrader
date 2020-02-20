from pycoingecko import CoinGeckoAPI

api = CoinGeckoAPI()

api.get_price(ids = 'bitcoin', vs_currencies = 'ethereum')


