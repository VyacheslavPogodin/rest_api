import requests
import pytest
from settings import url_form_in_ip

ansver_not_auth = {"name":"NotAuthenticated","message":"Not authenticated","code":401,"className":"not-authenticated","errors":{}}
# Тестовые функции проверка запросов без авторизации

class TestClassCheckPageGet:
    # тест страницы информация УСПД
    def test_get_devinfo_info_uspd(self):        
        key = "info_uspd"
        json_standard = [
        'name', 'modification', 'serial', 'address', 'metrocom', 'md5mm', 'id', 'logs'
        ]
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 200,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
        assert list(response.json().keys()) == json_standard,                                       f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"


    # Проверка запросов на страницу конфигурирования УСПД без авторизации    
    def test_get_confmode_info_configure_not_auth(self):        
        key = 'configyre'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запросов на страницу времени УСПД без авторизации
    def test_get_currenttime_not_auth(self):    
        key = 'time'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запросов текущей временной зоны УСПД без авторизации
    def test_get_zonetime_not_auth(self):    
        key = 'time_zone'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запроса списка серверов обновления времени УСПД без авторизации
    def test_get_ntpservers_not_auth(self):    
        key = 'ntp_serv'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запроса интерфейсов ПУ установленных в УСПД без авторизации
    def test_get_interfaces_not_auth(self):    
        key = 'interfaces'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запроса настроек интерфейса RS-485 установленного в УСПД без авторизации
    def test_get_RS_not_auth(self):    
        key = 'rs-485'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Проверка запроса настроек интерфейса Интернет установленного в УСПД без авторизации
    def test_get_eth_not_auth(self):    
        key = 'eth'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"


    # Проверка запроса настроек интерфейса GSM №1 установленного в УСПД без авторизации
    def test_get_gsm_1_not_auth(self):    
        key = 'gsm_1'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"
    
    # Проверка запроса настроек интерфейса GSM №1 установленного в УСПД без авторизации
    def test_get_gsm_2_not_auth(self):    
        key = 'gsm_2'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Журнал сухих контактов
    def test_get_journal_discret_not_auth(self):    
        key = 'discretejournal'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Журнал коррекции времени
    def test_get_timesynq_not_auth(self):    
        key = 'timesynq'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"

    # Журнал перехода на резервное питание
    def test_get_powerjournal_not_auth(self):    
        key = 'powerjournal'
        response = requests.get(url_form_in_ip(key), timeout=10)
        assert response.status_code == 401,                                                         f"С адреса {response.url} получен ответ на запрос сервера не соответствующий требуемому"
        assert response.json() == ansver_not_auth,                                                  f"С адреса {response.url} ответ от сервера не соответствует требуемому, при данном запросе"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8',               f"В заголовке ответа Content-Type с адреса {response.url} выставлен не ожидаемый тип передаваемого контента"
        assert int(response.headers['Content-Length']) == len(response.content),                    f"Объем передаваемого контената с адреса {response.url} не соответствует указанному в заголовке Content-Length"