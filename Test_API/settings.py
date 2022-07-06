
# IP сервера
ip = '10.10.29.110'


# формирование url адресов для тестирования
def url_form_in_ip(key):
    desp_url = {'auth': 'authentication',
    'info_uspd': 'devinfo',
    'configyre': 'confmode',
    'time': 'currenttime',
    'time_zone': 'tzcode',
    'ntp_serv': 'ntpservers',
    'interfaces': 'devinterfaces',
    'rs-485': 'rsconfig',
    'eth': 'confethernet',
    'gsm_1': 'gsmconfig/1',
    'gsm_2': 'gsmconfig/2',
    'discretejournal': 'discretejournal',
    'timesynq': 'timesynq',
    'powerjournal': 'powerjournal',
    }
    return 'http://'+ip+'/api/v1/'+desp_url[key]