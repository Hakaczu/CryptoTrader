import json

class Config:



    def __init__(self, path):
        self.confPath = path
    
    def loadConf(self):
        with open(self.confPath) as json_file:
            data = json.load(json_file)
            self.mainFiat = data['traiding']['main_fiat_account']
            self.mainCrypto = data['traiding']['main_crypto_account']
            self.traidingCrypto = data['traiding']['traiding_crypto']
            self.profit = data['traiding']['profit_precent']