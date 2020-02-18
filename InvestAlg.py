class InvestAlg:
    def __init__(self, base, sumweight):
        self.base =  base
        self.sum = sumweight
    
    def getAmountToInvest(self, weight):
        amount = self.base / self.sum
        amount = amount * weight
        return amount
    