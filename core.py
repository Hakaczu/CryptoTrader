from Alghoritm import Alghoritm
from Config import Config
from sid import generateSID
from Log import Log
from coingecko import CoinGecko
import datetime
import time

def printLog(status, decision, rate, mainCrypto):
    date = datetime.datetime.now()
    dateLog = date.strftime('%H:%M:%S')
    text = dateLog + "| " + str(rate) + " " + mainCrypto + " | " + status + " | " + decision
    print(text)

def getStatus(profit):
    text = "Profit: "+ str(profit) + "%"
    return text

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
    curr = 0
    api.get48Data(maincrypto = conf.mainCrypto, tradingcrypto  = conf.tradingCrypto)
    
    try:
        while True:
            time.sleep(5)
            currOld = curr
            curr = api.getPrice(maincrypto = conf.mainCrypto, tradingcrypto=conf.tradingCrypto)
            if currOld == curr:
                continue
            if botTradingAmount > 0:
                decision = alg.checkSell(amount=botTradingAmount,curr=curr,buyCurr=buyCurr)
                profit = alg.sellProfit(amount=botTradingAmount, curr=curr,buyCurr=buyCurr)
                if decision == True:
                    log.transaction(rate=curr, amount=botMainAmount, trtype="Sell", profit=profit)
                    botMainAmount = curr * botTradingAmount
                    botTradingAmount = 0
                    decision = "Sell"
                    status = getStatus(profit=profit)
                    printLog(status=status, decision=decision, rate=curr, mainCrypto=conf.mainCrypto)
                else:
                    status = getStatus(profit=profit)
                    decision = "Wait of Sell" 
                    log.log(status=status, decision=decision, rate=curr)
                    printLog(status=status, decision=decision, rate=curr, mainCrypto=conf.mainCrypto)
            else:
                decision = alg.checkBuy(avgCurr=api.avg48, minCurr=api.min48, curr=curr)
                profit = alg.buyProfit(avgCurr=api.avg48, curr=curr)
                if decision == True:
                    amount = botMainAmount / curr
                    log.transaction(rate=curr, amount=amount, trtype="Buy", profit=profit)
                    botTradingAmount = amount
                    botMainAmount = 0
                    buyCurr = curr
                    decision = "Buy"
                    status = getStatus(profit=profit)
                    printLog(status=status, decision=decision, rate=curr, mainCrypto=conf.mainCrypto)
                else:
                    status = getStatus(profit=profit)
                    decision = "Wait of Buy" 
                    log.log(status=status, decision=decision, rate=curr)
                    printLog(status=status, decision=decision, rate=curr, mainCrypto=conf.mainCrypto)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
    except:
        print("Found Error Reset Core")
            

if __name__ == "__main__":
    core()
