#import pysqlite3
import sqlite3
import datetime
#https://docs.python.org/3.8/library/sqlite3.html

class Database:
    path = "trades.db"

    def __init__(self):
        self.open()

    def open(self):
        try:
            self.connection = sqlite3.connect(self.path)
            print("Database connect OK")

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
    
    def writeLog(self, curr_id, status, rate):
        date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO trade_log(date, curr_id, rate, status) VALUES('" + date  + "', '" + curr_id + "', " + str(rate) + ", '" + status +"')"
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        return cur.lastrowid

    def readLog10(self):
        query = "SELECT date, curr_id, rate, status FROM trade_log LIMIT 10"
        cur = self.connection.cursor()
        cur.execute(query)
        res =  cur.fetchall()
        return res

    def close(self):
        self.connection.close