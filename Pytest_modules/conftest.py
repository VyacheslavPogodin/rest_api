"""Define some fixtures to use in the project."""

import psycopg2
from psycopg2 import OperationalError
from datetime import datetime
import os, pytest
from py.xml import html
from time import sleep




# запрос аутентификации для генерации токена
@pytest.fixture()
def create_connection():
    
    connection = None
    desp_bd = {
    'db_name':'uspd',
    'db_user':'admin',
    'db_password':'kPZa83Uz2#0',
    'db_host':'localhost',
    'db_port':'5432'}
    try:
        connection = psycopg2.connect(
            database=desp_bd['db_name'],
            user=desp_bd['db_user'],
            password=desp_bd['db_password'],
            host=desp_bd['db_host'],
            port=desp_bd['db_port'],
        )
        #print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    
    yield connection
    
    connection.close()

@pytest.fixture(scope='class')
def modul_id_return():
    modul_id = {
        'time': 1,
        'genopt_generator':2,
        'myrmidon_parser':3,
        'zig_bee':4,
        'spodes':5,
        'hunter':6,
        'web':7,
        'transp':8,
        'spi_io':9,
        'start':10,
        'internet':11,
        'zeus':13,
        'routing':14,
    }
    return modul_id

@pytest.fixture(scope='class')
def module_status_id_return():
    module_status_id = {
        'start':1,
        'stop':2,
        'reboot':3,
        'conf_in':4,
        'conf_out':5,
        'sync_ok':8,
        'sync_err':9,
    }
    return module_status_id

# удаляем старую запись, если она осталась после падения предыдущего теста теста
@pytest.fixture
def clear_table(create_connection):
    cur = create_connection.cursor()
    cur.execute("DELETE FROM tasks")
    cur.execute("DELETE FROM electricity_quality")
    cur.execute("DELETE FROM meter_relay")
    cur.execute("DELETE FROM results")
    cur.execute("DELETE FROM outcoming_packets ")
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111' OR eui = '1111111111111112'")
    create_connection.commit()
    create_connection.close
    yield
    cur = create_connection.cursor()
    cur.execute("DELETE FROM tasks")
    cur.execute("DELETE FROM electricity_quality")
    cur.execute("DELETE FROM meter_relay")
    cur.execute("DELETE FROM results")
    cur.execute("DELETE FROM outcoming_packets ")
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111' OR eui = '1111111111111112'")
    create_connection.commit()
    create_connection.close


@pytest.fixture(scope='class')
def archival_daily():
    connection = None
    try:
        connection = psycopg2.connect(database='uspd', user='admin', password='kPZa83Uz2#0', host='localhost', port='5432',)
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    cur = connection.cursor()
    # Заносим новое устройство в public.meter_device и получаем его ID
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111'")
    cur.execute(                                                                                                                                                                                                                                                                    #id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask)
        f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 22222222, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 255, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 15) RETURNING id"
        )
    ID_METER = cur.fetchone()[0]
    # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
    cur.execute(f"DELETE FROM archive_daily WHERE id_meter = {ID_METER}")
    connection.commit()

    archive_day = [ ("A+", 0, 100), ("A+", 1, 101), ("A+", 2, 102), ("A+", 3, 103), ("A+", 4, 104), ("A+", 5, 105), ("A+", 6, 106), ("A+", 7, 107), ("A+", 8, 108),
                    ("A-", 0, 200), ("A-", 1, 201), ("A-", 2, 202), ("A-", 3, 203), ("A-", 4, 204), ("A-", 5, 205), ("A-", 6, 206), ("A-", 7, 207), ("A-", 8, 208),
                    ("R+", 0, 300), ("R+", 1, 301), ("R+", 2, 302), ("R+", 3, 303), ("R+", 4, 304), ("R+", 5, 305), ("R+", 6, 306), ("R+", 7, 307), ("R+", 8, 308),
                    ("R-", 0, 400), ("R-", 1, 401), ("R-", 2, 402), ("R-", 3, 403), ("R-", 4, 404), ("R-", 5, 405), ("R-", 6, 406), ("R-", 7, 407), ("R-", 8, 408),
                    ]
    # Заносим запись в public.archive_daily
    for i in archive_day:
        cur.execute(
            f"INSERT INTO archive_daily (id_meter ,time, time_value, channel, tariff, value) VALUES ({ID_METER}, CURRENT_TIMESTAMP(3), '2022-11-05 00:00:00.000', '{i[0]}', {i[1]}, {i[2]})"
        )    
    connection.commit()
    yield
    cur.execute(f"DELETE FROM archive_daily WHERE id_meter = {ID_METER}")
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111'") 
    connection.commit()
    connection.close


@pytest.fixture(scope='class')
def load_profile():
    connection = None
    try:
        connection = psycopg2.connect(database='uspd', user='admin', password='kPZa83Uz2#0', host='localhost', port='5432',)
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    cur = connection.cursor()
    # Заносим новое устройство в public.meter_device и получаем его ID
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111'")
    cur.execute(                                                                                                                                                                                                                                                                    #id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask)
        f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 255, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 15) RETURNING id"
        )
    ID_METER = cur.fetchone()[0]
    # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
    cur.execute(f"DELETE FROM load_profile WHERE id_meter = {ID_METER}")
    connection.commit()

    load_profile = [ ("A+", 100), ("A-", 200), ("R+", 300), ("R-", 400),
                    ]
    # Заносим запись в public.archive_daily
    for i in load_profile:
        cur.execute(
            f"INSERT INTO load_profile (id_meter ,time, time_value, channel, value) VALUES ({ID_METER}, CURRENT_TIMESTAMP(3), '2022-11-05 00:00:00.000', '{i[0]}', {i[1]})"
        )    
    connection.commit()
    yield
    cur.execute(f"DELETE FROM load_profile WHERE id_meter = {ID_METER}")
    cur.execute("DELETE FROM meter_device WHERE eui = '1111111111111111'") 
    connection.commit()
    connection.close()

# удаляем старую запись, если она осталась после падения предыдущего теста теста
@pytest.fixture(scope='class')
def restart_module():
    os.system("systemctl restart uspd-routing")
    sleep(50)
    yield


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = "reports/"+datetime.now().strftime("%Y-%m-%d %H-%M-%S")+".html"