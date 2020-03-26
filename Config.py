import json

class Config:

    def __init__(self, path):
        self.confPath = path
        self.loadConf()
        self.writeConf()

    
    def loadConf(self):
        with open(self.confPath) as json_file:
            data = json.load(json_file)
            self.type = data['type']
            self.cryptoAmount = data['tradingAmount']
            self.mainCrypto = data['maincrypto']
            self.tradingCrypto = data['tradingcrypto']
            self.profit = data['profit']
    
    def writeConf(self):
        print("Type: " + self.type)
        print("Main Crypto: " + self.mainCrypto)
        print("Trading Crypto: " + self.tradingCrypto)
        print("Target profit: " + str(self.profit) + "%")
        print("Cryptocurrency amount for trading: " + str(self.cryptoAmount) + " " + str(self.mainCrypto))
    
    def verifyConfig(self):
        print("To Do")