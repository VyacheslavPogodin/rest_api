import json
import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/gsmconfig'

paydata_new={'id': 1, 'sim_num': '1', 'apn': 'FixedIP.nw', 'username': 'test1', 'password': 'test1', 'connection_priority': '1'}

#paydata_old={"SimData":{"sim_num":"1","apn":"FixedIP.nw","username":None,"password":None},"PriorData":{"connection_priority":3}}


#dict_ntp = response.json()[len(response.json())-1]
#print(type(response.json()[len(response.json())-1]))
{'id': 1, 'sim_num': '1', 'apn': 'FixedIP.nw', 'username': None, 'password': None, 'connection_priority': '1'}



chekc_gsm = requests.get(url_2+'/1', headers=head, timeout=10).json()
chekc_gsm['apn'] += '_test'
chekc_gsm['username'] += '_test'
chekc_gsm['password'] += '_test'
chekc_gsm['connection_priority'] = '3'
#new = response.json()

requests.put(url_2+'/1', headers=head, json=chekc_gsm, timeout=10) 
response_new = requests.get(url_2+'/1', headers=head, timeout=10).json()
print(chekc_gsm)
print(response_new)
print(chekc_gsm == response_new)

{'name': 'GeneralError', 'message': 'insert into "config_gsm" ("apn", "id", "password", "sim_num", "username") values ($1, $2, $3, $4, $5) returning "id" - duplicate key value violates unique constraint "config_gsm_pkey"', 'code': 500, 'className': 'general-error', 
'data': {}, 'errors': {}}