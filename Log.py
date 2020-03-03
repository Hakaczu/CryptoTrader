from Database import Database

class Log:

    def __init__(self, curr_id):
        self.db = Database()
        self.curr_id = curr_id
        
    def initLog(self, status):
        rate = 0
        self.db.writeLog(curr_id = self.curr_id, status = status , rate = rate)
    
    def getCurr(self, rate, status):
        self.db.writeLog(curr_id = self.curr_id, rate = rate, status = status)