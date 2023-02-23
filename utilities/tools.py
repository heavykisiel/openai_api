import datetime
import time
import hashlib

def timeDateWithBreak(breaksign):
    dt_n = datetime.datetime.now()
    timez = time.localtime()
    dt_nF = dt_n.strftime("%m/%d/%Y, %H:%M:%S")
    ct = time.strftime("%H:%M:%S", timez)
    breakt = breaksign#"_"
    t_str = ct[0]+ct[1]+ breakt +  ct[3] + ct[4] + breakt + ct[6] + ct[7] + breakt + dt_nF[0] + dt_nF[1] + breakt + dt_nF[3] + dt_nF[4] + breakt
    return t_str
def hasherUsername(username):
    a = hashlib.sha256(username.encode('utf-8')).hexdigest()
    return a
