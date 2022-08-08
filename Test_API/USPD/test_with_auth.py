import requests
import pytest
from settings import url_form_in_ip


# Тестовые функции

def test_get_authentication_201():        
        key = "auth"
        payload =  {"strategy": "local", "login": "user_admin", "password": "admin123"}
        response = requests.post(url_form_in_ip(key), data=payload)
                
        assert response.status_code == 201,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys())  == ['accessToken', 'authentication', 'role'],                                              f"С адреса {response.url} в ответе список требуемых параметров не соответствует требуемому"             
        assert response.json()['role'] == {"id":1, 'login':"user_admin",  "role_name":"user"},                                          f"С адреса {response.url} при аутентификации пользователя присвоена не соответствующая роль"




class TestClassCheckPageGet:

    # Проверка запросов на страницу конфигурирования УСПД с авторизацией
    def test_get_confmode_info_configure_with_auth(self, form_head_for_get_auth):        
        key = "configyre"
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys())  == ['data','statuses']
        assert list(response.json()['data'].keys())  == ['id', 'module_id', 'time', 'status_id', 'status_name']
        assert isinstance(response.json()['data']['id'], int)
        assert response.json()['data']['module_id'] == 7
        assert response.json()['statuses'] == [{"id":4,"description":"conf_in"},{"id":5,"description":"conf_out"}]



    # Проверка запросов времени с авторизацией
    def test_get_currenttime_with_auth(self, form_head_for_get_auth):        
        from datetime import datetime
        key = "time"
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert response.json()['error'] == ""




    # Проверка запросов текущей временной зоны УСПД с авторизацией
    def test_get_zonetime_with_auth(self, form_head_for_get_auth):    
        key = 'time_zone'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['timezone']
        assert  isinstance(response.json()['timezone'], int)




    # Проверка запроса интерфейсов ПУ установленных в УСПД с авторизацией
    def test_get_interfaces_with_auth(self, form_head_for_get_auth):    
        key = 'interfaces'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json() == []:
            pytest.skip("Интерфейсы ПУ в УСПД не настроены")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json()[0].keys()) == ['id', 'resource_name', 'flag', 'port']

        


    # Проверка запроса настроек интерфейса RS-485 установленного в УСПД без авторизации
    def test_get_RS_with_auth(self, form_head_for_get_auth):    
        key = 'rs-485'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert isinstance(response.json()['rsData'], list)
        assert response.json()['rsData'] != [],                                                                                         "В приборе УСПД не настроен ни один интерфейс RS-485 "
        assert response.json()['parityData'] == [{'id': 1, 'parity': 'even'},
                                                {'id': 2, 'parity': 'odd'},
                                                {'id': 3, 'parity': 'space'},
                                                {'id': 4, 'parity': 'marker'},
                                                {'id': 5, 'parity': 'none'}]
        
        



        # Проверка запроса настроек интерфейса Интернет установленного в УСПД с авторизацией
    def test_get_eth_with_auth(self, form_head_for_get_auth):    
        key = 'eth'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json() == []:
            pytest.skip("интерфейс IP в УСПД не настроен")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert isinstance(response.json(), list)



    # Журнал сухих контактов
    def test_get_journal_discret_with_auth(self, form_head_for_get_auth):    
        key = 'discretejournal'
        response = requests.get(url_form_in_ip(key),headers=form_head_for_get_auth, timeout=10)
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert response.headers['Content-Encoding'] == 'gzip',                                                                          f"Кодировка передаваемого контената с адреса {response.url} не соответствует ожидаемой"
        assert isinstance(response.json(), list),                                                                                       f"С адреса {response.url} получаем полное говно"




    # Журнал коррекции времени
    def test_get_timesynq_with_auth(self, form_head_for_get_auth):    
        key = 'timesynq'
        response = requests.get(url_form_in_ip(key),headers=form_head_for_get_auth, timeout=10)
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert response.headers['Content-Encoding'] == 'gzip',                                                                          f"Кодировка передаваемого контената с адреса {response.url} не соответствует ожидаемой"
        assert isinstance(response.json(), list),                                                                                       f"С адреса {response.url} получаем полное говно"




    # Журнал перехода на резервное питание
    def test_get_powerjournal_with_auth(self, form_head_for_get_auth):    
        key = 'powerjournal'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert response.headers['Content-Encoding'] == 'gzip',                                                                          f"Кодировка передаваемого контената с адреса {response.url} не соответствует ожидаемой"
        assert isinstance(response.json(), list),                                                                                       f"С адреса {response.url} получаем полное говно"



