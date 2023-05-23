
from time import sleep
from pytest_check import check
import pytest

            #task_type parameter     gen_option code_command 
for_test_get_tasks=[
                    (1, 2, "{serial}",        "11111111111111110B01000118", ""),
                    (2, 3, "{get time}",      "11111111111111110B01000306", ""), 
                    (5, 9, "{relay}",         ("11111111111111110B0100031F", "11111111111111110B0100031D"), ""), 
                    (6, 8, "{instantaneous}", "11111111111111110B01000310", "0203"),
                    (9, 11, "{current values}", "11111111111111110B0100020B", "0201"),
                    pytest.param(8, 7 ,  "{get register}",      "11111111111111110B01000306", "", marks=pytest.mark.xfail), 

                    #Запросы архивов
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:A+, tariff:0}",  "11111111111111110B0100030A", "01160B0E000000020102020000", ), # 02(период)01020200(канал)00(тариф)  01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1m, datetime:2022-11-14 00:00:00.0, channel:A+, tariff:0}",  "11111111111111110B0100030A", "01160B0E000000030102020000", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:A-, tariff:0}",  "11111111111111110B0100030A", "01160B0E000000020102020100", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:R+, tariff:0}",  "11111111111111110B0100030A", "01160B0E000000020102020200", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:R-, tariff:0}",  "11111111111111110B0100030A", "01160B0E000000020102020300", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:A+, tariff:1}",  "11111111111111110B0100030A", "01160B0E000000020102020001", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:A+, tariff:2}",  "11111111111111110B0100030A", "01160B0E000000020102020002", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    (7, 6, "{archive interval:1d, datetime:2022-11-14 00:00:00.0, channel:A+, tariff:3}",  "11111111111111110B0100030A", "01160B0E000000020102020003", ), # 01 - за 1 час, 02 - за 1 сутки, 03 - за 1 месяц
                    # Запрос профиля
                    
                    (7, 6, "{archive interval:60m, datetime:2022-11-14 00:00:00.0, channel:A+}",  "11111111111111110B01000312", "01160B0E000000020500", ), 
                    (7, 6, "{archive interval:60, datetime:2022-11-14 00:00:00.0, channel:A-}",  "11111111111111110B01000312", "01160B0E000000020501", ), 
                    (7, 6, "{archive interval:60m, datetime:2022-11-14 00:00:00.0, channel:R+}",  "11111111111111110B01000312", "01160B0E000000020502", ), 
                    (7, 6, "{archive interval:60, datetime:2022-11-14 00:00:00.0, channel:R-}",  "11111111111111110B01000312", "01160B0E000000020503", ), 

                    (7, 6, "{archive interval:30, datetime:2022-11-14 00:00:00.0, channel:A+}",  "11111111111111110B01000312", "01160B0E000000020500", ), 
                    (7, 6, "{archive interval:30m, datetime:2022-11-14 00:00:00.0, channel:A-}",  "11111111111111110B01000312", "01160B0E000000020501", ), 
                    (7, 6, "{archive interval:30, datetime:2022-11-14 00:00:00.0, channel:R+}",  "11111111111111110B01000312", "01160B0E000000020502", ), 
                    (7, 6, "{archive interval:30m, datetime:2022-11-14 00:00:00.0, channel:R-}",  "11111111111111110B01000312", "01160B0E000000020503", ), 
                    pytest.param(8, 7,  "{get register}",  "11111111111111110B01000300", "", marks=pytest.mark.xfail), # Типы тасок более 7 не обрабатываются
]

            #task_type parameter     gen_option code_command 
for_test_set_tasks=[ pytest.param(3,  "{00:00-T1;10:00-T2;21:00-T3|00:00-T1;10:00-T2;21:00-T3|00:00-T1;09:00-T2;22:00-T3|11OCT,05NOV,06DEC|ACT:2022-10-27 07:45:24|}", "11111111111111110B01000118", "", marks=pytest.mark.xfail),
                    (4,  "{relay control_mode=4, output_state=1, power_limit_value=null, time_delay_off_value=null, time_delay_on_value=null}",         "11111111111111110B0100011E", "01"), #Установка состояния реле
                    (4,  "{relay control_mode=4, output_state=0, power_limit_value=null, time_delay_off_value=null, time_delay_on_value=null}",         "11111111111111110B0100011E", "00"), #Установка состояния реле
                    (4,  "{relay control_mode=null, output_state=null, power_limit_value=255.0, time_delay_off_value=22, time_delay_on_value=22}",         "11111111111111110B0100011C", "010416020000FF0000000000"), #становка лимита мощности
                    (4,  "{relay control_mode=null, output_state=null, power_limit_value=0.0, time_delay_off_value=22, time_delay_on_value=22}",         "11111111111111110B0100011C", "020416020000000000000000"), #становка лимита мощности
                    (4,  "{relay control_mode=null, output_state=null, power_limit_value=null, time_delay_off_value=22, time_delay_on_value=22}",         "11111111111111110B0100011C", "000416020000000000000000"), #становка лимита мощности
                    (4,  "{relay control_mode=null, output_state=null, power_limit_value=255.0, time_delay_off_value=null, time_delay_on_value=null}",         "11111111111111110B0100011C", "01040A020000FF0000000000"), #становка лимита мощности, по умолчанию время 10 секунд
                    pytest.param(11,  "{set time}",      "11111111111111110B01000306", "", marks=pytest.mark.xfail), 
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
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0] 
        # Заносим запись в public.tasks
        cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter) VALUES (13, {task_type}, {ID_METER}, '1111111111111111', 5, {param_id}, '{parameter}') RETURNING id"
        )
        ID_TASK = cur.fetchone()[0]
        if task_type == 5:
            cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter) VALUES (13, {task_type}, {ID_METER}, '1111111111111111', 5, {param_id}, '{parameter}') RETURNING id"
            )
            ID_TASK_1 = cur.fetchone()[0]
        else:
            ID_TASK_1 = ID_TASK

        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.load_profile
        cur.execute(f"SELECT packet FROM outcoming_packets WHERE task_id = {ID_TASK} OR task_id = {ID_TASK_1} ORDER BY id" )
        packet = cur.fetchall()

        assert packet != None, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        assert packet != []
        # with check: assert packet == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        
        if task_type == 5:

            with check: assert packet[0][0][:26] != packet[1][0][:26], "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
            with check: assert packet[0][0][:26] in parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
            with check: assert packet[1][0][:26] in parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        else:
            with check: assert packet[0][0][:26] == parameter_code, "В сформированном пакете в таблице public.outcoming_packets не верно сформированы данные"
        if measuring != "":
            with check: assert packet[0][0][28:] == measuring, "В сформированном пакете в таблице public.outcoming_packets не верно выставлена среда или группа измерения 0x0203"

@pytest.mark.usefixtures("restart_module")
class TestClassTasksSet:
# Проверка таблицы public.outcoming_packets на наличие записей пакета для отправки
    @pytest.mark.parametrize("task_type, parameter, parameter_code, measuring", for_test_set_tasks)
    @pytest.mark.usefixtures("clear_table")
    def test_set_parameters(self, create_connection, task_type, parameter, parameter_code, measuring):
        
        #Формируем сообщение для таблицы public.tasks с учетом параметризации теста
        cur = create_connection.cursor()
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 5, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
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