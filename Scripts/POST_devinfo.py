import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r.json()
print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/devinfo'

r = requests.get(url_2, headers=head)

print(type(int(r.headers['Content-Length'])))
print(type(len(r.content)))

print(int(r.headers['Content-Length']) == len(r.content))


d = {
"name": "УСПД ШЛ-ZB-L",
"modification": "01D.GE2U2.ZR2.I6по",
"serial": "180220200004",
"address": "Арсенальная ул., 1, корп.2",
"metrocom": "MetroCom v.2.1.5",
"md5mm": "2e7a65e869b7ac747dc29567e1f8183b",
"id": 1,
"password": True
}

d2 = {
'name': 'УСПД ШЛ-ZB-L',
'modification': '01D.GE2U2.ZR2.I6по',
'serial': '180220200004',
'address': 'Арсенальная ул., 1, корп.2',
'metrocom': 'MetroCom v.2.1.5',
'md5mm': '2e7a65e869b7ac747dc29567e1f8183b',
'id': 1,
'logs': True
}

#print(type(r1.json()), type(d), type(d2))
print(r.json() == d, r.json() == d2)


#url = 'website.com/id' 
 
#res=requests.get(url, headers=head) 

#r_dict = r.json()

#print(r_dict['role'])
#print(type(r.text))