class TestClassChengeConfigureStatus:

   

    # Проверка запроса на включение конфигурирования УСПД с авторизацией
    def test_post_confmode_configure_on_with_auth(self, form_head_for_get_auth):        
        key = "configyre"
        payload = {'mode':'conf_in'}
        
        # Проверка статуса режима конфигуратора УСПД
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json()['data']['status_id'] == 4:
            pytest.exit("Перед началом тестирования необходимо перевести конфигурирование УСПД в режим ОТКЛ")

        change_status_conf = requests.post(url_form_in_ip(key), headers=form_head_for_get_auth, data=payload)
        check_status = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
                
        assert change_status_conf.status_code == 201,                                                                                   f"С адреса {change_status_conf.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert change_status_conf.json() == {"confChanged":True}
        assert check_status.json()['data']['status_id']  == 4
        assert change_status_conf.headers['Content-Type'] == 'application/json; charset=utf-8',                                         f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(change_status_conf.headers['Content-Length']) == len(change_status_conf.content),                                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запроса на выключение конфигурирования УСПД с авторизацией
    def test_post_confmode_configure_off_with_auth(self, form_head_for_get_auth):        
        key = "configyre"
        payload = {'mode':'conf_out'}
        change_status_conf = requests.post(url_form_in_ip(key), headers=form_head_for_get_auth, data=payload)
        check_status = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        
    # Проверка статуса режима конфигуратора УСПД
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json()['data']['status_id'] == 4:
            pytest.exit("Перед началом тестирования необходимо перевести конфигурирование УСПД в режим ОТКЛ")

        assert change_status_conf.status_code == 201,                                                                                   f"С адреса {change_status_conf.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert change_status_conf.json() == {"confChanged":True}
        assert check_status.json()['data']['status_id']  == 5
        assert change_status_conf.headers['Content-Type'] == 'application/json; charset=utf-8',                                         f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(change_status_conf.headers['Content-Length']) == len(change_status_conf.content),                                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"



