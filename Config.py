import json

class Config:

    def __init__(self, path):
        self.confPath = path
        self.loadConf()

    
    def loadConf(self):
        with open(self.confPath) as json_file:
            data = json.load(json_file)
            self.type = data['type']
            self.cryptoAmount = data['start_sim_crypto']
            self.mainCrypto = data['maincrypto']
            self.traidingCrypto = data['traidingcrypto']
            self.profit = data['profit']
    
    def verifyConfig(self):
        print("To Do")