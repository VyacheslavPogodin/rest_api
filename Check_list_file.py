import requests
from datetime import datetime, timedelta
import json, os
from GET_aut import authentication_token


#files = os.listdir('accessToken')
#rint(files[-1])
#print((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H-%M-%S")+".json")
#print(files[-1]>(datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H-%M-%S")+".json")
#name_file = authentication_token()
#with open(name_file) as json_file:
#    data_head = json.load(json_file)
#head = {'Authorization': data_head['accessToken']}
#print(head)
print(datetime.utcfromtimestamp(1649057289).strftime('%Y-%m-%d %H:%M:%S'))