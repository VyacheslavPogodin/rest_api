from time import sleep
from pytest_check import check
import pytest

command_start_module = '/usr/bin/java -Djava.library.path="/home/root/USPD/module_myrmidon_parser/lib/" -cp .:/home/root/USPD/module_myrmidon_parser/lib/module_myrmidon_parser-0.9.25.jar:/home/root/USPD/module_myrmidon_parser/lib/log4j-1.2.17.jar:/home/root/USPD/module_myrmidon_parser/lib/postgresql-9.0-801.jdbc4.jar:/home/root/USPD/module_myrmidon_parser/lib/commons-codec-1.12.jar:/home/root/USPD/module_myrmidon_parser/lib/antlr-2.7.7.jar ru.tpp.myrmidon.ModuleMyrmidonParser'

                    #cannel       value 
for_test_incoming =[("00", "A+", '00ff140000'), 
                    ("01", "A-", '00ff143200'),
                    ("02", "R+", '00ff140000'),
                    ("03", "R-", '1e00000100'),
]
                    #cannel      tariff value 
for_test_archive =[ ("00", "A+", "00", 'ffff140000'),
                    ("00", "A+", "01", 'ffff140000'),
                    ("00", "A+", "02", 'ffff140000'),
                    ("00", "A+", "03", 'ffff140000'),
                    ("01", "A-", "00", 'ffff14ff00'),
                    ("01", "A-", "01", 'ffff14ff00'),
                    ("01", "A-", "02", 'ffff14ff00'),
                    ("01", "A-", "03", 'ffff14ff00'),
                    ("02", "R+", "00", 'ffff14ff00'),
                    ("02", "R+", "01", 'ffff14ff00'),
                    ("02", "R+", "02", 'ffff14ff00'),
                    ("02", "R+", "03", 'ffff14ff00'),
                    ("03", "R-", "00", 'ffff14ff00'),
                    ("03", "R-", "01", 'ffff14ff00'),
                    ("03", "R-", "02", 'ffff14ff00'),
                    ("03", "R-", "03", 'ffff14ff00'),
]
            #on_off, interval_type, time_off, limit_value
for_test_limit = [ # ("02", "04", "1E", "ff001E0000"), 
#                     ("02", "04", "FF", "f0001E0000"),
#                     ("02", "00", "FF", "ff001E0000"),
#                     ("02", "00", "FF", "ff001E0000"),
                    ("01", "04", "01", "ff001E0000"),
                    ("01", "00", "01", "ff001E0000"),
]

for_test_quality = [("160A0A101E1E", "00", "ff001E0000"),
                    ("160A0A101E1E", "01", "ff001E0000"),
                    ("160A0A101E1E", "02", "f0001E0000"),
                    ("160A0A101E1E", "03", "ff001E0000"),
                    ("160A0A101E1E", "04", "ff001E0000"),
                    ("160A0A101E1E", "05", "ff001E0000"),
                    ("160A0A101E1E", "06", "ff001E0000"),
                    ("160A0A101E1E", "07", "ff001E0000"),
                    ("160A0A101E1E", "08", "ff001E0000"),
                    ("160A0A101E1E", "09", "ff001E0000"),
                    ("160A0A101E1E", "0A", "ff001E0000"),
                    ("160A0A101E1E", "0B", "ff001E0000"),
                    ("160A0A101E1E", "0C", "ff001E0000"),
                    ("160A0A101E1E", "0D", "ff001E0000"),
                    ("160A0A101E1E", "0E", "ff001E0000"),
                    ("160A0A101E1E", "0F", "ff001E0000"),
                    ("160A0A101E1E", "10", "ff001E0000"),
                    ("160A0A101E1E", "11", "ff001E0000"),
                    ("160A0A101E1E", "12", "ff001E0000"),
                    ("160A0A101E1E", "13", "ff001E0000"),
                    ("160A0A101E1E", "14", "ff001E0000"),
                    ("160A0A101E1E", "15", "ff001E0000"),
                    ("160A0A101E1E", "16", "ff001E0000"),
#<<<<<<< HEAD
                    pytest.param("160A0A101E1E", "17", "ff001E0000", marks=pytest.mark.xfail),
#=======
                    ("160A0A101E1E", "17", "ff001E0000"),
                    ("160A0A101E1E", "18", "ff001E0000"),
                    ("160A0A101E1E", "19", "ff001E0000"),
                    ("160A0A101E1E", "1A", "ff001E0000"),
                    ("160A0A101E1E", "1B", "ff001E0000"),
                    ("160A0A101E1E", "1C", "ff001E0000"),
                    ("160A0A101E1E", "1D", "ff001E0000"),
                    ("160A0A101E1E", "1E", "ff001E0000"),
                    ("160A0A101E1E", "1F", "ff001E0000"),
                    ("160A0A101E1E", "20", "ff001E0000"),
                    ("160A0A101E1E", "21", "ff001E0000"),
                    ("160A0A101E1E", "27", "ff001E0000"),
                    ("160A0A101E1E", "28", "ff001E0000"),
                    ("160A0A101E1E", "29", "ff001E0000"),
                    ("160A0A101E1E", "2A", "ff001E0000"),
                    ("160A0A101E1E", "2B", "ff001E0000"),
                    ("160A0A101E1E", "2C", "ff001E0000"),
#>>>>>>> f445941ee1752e53517a83c5322b2c2fcff66faa
]

