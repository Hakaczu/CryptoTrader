import datetime

def generateSID(mode):
    date = datetime.datetime.now()
    date = date.strftime('%Y%m%d%H%M%S')
    sid = date + mode
    return sid