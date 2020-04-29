from Alghoritm import Alghoritm
from Config import Config
from Log import Log
from coingecko import CoinGecko
import datetime
import time

class Core:
    configPath = 'config.json'
    botMainAmount = 0
    botTradingAmount = 0
    buyCurr = 0
    curr = 0
    seconds = 20

    def __init__(self):
        self.initConf()
        self.generateSID()
        self.initAlghoritm()
        self.initLog()
        self.initApi()

    def initAlghoritm(self):
        self.alg = Alghoritm(target = self.conf.profit)

    def initLog(self):
        self.log = Log(mainCrypto = self.conf.mainCrypto, tradingCrypto = self.conf.tradingCrypto, sid = self.sid)
        status = "Type: " + self.conf.type + "; Trading amount: " + str(self.conf.cryptoAmount) + "; Target profit: " + str(self.conf.profit)
        decision = "Let's start trading"
        self.log.initLog(status=status, decision=decision)
    
    def initConf(self):
        self.conf = Config(self.configPath)
        self.botMainAmount = self.conf.cryptoAmount

    def initApi(self):
        self.api = CoinGecko()

    def generateSID(self):
        mode = self.conf.type 
        date = datetime.datetime.now()
        date = date.strftime('%Y%m%d%H%M%S')
        self.sid = date + mode
        
    
    def printLog(self, status, decision, rate, mainCrypto):
        date = datetime.datetime.now()
        dateLog = date.strftime('%H:%M:%S')
        text = dateLog + "| " + str(rate) + " " + mainCrypto + " | " + status + " | " + decision
        print(text)

    def getStatus(self, profit):
        text = "Profit: "+ str(profit) + "%"
        return text
    
    def run(self):
        self.api.get48Data(maincrypto = self.conf.mainCrypto, tradingcrypto  = self.conf.tradingCrypto)
        try:
            while True:
                time.sleep(self.seconds)
                currOld = self.curr
                self.curr = self.api.getPrice(maincrypto = self.conf.mainCrypto, tradingcrypto=self.conf.tradingCrypto)
                if currOld == self.curr:
                    continue
                if self.botTradingAmount > 0:
                    decision = self.alg.checkSell(amount=self.botTradingAmount,curr=self.curr,buyCurr=self.buyCurr)
                    profit = self.alg.sellProfit(amount=self.botTradingAmount, curr=self.curr,buyCurr=self.buyCurr)
                    if decision == True:
                        self.log.transaction(rate=self.curr, amount=self.botTradingAmount, trtype="Sell", profit=profit)
                        self.botMainAmount = self.curr * self.botTradingAmount
                        self.botTradingAmount = 0
                        decision = "Sell"
                        status = self.getStatus(profit=profit)
                        self.printLog(status=status, decision=decision, rate=self.curr, mainCrypto=self.conf.mainCrypto)
                        self.api.get48Data(maincrypto = self.conf.mainCrypto, tradingcrypto  = self.conf.tradingCrypto)
                    else:
                        status = self.getStatus(profit=profit)
                        decision = "Wait of Sell" 
                        self.log.log(status=status, decision=decision, rate=self.curr)
                        self.printLog(status=status, decision=decision, rate=self.curr, mainCrypto=self.conf.mainCrypto)
                else:
                    decision = self.alg.checkBuy(avgCurr=self.api.avg48, minCurr=self.api.min48, curr=self.curr)
                    profit = self.alg.buyProfit(avgCurr=self.api.avg48, curr=self.curr)
                    if decision == True:
                        amount = self.botMainAmount / self.curr
                        self.log.transaction(rate=self.curr, amount=self.botMainAmount, trtype="Buy", profit=profit)
                        self.botTradingAmount = amount
                        self.botMainAmount = 0
                        self.buyCurr = self.curr
                        decision = "Buy"
                        status = self.getStatus(profit=profit)
                        self.printLog(status=status, decision=decision, rate=self.curr, mainCrypto=self.conf.mainCrypto)
                    else:
                        status = self.getStatus(profit=profit)
                        decision = "Wait of Buy" 
                        self.log.log(status=status, decision=decision, rate=self.curr)
                        self.printLog(status=status, decision=decision, rate=self.curr, mainCrypto=self.conf.mainCrypto)
                        self.api.get48Data(maincrypto = self.conf.mainCrypto, tradingcrypto  = self.conf.tradingCrypto)
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            pass
        except:
             print("Found Error Reset Core")
             self.run()

            

if __name__ == "__main__":
    core = Core()
    core.run()