@pytest.mark.usefixtures("restart_module")


class TestClassIncomingPacketLoadProfile:

# Проверка таблицы load_profile на наличие записей о параметрах нагрзки
    @pytest.mark.parametrize("send_incoming , channel, value", for_test_incoming)
    @pytest.mark.usefixtures("clear_table")
    
    
    
    def test_load_profile(self, create_connection, send_incoming , channel, value):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста
        DICT_SEND_INCOMING = {
            'load_profile '+channel : '11111111111111110B01011213011601001001160A15110000001E0000020205'+send_incoming+value.upper()+'000000',
        }
        val_dec = int(value[:2], 16)/65536 + int(value[2:4], 16)/256 + int(value[4:6], 16) + int(value[6:8], 16)*256 + int(value[8:10], 16)*65536
        
        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]
        # Удаляем записи в public.load_profile, если они остались после падения предыдущего теста
        cur.execute(f"DELETE FROM load_profile WHERE id_meter = {ID_METER}")
        create_connection.commit()
        sleep(1)
        # Заносим запись в public.incoming_packets
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['load_profile '+channel]}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.load_profile
        cur.execute(f"SELECT * FROM load_profile WHERE id_meter = {ID_METER} ORDER BY time DESC LIMIT 1" )
        rezult = cur.fetchone()

        assert rezult != None, "Запись параметров профиля отсутствует в таблице load_profile"
        with check: assert rezult[3] == channel, "Канал измерения в таблице не соответствует требуемому"
        with check: assert rezult[5] == round(val_dec, 12), "Значение нагрузки не соответствует требуемому"


@pytest.mark.usefixtures("restart_module")
class TestClassIncomingPacketArchiveDay:
    
    # Проверка таблицы public.archive_daily на наличие записей суточных показаний
    @pytest.mark.parametrize("send_incoming , channel, tarif, value", for_test_archive)
    @pytest.mark.usefixtures("clear_table")
    def test_archive_daily(self, create_connection, send_incoming , channel, tarif, value):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста
        DICT_SEND_INCOMING = {
            'archive_daily '+channel +' '+tarif : '11111111111111110B0101020A011601205001160A1400000002010000020202'+send_incoming+tarif+value.upper()+'000000',
        }
        val_dec = int(value[:2], 16)/65536 + int(value[2:4], 16)/256 + int(value[4:6], 16) + int(value[6:8], 16)*256 + int(value[8:10], 16)*65536

        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]
        # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
        cur.execute(f"DELETE FROM archive_daily WHERE id_meter = {ID_METER}")
        create_connection.commit()
        sleep(1)
        # Заносим запись в public.incoming_packets
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['archive_daily '+channel +' '+tarif]}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.archive_daily
        cur.execute(f"SELECT * FROM archive_daily WHERE id_meter = {ID_METER} ORDER BY time DESC LIMIT 1" )
        rezult = cur.fetchone()

        assert rezult != None, "Запись параметров профиля отсутствует в таблице archive_daily"
        with check: assert rezult[4] == channel, "Канал измерения в таблице не соответствует требуемому"
        with check: assert rezult[5] == int(tarif,16), "Канал измерения в таблице не соответствует требуемому"
        with check: assert rezult[6] == round(val_dec, 4), "Значение нагрузки не соответствует требуемому"


