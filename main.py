from Database import Database

db = Database("trades.db")
db.writeLog('none', 'initial log', 0)

logs = db.readLog10()
for log in logs:
    print(log)