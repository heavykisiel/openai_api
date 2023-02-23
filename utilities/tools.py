import datetime
import time
import hashlib
import os
from configparser import ConfigParser


def get_cfg():
    file = 'config.cfg'
    cfg = ConfigParser()
    cfg.read(file)
    return cfg

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

def addApiKey():
    cfg = get_cfg()
    if cfg['userinfo']['apiKey'] != "":
        b = input('You provided your apiKeys, do you want to change it? (y/n)')
        if b[0] == 'y' or b[0] == 'y'.upper():
            addApiKeyInput()
    else:
       addApiKeyInput()

def addApiKeyInput():
        cfg =  get_cfg()
        print('Provide you openai API keys: ')
        print('1. Via env variables')
        print('2. Via config file')
        print('3. Manually here')
        print('4. Press any Key to quit')
        a = input('select option (1/2/3/AnyKey) ')
        if a == '1':
            try:
                print('\nyour API key in env variables is set to: '+ os.environ['OPENAI_API_KEY'])
                print('your API key in config.cfg is set to: '+ cfg['userinfo']['apiKey'])
            except KeyError:
                print('Your do not have env variable setted')
                print('To do so, you have to: ')
            finally:
                print('\trun "cmd" with windowsKey + r')
                print('\ttype "set OPENAI_API_KEY = [your api key]"')
                print('\twhere [your api key] is your 51 characters key')
                print('\tif you set your key you may need to restart your CMD')
                print('\tIf you dont have api key it can be generated from the link below')
                print('\thttps://platform.openai.com/account/api-keys')
        if a == '2':
                print('')
        if a == '3':
            print('\nyour API key in env variables is set to: '+ os.environ['OPENAI_API_KEY'])
            print('your API key in config.cfg is set to: '+ cfg['userinfo']['apiKey'])
            b = input('input your API key here to: ')
            cfg['userinfo']['apiKey'] = b
            with open('config.cfg', 'w') as cfgFile:
                cfg.write(cfgFile)

def checkApiKey():
    cfg = get_cfg()
    if cfg['userinfo']['apiKey'] != "":
        if len(cfg['userinfo']['apiKey']) == 51:
            return True
    if os.getenv("OPENAI_API_KEY") != "" or None:
        if len(os.getenv("OPENAI_API_KEY")) == 51:
            return True
    return False