@pytest.mark.usefixtures("restart_module")
class TestClassIncomingTime:

    @pytest.mark.usefixtures("clear_table")
    def test_time_py(self, create_connection):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста
        from datetime import datetime
        
        date = datetime.utcnow()
        date_send = date.strftime("%y %m %d %H %M %S").split()
        date_hex = ''
        for i in date_send:
            date_hex += format(int(i), 'X').zfill(2)

        date_bd = date.strftime("%y-%m-%d-%H-%M-%S").replace('-0', '-') #Приводим к формату вывода из БД
        DICT_SEND_INCOMING = {
            'time PY' : '11111111111111110B010100060116012801'+ date_hex,
        }

        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
            
        ID_METER = cur.fetchone()[0]
        # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
        cur.execute(f"DELETE FROM results WHERE meter_identifier = '1111111111111111'")
        create_connection.commit()
        sleep(1)
        # Заносим запись в public.incoming_packets
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['time PY']}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.results
        cur.execute(f"SELECT task_type, response_id, response, task_id FROM results WHERE meter_identifier = '1111111111111111' ORDER BY id DESC LIMIT 1" ) # task_type, response_id, response, task_id
        rezult = cur.fetchone()

        assert rezult != None, "Запись параметров профиля отсутствует в таблице results"
        with check: assert rezult[0] == 2, "Канал измерения в таблице не соответствует требуемому"
        with check: assert rezult[1] == 3, "Канал измерения в таблице не соответствует требуемому"
        with check: assert rezult[2] == date_bd, "Значение нагрузки не соответствует требуемому"
        with check: assert rezult[3] == -1, "Значение нагрузки не соответствует требуемому"


@pytest.mark.usefixtures("restart_module")
class TestClassIncomingRelay:

    @pytest.mark.parametrize("output_state , limit_value ", [("00", 0.0), ("01", 0.0),])
    @pytest.mark.usefixtures("clear_table")
    def test_relay_py(self, create_connection, output_state , limit_value):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста
        state = {'00':1, '01':2}
        # limit_value = 0.0
        DICT_SEND_INCOMING = {
            'relay PY' : '11111111111111110B0101031F01160108'+ output_state,
        }                                #0B0101031F0116010801
                                        #0B0101011F0116012D01
        
        cur = create_connection.cursor()
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]

        cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter, status) VALUES (13, 5, {ID_METER}, '1111111111111111', 5, 9, '"+"{relay}"+"', 2) RETURNING id"
        )
        ID_TASK = cur.fetchone()[0]
        cur.execute(
            f"INSERT INTO outcoming_packets (module_id, priority_id, sequence, packet, task_id) VALUES (13, 4, 0, '1111111111111111', {ID_TASK})"
        ) 
        # Заносим запись в public.incoming_packets
        create_connection.commit()
        
        sleep(2)
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['relay PY']}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.meter_relay
        cur.execute(f"SELECT * FROM meter_relay WHERE meter_id = {ID_METER} ORDER BY time DESC LIMIT 1" ) # task_type, response_id, response, task_id
        meter_relay = cur.fetchone()
        cur.execute(f"SELECT task_type, response_id, response, task_id FROM results WHERE meter_identifier = '1111111111111111' ORDER BY id DESC LIMIT 1" ) # task_type, response_id, response, task_id
        rezult = cur.fetchone()

        assert meter_relay != None, "Запись параметров профиля отсутствует в таблице meter_relay"
        assert rezult != None, "Запись параметров профиля отсутствует в таблице rezult"
        with check: assert meter_relay[3] == state[f"{output_state}"], "Состояние реле в таблице не соответствует теребуемому"
        with check: assert meter_relay[4] == None, "Канал измерения в таблице не соответствует требуемому"
        with check: assert meter_relay[5] == None, "Значение нагрузки не соответствует требуемому"
        with check: assert meter_relay[6] == limit_value, "Значение нагрузки не соответствует требуемому"
        with check: assert rezult[2][1:-1] == f'relay control_mode=null, output_state={state[f"{output_state}"]-1}, power_limit_value=null, time_delay_off_value=null, time_delay_on_value=null', "Значение нагрузки не соответствует требуемому"


