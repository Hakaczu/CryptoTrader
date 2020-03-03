from Log import Log
from Config import Config

cf = Config("accounts.json")
cf.loadConf()

lg = Log(cf.mainCrypto)
lg.initLog('Type: Simulation; ')
