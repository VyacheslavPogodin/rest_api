import json
import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/devinterfaces/6'

data_new = {'resource_name': 'Test', 'flag': False, 'port': 'Test', 'timeout': 100000}

response = requests.get(url_2, headers=head, timeout=10)
#response = requests.put(url_2, headers=head, data=data_new, timeout=10)


#dict_ntp = response.json()[len(response.json())-1]
#print(type(response.json()[len(response.json())-1]))


print(response.headers)

[{'id': 11, 'resource_name': 'TEST', 'flag': True, 'port': '/dev/test', 'timeout': 120},
{'id': 13, 'resource_name': 'TEST_485', 'flag': True, 'port': '/dev/tty88', 'timeout': 123},
{'id': 12, 'resource_name': 'SPODUS', 'flag': True, 'port': '4052', 'timeout': 1800},
{'id': 2, 'resource_name': 'ZIG_BEE', 'flag': True, 'port': '/dev/ttyS1', 'timeout': 1800},
{'id': 16, 'resource_name': '485_BUS_2', 'flag': True, 'port': '/dev/ttyS4', 'timeout': 300},
{'id': 17, 'resource_name': '485_BUS_3', 'flag': True, 'port': '/dev/ttyS4', 'timeout': 300},
{'id': 18, 'resource_name': '485_BUS_4', 'flag': True, 'port': '/dev/ttyS4', 'timeout': 300},
{'id': 1, 'resource_name': '485_BUS_1', 'flag': True, 'port': '/dev/ttyS4', 'timeout': 300}]

#Ответ на метод не приминим
{'name': 'MethodNotAllowed', 'message': 'Method `create` is not supported by this endpoint.', 'code': 405, 'className': 'method-not-allowed', 'errors': {}}


{'Server': 'nginx/1.10.3', 'Date': 'Thu, 31 Mar 2022 12:45:08 GMT',
'Content-Type': 'application/json; charset=utf-8',
'Content-Length': '134', 'Connection': 'keep-alive',
'X-DNS-Prefetch-Control': 'off', 'Expect-CT': 'max-age=0', 'X-Frame-Options': 'SAMEORIGIN', 
'Strict-Transport-Security': 'max-age=15552000; includeSubDomains',
'X-Download-Options': 'noopen', 'X-Content-Type-Options': 'nosniff',
'X-Permitted-Cross-Domain-Policies': 'none', 'Referrer-Policy': 'no-referrer',
'X-XSS-Protection': '0', 'Access-Control-Allow-Origin': '*', 'Allow': 'GET',
'ETag': 'W/"86-5eXaBMsyL87XD8HaoY7q9J3lxZ4"', 'Vary': 'Accept-Encoding'}