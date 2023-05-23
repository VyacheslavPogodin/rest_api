
from time import sleep
from pytest_check import check
import pytest

            #task_type parameter     gen_option code_command 
for_test_get_tasks=[(1, 2, "{serial}",        "11111111111111110B01000018", ""),
                    (2, 3, "{get time}",      "11111111111111110B01000206", ""), 
                    (5, 9,"{relay}",         "11111111111111110B0100021F", ""), 
                    (6, 8, "{instantaneous}", "11111111111111110B01000210", "0203"),
                    pytest.param(7, 6, "{get archival}",  "11111111111111110B01000300", "", marks=pytest.mark.xfail),
                    (8, 7, "{register number=1}",  "11111111111111113201000211", "01"),
                    (8, 7, "{register number=2}",  "11111111111111113201000211", "02"),
                    (8, 7, "{register number=3}",  "11111111111111113201000211", "03"),
                    (8, 7, "{register number=4}",  "11111111111111113201000211", "04"),
                    (8, 7, "{register number=5}",  "11111111111111113201000211", "05"),
                    (8, 7, "{register number=6}",  "11111111111111113201000211", "06"),
                    (8, 7, "{register number=7}",  "11111111111111113201000211", "07"),
                    (8, 7, "{register number=8}",  "11111111111111113201000211", "08"),
                    (8, 7, "{register number=9}",  "11111111111111113201000211", "09"),
                    (8, 7, "{register number=10}",  "11111111111111113201000211", "0A"),
                    (8, 7, "{register number=11}",  "11111111111111113201000211", "0B"),
                    (8, 7, "{register number=12}",  "11111111111111113201000211", "0C"),
                    (8, 7, "{register number=13}",  "11111111111111113201000211", "0D"),
                    pytest.param(9, 11, "{get current}",   "11111111111111110B01000300", "", marks=pytest.mark.xfail), 
]

            #task_type parameter     gen_option code_command 
for_test_set_tasks=[ pytest.param(3,  "{00:00-T1;10:00-T2;21:00-T3|00:00-T1;10:00-T2;21:00-T3|00:00-T1;09:00-T2;22:00-T3|11OCT,05NOV,06DEC|ACT:2022-10-27 07:45:24|}", "11111111111111110B01000118", "", marks=pytest.mark.xfail),
                    (4,  "{relay control_mode=4, output_state=1, power_limit_value=null, time_delay_off_value=null, time_delay_on_value=null}",         "11111111111111110B0100011E0301", ""), #Установка состояния реле
                    (10,  "{relay control_mode=null, output_state=null, power_limit_value=255.0, time_delay_off_value=22, time_delay_on_value=22}",         "11111111111111110B0100011E0301", ""), #становка лимита мощности
                    pytest.param(11,  "{get time}",      "11111111111111110B01000306", "", marks=pytest.mark.xfail), 
]

@pytest.mark.usefixtures("restart_module")
class TestClassTasksGet:

# Проверка таблицы public.outcoming_packets на наличие записей пакета для отправки
    @pytest.mark.parametrize("task_type, param_id, parameter, parameter_code, measuring", for_test_get_tasks)
    @pytest.mark.usefixtures("clear_table")
    def test_get_parameters(self, create_connection, task_type, param_id, parameter, parameter_code, measuring):
        
        #Формируем сообщение для таблицы public.tasks с учетом параметризации теста
        cur = create_connection.cursor()    
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (32, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0] 
        # Заносим запись в public.tasks
        cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter) VALUES (13, {task_type}, {ID_METER}, '1111111111111111', 5, {param_id}, '{parameter}') RETURNING id"
        )
        ID_TASK = cur.fetchone()[0]   
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.load_profile
        cur.execute(f"SELECT packet FROM outcoming_packets WHERE task_id = {ID_TASK} ORDER BY id" )
        packet = cur.fetchone()

        assert packet != None, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        # with check: assert packet == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        with check: assert packet[0][:26] == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        if measuring != "":
            with check: assert packet[0][-len(measuring):] == measuring, "В сформированном пакете в таблице public.outcoming_packets не верно выставлена среда или группа измерения 0x0203"

@pytest.mark.usefixtures("restart_module")
class TestClassTasksSet:
# Проверка таблицы public.outcoming_packets на наличие записей пакета для отправки
    @pytest.mark.parametrize("task_type, parameter, parameter_code, measuring", for_test_set_tasks)
    @pytest.mark.usefixtures("clear_table")
    def test_set_parameters(self, create_connection, task_type, parameter, parameter_code, measuring):
        
        #Формируем сообщение для таблицы public.tasks с учетом параметризации теста
        cur = create_connection.cursor()
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]
        # Заносим запись в public.tasks
        cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter) VALUES (13, {task_type}, {ID_METER}, '1111111111111111', 5, 1, '{parameter}') RETURNING id"
        )
        ID_TASK = cur.fetchone()[0]   
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.outcoming_packets
        cur.execute(f"SELECT packet FROM outcoming_packets WHERE task_id = {ID_TASK} ORDER BY id" )
        packet = cur.fetchone()

        assert packet != None, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        # with check: assert packet == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        with check: assert packet[0][:26] == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        if measuring != "":
            with check: assert packet[0][28:] == measuring, "В сформированном пакете в таблице public.outcoming_packets не верно выставлена среда или группа измерения 0x0203"