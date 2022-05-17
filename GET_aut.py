import requests
from datetime import datetime, timedelta
import json, os


def authentication_token(ip='10.10.29.110'):

    payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

# Если нет то создаем дерикторию    
    if not os.path.exists('accessToken'):
        os.makedirs('accessToken')    
    
# Проверяем наличие файлов токенов и дату создания (должно быть не старше суток)     
    files = os.listdir('accessToken')
    
    
    if files !=[] and files[-1] > (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H-%M-%S")+".json":
        
        name_files_token = 'accessToken/'+files[-1]
        
            
    else:  
        
        r_auth =  requests.post('http://'+ip+'/api/v1/authentication', data=payload)
        Token_r = r_auth.json()
    
#Сохраняем токен в файле
        name_files_token = 'accessToken/'+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+".json"
        with open(name_files_token, 'w') as outfile:
            json.dump(Token_r, outfile)

    return name_files_token