# Проверка работы запросов с NTP-services
class TestClassChangesNtpServers:

    # Проверка запроса списка серверов обновления времени УСПД с авторизацией
    def test_get_ntpserver_with_auth(self, form_head_for_get_auth):
        key = 'ntp_serv'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json() == []:
            pytest.skip("Сервера NTP в УСПД не настроены, перед началом тестирования необходимо настроить УСПД")        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert isinstance(response.json(), list),                                                                                       f"Передаваемый контент с адреса {response.url} не является списком NTP-servers"
        assert list(response.json()[0].keys()) == ['id','host','port']



    def test_post_add_ntpserver_with_auth(self, form_head_for_get_auth):
        key = 'ntp_serv'
        payload = {'host':'ntp_test_add','port':129}

        check_ntp_old = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        add_ntp_server = requests.post(url_form_in_ip(key), headers=form_head_for_get_auth, data=payload)
        check_ntp_new = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        
        # проверка на наличие тестового сервера в базе, иначе отмена тестирования
        if len(check_ntp_new) - len(check_ntp_old) != 1:
            pytest.exit("Ошибка создания тестового ntp-сервераб тестовый сервер не добавлен БД , критический баг")   
        
        assert add_ntp_server.status_code == 201,                                                                                       f"С адреса {add_ntp_server.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert add_ntp_server.headers['Content-Type'] == 'application/json; charset=utf-8',                                             f"В заголовке ответа Content-Type с адреса {add_ntp_server.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(add_ntp_server.headers['Content-Length']) == len(add_ntp_server.content),                                            f"Объем передаваемого контената с адреса {add_ntp_server.url} не соответствует указанному в заголовке Content-Length"
        assert isinstance(check_ntp_new[-1]['id'], int),                                                                                f"Текущий адреса {add_ntp_server.url}. Присвоенный ID не соответствует типу int"
        assert check_ntp_new[-1]['host'] == 'ntp_test_add',                                                                             f"Текущий адреса {add_ntp_server.url}. Полученное имя 'host' от сервера не равно тестовому имени 'host' 'ntp_test_add'"
        assert check_ntp_new[-1]['port'] == 129,                                                                                        f"Текущий адреса {add_ntp_server.url}. Полученное значение 'port' от сервера не равно тестовому значению 'port' 'ntp_test_add'"




    def test_put_update_ntpserver_with_auth(self, form_head_for_get_auth):
        key = 'ntp_serv'
        payload = {'host':'ntp_test_update','port':921}
        
        check_ntp_old = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        update_ntp_server = requests.put(url_form_in_ip(key)+'/'+str(check_ntp_old[-1]['id']), headers=form_head_for_get_auth, json=payload)        
        check_ntp_new = requests.get(url_form_in_ip(key)+'/'+str(check_ntp_old[-1]['id']), headers=form_head_for_get_auth, timeout=10).json()
        
        assert update_ntp_server.status_code == 200,                                                                                    f"С адреса {update_ntp_server.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert update_ntp_server.headers['Content-Type'] == 'application/json; charset=utf-8',                                          f"В заголовке ответа Content-Type с адреса {update_ntp_server.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(update_ntp_server.headers['Content-Length']) == len(update_ntp_server.content),                                      f"Объем передаваемого контената с адреса {update_ntp_server.url} не соответствует указанному в заголовке Content-Length"
        assert check_ntp_new['id'] == check_ntp_old[-1]['id']
        assert check_ntp_new['host'] == 'ntp_test_update'
        assert check_ntp_new['port'] == 921




    def test_delete_del_ntpserver_with_auth(self, form_head_for_get_auth):
        key = 'ntp_serv'

        check_ntp_old = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        update_ntp_server = requests.delete(url_form_in_ip(key)+'/'+str(check_ntp_old[-1]['id']), headers=form_head_for_get_auth, timeout=10)        
        check_ntp_new = requests.get(url_form_in_ip(key)+'/'+str(check_ntp_old[-1]['id']), headers=form_head_for_get_auth, timeout=10).json()

        url_check = update_ntp_server.url[19:]
        
        assert update_ntp_server.status_code == 200,                                                                                    f"С адреса {update_ntp_server.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert update_ntp_server.headers['Content-Type'] == 'application/json; charset=utf-8',                                          f"В заголовке ответа Content-Type с адреса {update_ntp_server.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(update_ntp_server.headers['Content-Length']) == len(update_ntp_server.content),                                      f"Объем передаваемого контената с адреса {update_ntp_server.url} не соответствует указанному в заголовке Content-Length"
        assert check_ntp_new == {'name': 'NotFound',
                                'message': 'Page not found',
                                'code': 404,
                                'className': 'not-found',
                                'data': {'url': url_check}, 'errors': {}}


# Тестирование интерфейса GSM
class TestClassGSMConfig:

    # Проверка запроса настроек интерфейса GSM №1 установленного в УСПД без авторизации
    def test_get_gsm_1_with_auth(self, form_head_for_get_auth):    
        key = 'gsm_1'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json() == {}:
            pytest.skip("В УСПД не настроены параметры GSM №1, перед началом тестирования необходимо настроить УСПД")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['id', 'sim_num', 'apn', 'username', 'password', 'connection_priority']
        
    
    
    # Проверка запроса на изменение настроек интерфейса GSM №1 установленных в УСПД с авторизацией
    def test_put_gsm_1_with_auth(self, form_head_for_get_auth):    
        key = 'gsm_1'
        check_gsm = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        conf_gsm_new={'sim_num': '1',
                        'apn': 'Test.spb', 'username': 'test123',
                        'password': 'Test1#$', 'connection_priority': '1'}
        response = requests.put(url_form_in_ip(key), headers=form_head_for_get_auth, json=conf_gsm_new, timeout=10)
        res_get = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        conf_gsm_new['id'] = 1

        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        
        assert res_get.json() == conf_gsm_new
    
    
    
    
 # Проверка запроса настроек интерфейса GSM №1 установленного в УСПД без авторизации
    def test_get_gsm_2_with_auth(self, form_head_for_get_auth):    
        key = 'gsm_2'
        response = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        if response.json() == {}:
            pytest.skip("В УСПД не настроены параметры GSM №2, перед началом тестирования необходимо настроить УСПД")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['id', 'sim_num', 'apn', 'username', 'password', 'connection_priority']
        
    
    
    # Проверка запроса на изменение настроек интерфейса GSM №1 установленных в УСПД с авторизацией
    def test_put_gsm_2_with_auth(self, form_head_for_get_auth):    
        key = 'gsm_2'
        check_gsm = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10).json()
        conf_gsm_new={'sim_num': '2',
                        'apn': 'Test.spb', 'username': 'test123',
                        'password': 'Test1#$', 'connection_priority': '2'}
        response = requests.put(url_form_in_ip(key), headers=form_head_for_get_auth, json=conf_gsm_new, timeout=10)
        res_get = requests.get(url_form_in_ip(key), headers=form_head_for_get_auth, timeout=10)
        conf_gsm_new['id'] = 2
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        
        assert res_get.json() == conf_gsm_new




class TestClassEthConfig:

    # Проверка запроса настроек интерфейса Интернет установленного в УСПД с авторизацией
    def test_get_eth_1_with_auth(self, form_head_for_get_auth):    
        url = url_form_in_ip('eth')+'/1'
        response = requests.get(url, headers=form_head_for_get_auth, timeout=10)
        if response.json() == {'name': 'NotFound', 'message': 'Page not found',
                                'code': 404, 'className': 'not-found',
                                'data': {'url': '/api/v1/confethernet/3'}, 'errors': {}}:
            pytest.skip("интерфейс eth1 в УСПД не установлен")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['id','ip','mask','gateway','dns_1',
                                                    'dns_2','mac','domain','connection','source']



# Проверка запроса настроек интерфейса Интернет установленного в УСПД с авторизацией
    def test_get_eth_2_with_auth(self, form_head_for_get_auth):    
        url = url_form_in_ip('eth')+'/2'
        response = requests.get(url, headers=form_head_for_get_auth, timeout=10)
        if response.json() == {'name': 'NotFound', 'message': 'Page not found',
                                'code': 404, 'className': 'not-found',
                                'data': {'url': '/api/v1/confethernet/3'}, 'errors': {}}:
            pytest.skip("интерфейс eth1 в УСПД не установлен")
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['id','ip','mask','gateway','dns_1',
                                                    'dns_2','mac','domain','connection','source']



    # Проверка запроса на изменение настроек Еthernet установленных в УСПД с авторизацией 
    # (поскольку при тестировании идет подключение по Eth1 тестировать на изменение будем только Eth2)
    def test_put_eth_2_with_auth(self, form_head_for_get_auth):    
        url = url_form_in_ip('eth')+'/2'
        check_eth = requests.get(url, headers=form_head_for_get_auth, timeout=10).json()
        conf_eth_new={'ip': '999.999.999.999',
                        'mask': '255.255.252.0', 'gateway': '10.10.31.255',
                        'dns_1': '10.10.30.1', 'dns_2': '10.10.30.2',
                        'mac': 'd0:03:eb:ee:26:dd', 'domain': 'nartis.ru',
                        'connection': 'static', 'source': 1}
        
        response = requests.put(url, headers=form_head_for_get_auth, json=conf_eth_new, timeout=10)
        #response = requests.get(url, headers=form_head_for_get_auth, timeout=10)
        conf_eth_new['id'] = 2
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        
        assert response.json() == [conf_eth_new]




class TestClassRSConfig:

    # Проверка запроса настроек интерфейса RS-485 установленного в УСПД без авторизации
    def test_get_RS_with_auth(self, form_head_for_get_auth):    
        key = 'rs-485'
        url = url_form_in_ip(key)+'/1'

        response = requests.get(url, headers=form_head_for_get_auth, timeout=10)
        
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == ['id', 'baud','parity','data_bits','stop_bits','interface_id','res_port'],               "Полученный список параметров интерфейса RS-485 от прибора УСПД не соответствует требуемому"
        
    
    
    # Проверка запроса настроек интерфейса RS-485 установленного в УСПД без авторизации
    def test_put_RS_1_with_auth(self, form_head_for_get_auth):    
        key = 'rs-485'
        url = url_form_in_ip(key)+'/1'
               
        rs_conf_new = {'baud': 1234, 'parity': 2,
                        'data_bits': 16, 'stop_bits': 2,
                        'interface_id': 1}
        
        response = requests.put(url, headers=form_head_for_get_auth, json=rs_conf_new, timeout=10)
        res_get = requests.get(url, headers=form_head_for_get_auth, timeout=10).json()
            
        
        assert response.status_code == 200,                                                                                             f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',                                                   f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                                                        f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert response.json() == [{'id': 1, 'baud': 1234, 'parity': 2,
                                    'data_bits': 16, 'stop_bits': 2, 'interface_id': 1}]
        
        assert res_get == {'id': 1, 'baud': 1234, 'parity': 2,
                            'data_bits': 16, 'stop_bits': 2, 'interface_id': 1,
                            'res_port': '/dev/ttyS4'}