# <<<<<<< HEAD
@pytest.mark.usefixtures("restart_module")
class TestClassIncomingLimit:
# =======
# @pytest.mark.usefixtures("restart_module")
# class TestClassIncomingLimit:
# >>>>>>> f445941ee1752e53517a83c5322b2c2fcff66faa

    @pytest.mark.parametrize("on_off, interval_type, time_off, limit_value ", for_test_limit)
    @pytest.mark.usefixtures("clear_table")
    def test_limit_py(self, create_connection, on_off, interval_type, time_off, limit_value):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста

        TYPE_TIME = {'00':60, '04':1}

        DICT_SEND_INCOMING = {
            'relay PY' : '11111111111111110B0101011D0116012E'+on_off+interval_type+time_off+'02'+limit_value+'000000',
        }                               
        val_limit_dec = int(limit_value[:2], 16)/65536 + int(limit_value[2:4], 16)/256 + int(limit_value[4:6], 16) + int(limit_value[6:8], 16)*256 + int(limit_value[8:10], 16)*65536
        val_time_dec = int(time_off, 16)*TYPE_TIME[f'{interval_type}']
        
        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]

        cur.execute(
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter, status) VALUES (13, 5, {ID_METER}, '1111111111111111', 5, 9, '"+"{relay}"+"', 2) RETURNING id"
        )
        ID_TASK = cur.fetchone()[0]
        cur.execute(
            f"INSERT INTO outcoming_packets (module_id, priority_id, sequence, packet, task_id) VALUES (13, 4, 0, '1111111111111111', {ID_TASK})"
        ) 
        # Заносим запись в public.incoming_packets
        create_connection.commit()
        sleep(2)
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['relay PY']}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.meter_relay
        cur.execute(f"SELECT * FROM meter_relay WHERE meter_id = {ID_METER} ORDER BY time DESC LIMIT 1" ) # task_type, response_id, response, task_id
        meter_relay = cur.fetchone()
        cur.execute(f"SELECT task_type, response_id, response, task_id FROM results WHERE meter_identifier = '1111111111111111' ORDER BY id DESC LIMIT 1" ) # task_type, response_id, response, task_id
        rezult = cur.fetchone()

        assert meter_relay != None, "Запись параметров профиля отсутствует в таблице meter_relay"
        assert rezult != None, "Запись параметров профиля отсутствует в таблице rezult"
        with check: assert meter_relay[6] == round(val_limit_dec, 4), "Значение нагрузки не соответствует требуемому"
        with check: assert meter_relay[8] == val_time_dec, "Значение нагрузки не соответствует требуемому"
        with check: assert rezult[2][1:-1] == f'relay control_mode=null, output_state=null, power_limit_value={round(val_limit_dec, 6)}, time_delay_off_value={val_time_dec}, time_delay_on_value=null', "Значение нагрузки не соответствует требуемому"


@pytest.mark.usefixtures("restart_module")
class TestClassIncomingSerial:

    @pytest.mark.usefixtures("clear_table")
    def test_serial_num_py(self, create_connection):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста

        DICT_SEND_INCOMING = {
            'serial num PY' : '11111111111111110B010100180116012E3832324E3134343335353833330000000000000000000000000000000000',
        }
        
        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]
        
        cur.execute(
# <<<<<<< HEAD
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter, status) VALUES (13, 5, {ID_METER}, '1111111111111111', 5, 9, '"+"{serial}"+"', 2) RETURNING id"
# =======
            f"INSERT INTO tasks (module_id, task_type, meter_id, eui, interface_id, param_id, parameter, status) VALUES (13, 1, {ID_METER}, '1111111111111111', 5, 9, '"+"{serial}"+"', 2) RETURNING id"
# >>>>>>> f445941ee1752e53517a83c5322b2c2fcff66faa
        )
        ID_TASK = cur.fetchone()[0]
        cur.execute(
            f"INSERT INTO outcoming_packets (module_id, priority_id, sequence, packet, task_id) VALUES (13, 4, 0, '1111111111111111', {ID_TASK})"
        )
        # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
        cur.execute(f"DELETE FROM results WHERE meter_identifier = '1111111111111111'")
        create_connection.commit()
        sleep(1)
        # Заносим запись в public.incoming_packets
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['serial num PY']}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.results
        cur.execute(f"SELECT task_type, response_id, response, task_id FROM results WHERE meter_identifier = '1111111111111111' ORDER BY id DESC LIMIT 1" ) # task_type, response_id, response, task_id
        rezult = cur.fetchone()

        assert rezult != None, "Запись параметров профиля отсутствует в таблице archive_daily"
        with check: assert rezult[0] == 1, "Тип запроса в таблице не соответствует требуемому"
        with check: assert rezult[1] == 2, "Тип ответа в таблице не соответствует требуемому"
        with check: assert rezult[2][1:-1] == 'serial:822N144355833', "Запись о серийном номере не соответствует требуемому"
        with check: assert rezult[3] == -1, "task_id не соответствует требуемому"



