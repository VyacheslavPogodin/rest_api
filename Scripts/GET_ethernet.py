import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/confethernet/1'
conf_eth_new={'ip': '999.999.999.999',
                        'mask': '255.255.252.0', 'gateway': '10.10.31.255',
                        'dns_1': '10.10.30.1', 'dns_2': '10.10.30.2',
                        'mac': 'd0:03:eb:ee:26:dd', 'domain': 'nartis.ru',
                        'connection': 'static', 'source': 1}


response = requests.get(url_2, headers=head, timeout=10)
#dict_ntp = response.json()[len(response.json())-1]
#print(type(response.json()[len(response.json())-1]))


print(response.json())
print(response.url)

[{'id': 3, 
'ip': None, 
'mask': None, 
'gateway': None, 
'dns_1': None, 
'dns_2': None, 
'mac': None, 'domain': None, 
'connection': 'dhcp', 'source': 1}]
