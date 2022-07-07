import requests
from datetime import datetime
import json, os
from GET_aut import authentication_token

name_file = authentication_token()

with open(name_file) as json_file:
    data_head = json.load(json_file)

head_new = {'Authorization': data_head['accessToken']}

with open('accessToken/2022-04-01 17-57-40.json') as json_file:
    data_head = json.load(json_file)

head_dell = {'Authorization': data_head['accessToken']}
{'Accept': 'application/json', 'Content-Type': 'application/json; charset=utf-8'}

r_dell = requests.delete('http://10.10.29.110/api/v1/authentication/729f0167-cd43-4425-a791-154b5d3e0c44')


url_2 = 'http://10.10.29.110/api/v1/currenttime'

r = requests.get(url_2, headers=head_new)

print(r_dell.json())

print(r.json())

#auth=HTTPBasicAuth(toggl_token, 'api_token')
# 
# )
#print(r_get.json())
#r = requests.get(url_2, headers=head)

#print(r.text)
#print(r.json()['time'][11:15])
#print(str(datetime.now())[11:15])
#print(r.json()['time'][:10] == str(datetime.now())[:10])
#print(r.json()['time'][11:15] == str(datetime.now())[11:15])

{'Server': 'nginx/1.10.3', 'Date': 'Fri, 01 Apr 2022 06:14:50 GMT',
'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '144',
'Connection': 'keep-alive', 'X-DNS-Prefetch-Control': 'off', 'Expect-CT': 'max-age=0',
'X-Frame-Options': 'SAMEORIGIN', 'Strict-Transport-Security': 'max-age=15552000; includeSubDomains',
'X-Download-Options': 'noopen', 'X-Content-Type-Options': 'nosniff',
'X-Permitted-Cross-Domain-Policies': 'none', 'Referrer-Policy': 'no-referrer',
'X-XSS-Protection': '0', 'Access-Control-Allow-Origin': '*', 'Allow': 'POST,DELETE',
'ETag': 'W/"90-2Z9bfE3fgl9NlGUFTSnsXQ2gx3g"', 'Vary': 'Accept-Encoding'}




{'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJpYXQiOjE2NDg3OTQ0NzIsImV4cCI6MTY0ODg4MDg3MiwiYXVkIjoibG9jYWxob3N0IiwiaXNzIjoiZmVhdGhlcnMiLCJzdWIiOiIxIiwianRpIjoiZmI3YmUwZTItN2NmZC00MGY0LTk1NjUtMDk0NWNjMjY3NWI2In0.Dwkklp01qvExM8tVHnXdxWjtKWDr1hsbWB_Wu5bwGY4',
'authentication': {'strategy': 'jwt',
'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJpYXQiOjE2NDg3OTQ0NzIsImV4cCI6MTY0ODg4MDg3MiwiYXVkIjoibG9jYWxob3N0IiwiaXNzIjoiZmVhdGhlcnMiLCJzdWIiOiIxIiwianRpIjoiZmI3YmUwZTItN2NmZC00MGY0LTk1NjUtMDk0NWNjMjY3NWI2In0.Dwkklp01qvExM8tVHnXdxWjtKWDr1hsbWB_Wu5bwGY4',
'payload': {'iat': 1648794472, 'exp': 1648880872, 'aud': 'localhost', 'iss': 'feathers',
'sub': '1', 'jti': 'fb7be0e2-7cfd-40f4-9565-0945cc2675b6'}},
'role': {'id': 1, 'login': 'user_admin', 'role_name': 'user'}}

#1;"user_admin";"user";"$2a$10$GvAVX3vr9V5yr.gx6M8b9.9lQP5jpyPx9LRhtK9iWm7KW5juQOMlO"