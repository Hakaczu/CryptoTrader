from Log import Log
from Config import Config
from sid import generateSID

sid = generateSID('simulation')

cf = Config("config.json")
cf.loadConf()

lg = Log(cf.mainCrypto, sid, cf.tradingCrypto)
lg.initLog(status = "Initial Log Simulation", decision = "Let's Start Trading!!!")
