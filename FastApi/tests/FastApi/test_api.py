import requests
import pytest
# Тест аутентификации пользователя.

list_users = [{"login":"Sidorov", "password" :"1234"},
              pytest.param({"login":"Begunow", "password" :"1234"},marks=pytest.mark.xfail), 
              pytest.param({"login":"Sidorov", "password" :"1234678"}, marks=pytest.mark.xfail),]

list_id_user = [('1', 200 , {'Сидоров': {'data_secret': [{'date_career_growth': '24.05.2024', 'salary': 12000}]}}),
                ('2', 403, {"detail": "You don't have access to this data."}),
                ('3', 403, {"detail": "You don't have access to this data."})]

# Тест аутентификации, 3 теста с верными данными и два с невеными (ожидаемое падение)
@pytest.mark.parametrize("payload", list_users)
def test_post_authentication(payload):        
        response = requests.post("http://localhost:8000/api/v1/login", json=payload)
        assert response.status_code == 200,                                              f"С адреса получен ответ на запрос сервера не соответствующий требуемому"
        assert response.headers['Content-Type'] == 'application/json',                   f"В заголовке ответа Content-Type с адреса  выставлен не ожидаемый тип передаваемого контента"
        assert list(response.json().keys())  == ['accessToken',],                        f"С адреса  в ответе список требуемых параметров не соответствует требуемому"             

# Тест запроса секретных данных с селективным доступом (аутентифицируется пользователь Sidorov и проверяется доступ ко всем данным)
@pytest.mark.parametrize("ID_USER, status_code, data_response", list_id_user)
def test_get_open_data(ID_USER, status_code, data_response):
        response_aut = requests.post("http://localhost:8000/api/v1/login", json={"login":"Sidorov", "password" :"1234"}).json()
        
        headers = {"Authorization": f"Bearer {response_aut['accessToken']}"}
        
        response_get = requests.get(f"http://localhost:8000/api/v1/employees_data/{ID_USER}", headers=headers, timeout=10)
        # assert response_aut.json()["accessToken"] == ''
        assert response_get.status_code == status_code,                               f"С адреса  получен ответ на запрос сервера не соответствующий требуемому"
        assert response_get.headers['Content-Type'] == 'application/json',            f"В заголовке ответа Content-Type с адреса выставлен не ожидаемый тип передаваемого контента"
        assert response_get.json() == data_response,                                  f"Неверные данные в ответе"
       
