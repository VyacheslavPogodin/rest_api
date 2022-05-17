from datetime import datetime
from urllib import response
import requests, json
from datetime import datetime
from GET_aut import authentication_token




ip = '10.10.29.110'
n=1
name_file = authentication_token()
'accessToken/2022-04-01 17-57-40.json'
with open(name_file) as json_file:
    data_head = json.load(json_file)
head = {'Authorization': data_head['accessToken']}

res_get = requests.get('http://'+ip+'/api/v1/devices', headers=head, timeout=10).json()
if res_get == []:
    ser_num = 28051986
else:
    ser_num = int(res_get[-1]['serial'])


pu_new = {'id_model': 1, 'id_interface': 1,
'included_in_survey': True, 'tariff_mask': 1, 'address': None,
'integral': 30, 'current_transformation_ratio': 1,
'voltage_transformation_ratio': 1, 'loss_ratio': 1,
'password_l': None, 'password_h': None,
'channel_mask': 7}

def conv(n,ri=10,ro=16):  #переводим из ri в ro
    digs="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=0
    for a in n:
        k=digs.find(a)
        acc=acc*ri+k
    res=""
    while(acc>0):
        k=acc%ro
        res=digs[k]+res
        acc=acc//ro
    return res


def add_n_new_dev(n_dev, ip):
    for i in range(n_dev):
        pu_new['serial'] = str(ser_num+1+i)
        pu_new['eui'] = conv(str(ser_num+1+i)).zfill(16)
        pu_new['name'] = 'test_'+str(ser_num+1+i)
        pu_new['in_time'] = str(datetime.now())[:-3]
        response = requests.post('http://'+ip+'/api/v1/devices', data=pu_new, timeout=10)
        #print(response.json()) 
        #print(response.headers)

add_n_new_dev(1, ip)

#res_roles = requests.get('http://'+ip+'/api/v1/currenttime', headers=head,  timeout=10)
#res = requests.get('http://'+ip+'/api/v1/archive/daily',headers=head, timeout=10)
#print(res.headers)

#Смена пароля и имени пользователя

#payload_roles = {'login': 'user_admin', 'role_name': 'user', 'password': 'admin123'}

#res_roles = requests.put('http://'+ip+'/api/v1/roles/1', headers=head,  json=payload_roles, timeout=10)
#print(res_roles.json())


#{ id_model integer                         NOT NULL,                       Номер модели
#  serial bigint                            NOT NULL,                       Серийный номер
#  eui character varying(16),               #тоже сделать NOT NULL          Индификатор на основе серийного номера
#  id_interface integer                     NOT NULL,                       Интерфейс общения прибора ПУ с УСПД
#  in_time timestamp without time zone      NOT NULL,                       Время включения в опрос
#  out_time timestamp without time zone,                                    Времы выключения прибора из опроса
#  archive boolean                          NOT NULL DEFAULT false,         Признак нахождения прибора ПУ в архиве устройств
#  included_in_survey boolean               NOT NULL,                       Признак включения устройства в опрос
#  last_time timestamp without time zone,
#  last_success_time timestamp without time zone,
#  tariff_mask integer,
#  online boolean                           DEFAULT false,
#  address bigint,
#  integral integer,
#  active_consumed boolean                  NOT NULL DEFAULT false,
#  active_released boolean                  NOT NULL DEFAULT true,
#  reactive_consumed boolean                NOT NULL DEFAULT false,
#  reactive_released boolean                NOT NULL DEFAULT false,
#  current_transformation_ratio integer,
#  voltage_transformation_ratio integer,
#  loss_ratio integer,
#  added timestamp without time zone        DEFAULT now(),
#  password_l character varying(64),
#  password_h character varying(64),
#  name character varying(128),
#  channel_mask integer}



{'id': 14,
'id_model': 2,
'serial': '28051996',
'eui': '0000000001AC0A1C',
'id_interface': 2,
'in_time': '2022-03-31 13:25:48.982', 
'out_time': None,
'archive': None, 'included_in_survey': True, 'last_time': None,
'last_success_time': None, 'tariff_mask': 4, 'online': False, 'address': None,
'integral': 30, 'active_consumed': False, 'active_released': True,
'reactive_consumed': False, 'reactive_released': False, 'current_transformation_ratio': 1,
'voltage_transformation_ratio': 1, 'loss_ratio': 1, 'added': '2022-03-31 13:50:51.19808',
'password_l': None, 'password_h': None, 'name': 'test_28051986', 'channel_mask': 7}