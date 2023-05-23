import requests
from time import sleep

def set_on_configur_econfmode(url_base):        
        
    Token_r = requests.post(url_base+'/api/v1/authentication', data={'strategy': 'local', 'login': 'admin', 'password': 'admin'}).json()
    
    response = requests.post(url_base+'/api/v1/confmode', headers={'Authorization': Token_r['accessToken']}, data= {"mode":"conf_in"}, timeout=10)
    print(response.json())



if __name__ == '__main__':

    while True:
        set_on_configur_econfmode('http://10.10.29.109')
        sleep(2400)