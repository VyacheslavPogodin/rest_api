"""Define some fixtures to use in the project."""

import pytest
import requests
from settings import url_form_in_ip
from datetime import datetime
import os, json
from py.xml import html

# запрос аутентификации для генерации токена
@pytest.fixture(scope='session')
def form_head_for_get_auth():
    payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}
    Token_r = requests.post(url_form_in_ip('auth'), data=payload).json()
    head = {'Authorization': Token_r['accessToken']}
    # Если нет то создаем дерикторию
    
    if not os.path.exists('accessToken'):
        os.makedirs('accessToken')

    #Сохраняем токен в файле
    with open('accessToken/'+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+".txt", 'w') as outfile:
        json.dump(Token_r, outfile)
    return head

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/'+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+".html"


#@pytest.fixture(autouse=True, scope='session')
#def my_fixture(form_head_for_get_auth):
    #setup
#    yield
    # teardown_stuff