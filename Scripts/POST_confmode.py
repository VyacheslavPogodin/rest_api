import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/confmode'



payload_2 =  {'mode':'conf_out'}
#response = requests.get(url_2, headers=head, timeout=10)
#status_conf = response.json()['data']['status_id']
cheng_status_conf = requests.post(url_2, headers=head, data=payload_2)
response = requests.get(url_2, headers=head, timeout=10)

print(type(cheng_status_conf.json().keys()))
print(cheng_status_conf.json().keys() == (['confChanged']))

#print(response.json().keys())
#print(response.json()['data'])
#print(response.json()['mod_id'])
#print(response.json()['statuses'])

#print(type(len(r.content)))

#print(int(r.headers['Content-Length']) == len(r.content))

otvet_standart = {
    "data": 
    {"id": 18785,
    "module_id": 7,
    "time":"2020-11-30 09:01:33.469783",
    "status_id": 5,
    "status_name": "conf_out"},
    "statuses":[
        {"id": 4,
        "description": "conf_in"
        },{"id": 5,
        "description": "conf_out"
        }]}

otvet_fact = {
    "data":
    {"id":89171,
    "module_id":7,
    "time":"2022-03-24 12:37:20.63992",
    "status_id":5,
    "status_name":"conf_out"},
    "mod_id":7,
    "statuses":[
        {"id":4,
        "description":"conf_in"},
        {"id":5,
        "description":"conf_out"}]}

#print(type(r1.json()), type(d), type(d2))
#print(r.json()['statuses'] == otvet_standart['statuses'], r.json()['statuses'] == otvet_fact['statuses'])


#url = 'website.com/id' 
 
#res=requests.get(url, headers=head) 

#r_dict = r.json()

#print(r_dict['role'])
#print(type(r.text))
