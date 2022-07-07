import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r.json()
head = {'Authorization': Token_r['accessToken']}
url_2 = 'http://10.10.29.110/api/v1/ntpservers'




list_ntpservices = [{"host": "ntp2.vniiftri.ru","port": 123},
        {"host": "ntp3.vniiftri.ru","port": 123},
        {"host": "ntp4.vniiftri.ru","port": 123},
        {"host": "ntp21.vniiftri.ru","port": 123},
        {"host": "ntp1.niiftri.irkutsk.ru","port": 123},
        {"host": "ntp2.niiftri.irkutsk.ru","port": 123},
        {"host": "vniiftri.khv.ru","port": 123},
        {"host": "ntp1.vniiftri.ru ","port": 123}]

for payload in list_ntpservices:
        r = requests.post(url_2, headers=head, data=payload)

r1 = requests.get(url_2, headers=head)
print(len(r1.json()))
