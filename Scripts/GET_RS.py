import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/rsconfig/1'

data_new = {'timeout': 99}

#response = requests.put(url_2, headers=head, json=data_new, timeout=10)
res_get = requests.get(url_2, headers=head, timeout=10).json()

#dict_ntp = response.json()[len(response.json())-1]
#print(type(response.json()[len(response.json())-1]))
#del res_get['id'], res_get['res_port']
print(res_get)
print(res_get.json == {'id': 1, 'baud': 1234, 'parity': 2,
                                    'data_bits': 16, 'stop_bits': 2, 'interface_id': 1})


{'rsData': 
            [{'id': 1, 'baud': 9600, 'parity': 5, 'data_bits': 8, 'stop_bits': 1, 'interface_id': 1, 'res_port': '/dev/ttyS4', 'res_name': '485_BUS_1', 'parity_name': 'none'}],
'parityData': 
            [{'id': 1, 'parity': 'even'}, {'id': 2, 'parity': 'odd'}, {'id': 3, 'parity': 'space'}, {'id': 4, 'parity': 'marker'}, {'id': 5, 'parity': 'none'}]}

