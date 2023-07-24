from fastapi import FastAPI, Body, Depends

from app.model import UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

 
app = FastAPI()

# База данных пользователей
#Список с id и ФИО
list_of_employees = [   {'id':1, 'name':'Сидоров'},
                        {'id':2,'name':'Иванов'}
                        ]
#Словарь с ключами id и данными пользователей для защиты
data_of_employees = {   1 : {'data_secret': [{'salary':12000, 'date_career_growth':'24.05.2024'}]}, 
                        2 : {'data_secret': [{'salary':50000, 'date_career_growth':'31.02.2024'}]}
                        }
#Список с данными регистрации пользователей
list_login_pass = [{'login':'Sidorov', 'password' :'1234'}, 
                   {'login':'Ivanov', 'password' :'4321'}
                    ]
#Словарь соответствия логинов id пользователей
list_id_users = {'Sidorov': '1', 'Ivanov': '2'}

# Стартовая страница
@app.get("/api/v1/")
async def start():
    return {'message': 'Welcome to work!'}

# Получение списка сотрудников с открытыми данными
@app.get("/api/v1/employees")
async def all_empl():
    return {'data': list_of_employees}

# Страница по каждому сотруднику с данными доступными только для аутентифицированных пользователей
@app.get("/api/v1/employees/{user_id}", dependencies=[Depends(JWTBearer(False))])
async def singl_empl(user_id):
    id=int(user_id)
    if id > len(list_of_employees):
        return {'error': 'No employee with this ID was found.'}
    for empl in list_of_employees:
        if empl['id'] == id:
            return empl

#Страница защищенных данных (доступ по токену для каждого сотрудника только к своим данным)
@app.get("/api/v1/employees_data/{user_id}", dependencies=[Depends(JWTBearer(True))])
async def singl_empl_secret(user_id):
    id=int(user_id)
    for empl in list_of_employees:
        if empl['id'] == id:
            return {empl['name'] : data_of_employees[id]}



# Проверка на наличие работника в базе
def check_user(data: UserLoginSchema):
    for user in list_login_pass:
        if user['login'] == data.login and user['password'] == data.password:
            return True
    return False

# Аутентификация по логину и паролю
@app.post("/api/v1/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        for user_data_aut in list_login_pass:
            if user_data_aut['login'] == user.login:
                return signJWT(list_id_users[user.login], user.login )
    return {
        "error": "Wrong login or password details!"
    }
