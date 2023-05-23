import os
from re import findall
from time import sleep
from pytest_check import check



#Тесты модуля time на функциональность при отправке команды на перезагрузку модуля. 
class TestClassCheckTableBD:


# Проверка таблицы status на наличие записей после перезагрузки модуля и логов на наличие записей о запуске модуля
    def test_check_status(self, create_connection, module_status_id_return, modul_id_return):
        n=2
        S_L = {}
        modul_id = modul_id_return['genopt_generator']
        modul_status = module_status_id_return
        os.system('rm /home/root/USPD/logs/generator_debug.log')                     # Очистка файла логов
        #sleep(2)
        os.system('systemctl restart uspd-routing')                           # Перезапуск модуля
        sleep(90)
        
        with open("/home/root/USPD/logs/generator_debug.log", 'r') as outfile:     # Чтение файла логов
            time_log = outfile.readlines()
        S_L['stop_module'] = None
        S_L['start_module'] = None
        S_L['connect_bd'] = None

        for send in time_log:
            #print(send)
            if send.find('[INFO] Shutting down') != -1:
                S_L['stop_module'] = 'OK'
            
            elif send.find('[INFO] Starting module') != -1:
                S_L['start_module'] = 'OK'
            
            elif send.find('[INFO] PostgreSQL JDBC Driver successfully connected') != -1:
                S_L['connect_bd'] = 'OK'
            
            elif send.find('version DB this module') != -1:
                S_L['version_bd'] = 'OK'

        connection = create_connection
        cur = connection.cursor()

        cur.execute(
            f"SELECT * FROM status WHERE module_id = {modul_id} ORDER BY id DESC LIMIT {n}"
            )
    
        id_list = cur.fetchall()
        
        
        
        #with check: assert S_L['stop_module'] == 'OK',  "В логах отсутствует запись об остановке модуля"
        with check: assert S_L['start_module'] == 'OK', "В логах отсутствует запись о старте модуля"
        #with check: assert S_L['connect_bd'] == 'OK', "В логах отсуствует запись об успешном подключении к базе данных"
        with check: assert S_L['version_bd'] == 'OK', "База данных соответствует требуемой"
        #with check: assert S_L['sync_ok'] == 'OK', "Статус синхронизации не внесен в таблицу status базы данных"
        
        with check: assert isinstance(id_list[0], tuple)
        with check: assert id_list[n-1][3] == modul_status['stop'], "В таблице status отсутствует запись об остановке модуля"
        with check: assert id_list[n-2][3] == modul_status['start'], "В таблице status отсутствует запись о запуске модуля"


# Проверка логов на наличие записи и соответствие ее применения конфигурации модуля generator из БД
    def test_config_module(self, create_connection):

        S_L = {}

        connection = create_connection
        cur = connection.cursor()
        cur.execute(
            f"SELECT * FROM config_genopt_generator "
            )
        
        config_from_bd = cur.fetchone()

        S_L['taskCheckPeriod'] = None
        S_L['stopFlagCheckPeriod'] = None
        S_L['activityMarkPeriod'] = None

        with open("/home/root/USPD/logs/generator_debug.log", 'r') as outfile:     # Чтение файла логов
            config_from_log = outfile.readlines()

        for send in config_from_log:
            #print(send)
            
            if send.find('[INFO] Config{') != -1: # Частота мониторинга новых событий в секундах
                S_L['taskCheckPeriod'] = (int(findall(r'\=\d+', send)[0][1:]))
                S_L['stopFlagCheckPeriod'] = (int(findall(r'\=\d+', send)[1][1:]))
                S_L['activityMarkPeriod'] = (int(findall(r'\=\d+', send)[2][1:]))

        #with check: assert config_from_log.keys() == []
        with check: assert len(config_from_bd) == 4
        with check: assert config_from_bd[1] == S_L['taskCheckPeriod'], "Настройки generator не соответствуют требуемым или отсутствует запись в логах"
        with check: assert config_from_bd[2] == S_L['stopFlagCheckPeriod'], "Настройки generator не соответствуют требуемым или отсутствует запись в логах"
        with check: assert config_from_bd[3] == S_L['activityMarkPeriod'], "Настройки generator не соответствуют требуемым или отсутствует запись в логах"



# Тест модуля при выставлении флага в таблице flags_table
    def test_flags_table(self, create_connection, module_status_id_return, modul_id_return):

        module_id_str = modul_id_return['genopt_generator']
        modul_status = module_status_id_return
        STOP_MODULE = 'NOT OK'

        connection = create_connection
        cur = connection.cursor()

        

# Выставляем флаг True
        cur.execute(
            f"INSERT INTO flags_table (flag, module_id) VALUES (True, {module_id_str}) RETURNING id"
            )
        connection.commit()
        id_flags = cur.fetchone()
        
        os.system(r" >/home/root/USPD/logs/generator_debug.log")
        sleep(10)
# Проверяем что он изменился на False
        cur.execute(
            f"SELECT flag FROM flags_table WHERE id = {id_flags[0]}"
            )
        flag = cur.fetchone()

# Провряем статус в таблице status
        cur.execute(
            f"SELECT status_id FROM status WHERE module_id = {module_id_str} ORDER BY id DESC"
            )
        
        status = cur.fetchone()

# Проверяем логи на наличие записи о остановке
        with open("/home/root/USPD/logs/generator_debug.log", 'r') as outfile:     # Чтение файла логов
            module_log = outfile.readlines()
        
        for send in module_log:
            #print(send)
            if send.find('[INFO] Shutting down') != -1:
                STOP_MODULE = 'OK'



        os.system('systemctl restart uspd-routing')
        #sleep(40)

        with check: assert flag[0] == False, "В таблице flags_table флаг не изменился на False"
        with check: assert status[0] == modul_status['stop'], "В таблице status не выставлен статус stop"
        with check: assert module_log != [], "Отсутствует запись в логе"
        with check: assert STOP_MODULE == 'OK', "Запись в логе не соответствует требуемой при остановке модуля"




    def flags_table_100(self, create_connection):

        connection = create_connection
        cur = connection.cursor()
        check = True
        n = []
        module_num = [8] #[1,2,3,4,5,6,8,13]
        num_of_runs = 10

        for j in module_num:

            module_id = j

            for i in range(num_of_runs):
                # Проверяем наличие записей в таблице flags_table, если записи есть удаляем
                cur.execute(
                    f"SELECT flag FROM flags_table WHERE module_id = {module_id} ORDER BY id DESC"
                    )
                check_flag_table = cur.fetchone()
                
                if check_flag_table != None:
                    
                    cur.execute(
                        f"DELETE FROM flags_table"
                        )
                    connection.commit()

                os.system('systemctl restart uspd-routing')
                sleep(40)

                cur.execute(
                    f"INSERT INTO flags_table (flag, module_id) VALUES (True, {module_id}) RETURNING id"
                    )
                connection.commit()
                id_flag = cur.fetchone()
                sleep(7)
            
                cur.execute(
                    f"SELECT status_id FROM status WHERE module_id = {module_id} ORDER BY id DESC"
                    )
            
                in_table_status = cur.fetchone()

                cur.execute(
                    f"SELECT flag FROM flags_table WHERE id = {id_flag[0]}"
                    )
            
                in_table_flag = cur.fetchone()
            
                if in_table_flag[0]:
                    check = False
                    n.append(str(module_id)+' модуль, шаг: '+str(i)+f', статус: {in_table_status}')
                    
                cur.execute(
                    f"DELETE FROM flags_table"
                    )
                connection.commit()

        os.system('systemctl restart uspd-routing')

        with check: assert check == True, f"Флаг не выставлен в {n}"