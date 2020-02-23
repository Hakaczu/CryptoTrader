#import pysqlite3
import sqlite3
#https://docs.python.org/3.8/library/sqlite3.html

class Database:
    def __init__(self, path):
        self.path = path
        self.open()

    def open(self):
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            print("Database connect OK")

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
    
    def wiriteQuery(self, query):
        self.cursor.excute(query)
        self.connection.commit()
    
    def readQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.connection.close