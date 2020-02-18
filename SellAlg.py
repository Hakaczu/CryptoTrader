class SellAlg:
    def __init__(self, target, commission = 0, margin = 0):
        # target is in precent
        self.target = target / 100
        self.commission =  commission
        self.margin = margin
   
    def doSell(self, sc, pc):
        # pc - purchare cost
        # sc - selling cost
        profit =  sc - pc - (self.commission * sc)
        profit = profit / pc
        
