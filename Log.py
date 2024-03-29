from Database import Database


class Log:

    def __init__(self, mainCrypto, sid, tradingCrypto):
        self.db = Database()
        self.mc = mainCrypto
        self.sid = sid
        self.tc = tradingCrypto

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

    def log(self, status, decision, rate, tid='null'):
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
        data.append(trtype)

        tid = self.db.writeTransaction(data)
        status = "Profit: " + str(profit) + "%"
        decision = trtype

        self.log(status=status, decision=decision, rate=rate, tid=tid)


if __name__ == "__main__":
    lg = Log("tet", "111", "tet3")
    lg.transaction(1111, 1, "Buy", 12)
