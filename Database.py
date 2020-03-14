#import pysqlite3
import sqlite3
import datetime
#https://docs.python.org/3.8/library/sqlite3.html

class Database:
    path = "trades.db"

    def __init__(self):
        self.open()
        self.data = datetime.datetime

    def open(self):
        try:
            self.connection = sqlite3.connect(self.path)
            print("Database connect OK")

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
    
    def prepareData(self):
        date = self.data.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        return date

    def writeLog(self, data):
        date = self.prepareData()
        query = "INSERT INTO Log(date, sid, main_crypto, rate, trade_crypto, status, decision, tid) VALUES('" + date + "', ?, ?, ?, ?, ?, ?, ?)"
        cur = self.connection.cursor()
        cur.execute(query, data)
        self.connection.commit()
        return cur.lastrowid

    # def readLog10(self):
    #     query = "SELECT date, curr_id, rate, status FROM trade_log LIMIT 10"
    #     cur = self.connection.cursor()
    #     cur.execute(query)
    #     res =  cur.fetchall()
    #     return res

    def writeTransaction(self, data):
        date = self.prepareData()
        query = "INSERT INTO Transactions(date, sid, main_crypto, rate, trade_crypto, amount, profit, type) VALUES('" + date + "', ?, ?, ?, ?, ?, ?, ?)"
        cur = self.connection.cursor()
        cur.execute(query, data)
        self.connection.commit()
        return cur.lastrowid


    def close(self):
        self.connection.close