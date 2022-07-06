from email import message
from urllib import response
import requests
import pytest
from settings import url_form_in_ip



class TestClassNegativeMetod:

    # Отправка на страницу /api/v1/devinterfaces не предусмотренных запросов
    def test_get_interfaces_with_auth(self, form_head_for_get_auth):    
        key = 'interfaces'
        data_new = {'resource_name': 'Test', 'flag': False, 'port': 'Test', 'timeout': 100000}
        
        res_post = requests.post(url_form_in_ip(key), headers=form_head_for_get_auth, data=data_new, timeout=10)
        res_post_num1 = requests.post(url_form_in_ip(key)+'/1', headers=form_head_for_get_auth, data=data_new, timeout=10)
        res_put = requests.put(url_form_in_ip(key), headers=form_head_for_get_auth, json=data_new, timeout=10)
        res_put_num1 = requests.put(url_form_in_ip(key)+'/1', headers=form_head_for_get_auth, json=data_new, timeout=10)
        res_del = requests.delete(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        res_del_num1 = requests.delete(url_form_in_ip(key)+'/1', headers=form_head_for_get_auth, timeout=10)
        

        assert res_post.json()['code'] == 405, "Метод не должен поддерживаться на донной странице"
        assert res_post_num1.json()['code'] == 404, "Метод не должен поддерживаться на донной странице"   
        assert res_put.json()['code'] == 405, "Метод не должен поддерживаться на донной странице"
        assert res_put_num1.json()['code'] == 405, "Метод не должен поддерживаться на донной странице"
        assert res_del.json()['code'] == 405, "Метод не должен поддерживаться на донной странице"
        assert res_del_num1.json()['code'] == 405, "Метод не должен поддерживаться на донной странице"