# <<<<<<< HEAD
@pytest.mark.usefixtures("restart_module")
# =======
# @pytest.mark.usefixtures("restart_module")
# >>>>>>> f445941ee1752e53517a83c5322b2c2fcff66faa
class TestClassIncomingQuality:

    @pytest.mark.parametrize("date_time, quality_type, quality_value ", for_test_quality)
    @pytest.mark.usefixtures("clear_table")
    def test_quality_py(self, create_connection, date_time, quality_type, quality_value):
        #Формируем сообщение для таблицы public.incoming_packets с учетом параметризации теста
        import datetime
        DICT_SEND_INCOMING = {
            'quality PY' : '11111111111111110B01010210011601030001'+date_time+'0000020203'+quality_type+quality_value+'000000',
        }
        
        val_dec = int(quality_value[:2], 16)/65536 + int(quality_value[2:4], 16)/256 + int(quality_value[4:6], 16) + int(quality_value[6:8], 16)*256 + int(quality_value[8:10], 16)*65536
        quality_type_dec = int(quality_type, 16)

        cur = create_connection.cursor()
        # Заносим новое устройство в public.meter_device и получаем его ID
        cur.execute(
            f"INSERT INTO meter_device (id_model, serial, eui, id_interface, in_time, archive, included_in_survey, last_time, tariff_mask, online, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, password_l, password_h, name, channel_mask) VALUES (2, 111, '1111111111111111', 1, CURRENT_TIMESTAMP(3), False, True, CURRENT_TIMESTAMP(0), 4, False, 30, 1, 1, 1, CURRENT_TIMESTAMP(0), '111111', '222222', 'test', 0) RETURNING id"
            )
        ID_METER = cur.fetchone()[0]
        # Удаляем записи в public.archive_daily, если они остались после падения предыдущего теста
        cur.execute(f"DELETE FROM results WHERE meter_identifier = '1111111111111111'")
        create_connection.commit()
        sleep(1)
        # Заносим запись в public.incoming_packets
        cur.execute(
            f"INSERT INTO incoming_packets (module_id , priority_id, sequence, packet) VALUES (4, 1, 0, '{DICT_SEND_INCOMING['quality PY']}')"
        )    
        create_connection.commit()
        sleep(10)
        # Проверяем наличие записи в public.electricity_quality
        cur.execute(f"SELECT value, time_value, measuring_type FROM electricity_quality WHERE id_meter = {ID_METER} ORDER BY measuring_type DESC LIMIT 1" ) # task_type, response_id, response, task_id
        electric_quality = cur.fetchone()
        # Проверяем наличие записи в public.electricity_quality
        cur.execute(f"SELECT task_type, response_id, response, task_id FROM results WHERE meter_identifier = '1111111111111111' ORDER BY id DESC LIMIT 1" ) # task_type, response_id, response, task_id
        rezult = cur.fetchone()

        assert rezult != None, "Запись параметров качества отсутствует в таблице electricity_quality"
        assert electric_quality != None, "Запись параметров качества отсутствует в таблице electricity_quality"
        
        with check: assert rezult[0] == 6, "Тип запроса в таблице не соответствует требуемому"
        with check: assert rezult[1] == 8, "Тип ответа в таблице не соответствует требуемому"
        with check: assert rezult[2][1:-1] == f'instantaneous datetime=22-10-10-16-30-30, measurement={quality_type_dec}, value={val_dec}', "Запись о серийном номере не соответствует требуемому"
        with check: assert rezult[3] == -1, "task_id не соответствует требуемому"

        with check: assert electric_quality[0] == round(val_dec, 4), "Тип задачи в таблице не соответствует требуемому"
        with check: assert electric_quality[1] == datetime.datetime(2022, 10, 10, 16, 30, 30), "Тип задачи в таблице не соответствует требуемому"
        with check: assert electric_quality[2] == quality_type_dec, "Тип задачи в таблице не соответствует требуемому"
