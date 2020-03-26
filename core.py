from Alghoritm import Alghoritm
from Config import Config
from sid import generateSID
from Log import Log
from coingecko import CoinGecko
import time
def core():
    print("Crypto Trading Bot")
    conf = Config('config.json')
    sid = generateSID(conf.type)
    print("Session ID: " + sid)
    log = Log(mainCrypto = conf.mainCrypto, tradingCrypto = conf.tradingCrypto, sid = sid)
    alg = Alghoritm(target = conf.profit)
    status = "Type: " + conf.type + "; Trading amount: " + str(conf.cryptoAmount) + "; Target profit: " + str(conf.profit)
    decision = "Let's start trading"
    log.initLog(status=status, decision=decision)
    #start bot config
    api = CoinGecko()
    botMainAmount = conf.cryptoAmount
    botTradingAmount = 0
    buyCurr = 0
    api.get48Data(maincrypto = conf.mainCrypto, tradingcrypto  = conf.tradingCrypto)
    curr = api.getPrice(maincrypto = conf.mainCrypto, tradingcrypto=conf.tradingCrypto)
    
    if botTradingAmount > 0:
        decision = alg.checkSell(amount=botTradingAmount,curr=curr,buyCurr=buyCurr)
        profit = alg.sellProfit(amount=botTradingAmount, curr=curr,buyCurr=buyCurr)
        if decision == True:
            log.transaction(rate=curr, amount=botMainAmount, trtype="Sell", profit=profit)
            botMainAmount = curr * botTradingAmount
            botTradingAmount = 0
    else:
        decision = alg.checkBuy(avgCurr=api.avg48, minCurr=api.min48, curr=curr)
        profit = alg.buyProfit(avgCurr=api.avg48, curr=curr)
        if decision == True:
            log.transaction(rate=curr, amount=botMainAmount, trtype="Buy", profit=profit)
            botTradingAmount = botMainAmount / curr
            botMainAmount = 0
            buyCurr = curr
            





if __name__ == "__main__":
    core()
