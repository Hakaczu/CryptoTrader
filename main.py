from Log import Log
from Config import Config
from sid import generateSID

sid = generateSID('simulation')

cf = Config("accounts.json")
cf.loadConf()

lg = Log(cf.mainCrypto, sid, cf.traidingCrypto)
lg.initLog(status = "Initial Log Simulation", decision = "Let's Start Trading!!!")
