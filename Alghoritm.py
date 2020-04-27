import numpy
class Alghoritm:
    def __init__(self, target, commission = 0, margin = 0):
        # target is in precent
        self.target = target
        self.commission =  commission
        self.margin = margin
        print("Trading Alghoritm is Ready")
   
    def checkSell(self, amount, curr, buyCurr):
        profit = self.sellProfit(amount = amount, curr = curr, buyCurr = buyCurr)
        if profit >= self.target:
            return True
        else:
            return False
    
    def sellProfit(self, amount, curr, buyCurr):
        pc = buyCurr * amount
        profit = ((amount * curr) - pc)/pc
        profit = profit * 100
        profit = numpy.round_(profit, decimals=8)
        return profit

    def buyProfit(self, avgCurr, curr):
        profit = avgCurr - curr
        profit = profit / avgCurr
        profit = profit * 100
        profit = numpy.round_(profit, decimals=8)
        return profit

    def checkBuy(self, avgCurr, minCurr, curr):
        if curr <= minCurr:
            return True
        else:
            profit = self.buyProfit(avgCurr = avgCurr, curr = curr)
            if profit >= self.target:
                return True
            else:
                return False


#test
# alg = Alghoritm(2)
# res =  alg.checkBuy(150,136,149)
# print(res)
# res = alg.checkSell(1, 146, 145)
# print(res)
