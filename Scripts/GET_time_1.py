import requests
from datetime import datetime


payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/currenttime'

r = requests.get(url_2, headers=head)

print(r.text)
print(r.json()['time'][11:15])
print(str(datetime.now())[11:15])
print(r.json()['time'][:10] == str(datetime.now())[:10])
print(r.json()['time'][11:15] == str(datetime.now())[11:15])

