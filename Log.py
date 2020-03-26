from Database import Database

class Log:

    def __init__(self, main_crypto, sid, trade_crypto):
        self.db = Database()
        self.mc = main_crypto
        self.sid = sid
        self.tc = trade_crypto
        
    def initLog(self, status, decision):
        rate = 0
        
        data = []

        data.append(self.sid)
        data.append(self.mc)
        data.append(rate)
        data.append(self.tc)
        data.append(status)
        data.append(decision)
        data.append('null')

        self.lastid = self.db.writeLog(data)

    def log(self, status, decision, rate, tid = 'null'):
        
        data = []

        data.append(self.sid)
        data.append(self.mc)
        data.append(rate)
        data.append(self.tc)
        data.append(status)
        data.append(decision)
        data.append(tid)

        self.lastid = self.db.writeLog(data)

    def transaction(self, rate, amount, trtype, profit):

        data = []
        data.append(self.sid)
        data.append(self.mc)
        data.append(rate)
        data.append(self.tc)
        data.append(amount)
        data.append(profit)
        data.append(type)

        tid = self.db.writeTransaction(data)
        status = "Profit: " + str(profit) + "%"
        decision = trtype
        
        self.log(status = status, decision = decision, rate = rate, tid = tid)



    
   