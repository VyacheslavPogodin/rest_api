
import binascii
from datetime import datetime
from time import sleep
from function import general_function, connect_dlms
from function import day_function
from function import hourly_function
from function import monthly_function
from function import load_profile_function
from function import volt_reg_function
from function import current_reg_function
from function import on_off_reg_function
from function import reconfig_reg_function
from function import external_events_function
from function import com_events_function
from function import access_events_function
from function import diagnostics_events_function
from function import tangent_reg_function
from function import quality_reg_function
from function import in_out_reg_function
from function import time_correct_reg_function
from function import delete_archive
'''
Имитатор счетчика Нартис 
'''
                
# Готовим и отправляем ответное сообщение
def reply_message(send, dict_device, ser):
    #dict_device = dict_device
    try:
        serial_number_dev = dict_device[str(send[3])]
    except IndexError as e:
        with open("IndexError.log", 'a') as outfile:
            outfile.write(str(send) +'  '+ f'  {e} ')
        
# Команда на начало обмена и окончание обмена    
    if send[5:6] == b'\x93' or send[5:6] == b'S': # PING   
        general_function.print_term_and_write_log(f'Ассоциация dlms, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        answer = connect_dlms.assotiate_dlms(send,)
        ser.write(answer)
        general_function.print_term_and_write_log(answer)
# associate response с паролем для чтения данных 111       
    elif send[4:6] == b'A\x10':
        general_function.print_term_and_write_log(f'Аутентификация в режиме Чтения, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        answer = connect_dlms.auth_dlms_password(send)
        ser.write(answer)
        general_function.print_term_and_write_log(answer)


    elif send[4:6] == b'a\x10':
        general_function.print_term_and_write_log(f'Аутентификация в режиме Конфигурирования, адрес {send[3]}')
        general_function.print_term_and_write_log(send, )
        connect_dlms.auth_dlms_cripto(send, ser, dict_device,)

# OBIS код запроса серийного номера  OBIS-код 0.0.96.1.0.255              
    elif send[16:22] == b'\x00\x00`\x01\x00\xff': 
        general_function.print_term_and_write_log(f'Запрос серийного номера, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        answer = connect_dlms.get_serial_number(send, serial_number_dev,)
        ser.write(answer)
        general_function.print_term_and_write_log(answer)
    
    # OBIS код запроса даты и времени OBIS-код 0.0.1.0.0.255
    elif send[4:6] == b'A2' and send[16:22] == b'\x00\x00\x01\x00\x00\xff':
        general_function.print_term_and_write_log(f'Получение даты и времени, адрес {send[3]}')  
        general_function.print_term_and_write_log(send)
        answer = connect_dlms.get_date(send,)
        ser.write(answer)
        general_function.print_term_and_write_log(answer)

      # OBIS код установки даты и времени OBIS-код 0.0.1.0.0.255
    elif send[4:6] == b'aT' and send[16:22] == b'\x00\x00\x01\x00\x00\xff':  
        general_function.print_term_and_write_log(f'Установка даты и времени, адрес {send[3]}')  
        general_function.print_term_and_write_log(send)
        answer = connect_dlms.set_date(send,)
        ser.write(answer)
        general_function.print_term_and_write_log(answer)

# Запрос списка объектов архивов    

    # OBIS код - 1.0.98.2.0.255 03 Журнал ежесуточных показаний. 
    elif send[14:23] == b'\x00\x07\x01\x00b\x02\x00\xff\x03':
        general_function.print_term_and_write_log(f'Получение суточного архива OBIS 1.0.98.2.0.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        day_function.get_day_archive_object(send, ser, dict_device,)
     # OBIS код - 1.0.99.2.0.255 03 Журнал часовых показаний. 
    elif send[14:23] == b'\x00\x07\x01\x00c\x02\x00\xff\x03':
        general_function.print_term_and_write_log(f'Получение часового архива OBIS 1.0.99.2.0.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        hourly_function.get_hourly_archive_object(send, ser, dict_device,)
    # OBIS код - 1.0.98.1.0.255 03 Журнал ежемесячных показаний.
    elif send[14:23] == b'\x00\x07\x01\x00b\x01\x00\xff\x03':
        general_function.print_term_and_write_log(f'Получение месячного архива OBIS 1.0.98.1.0.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        monthly_function.get_monthly_archive_object(send, ser, dict_device,)
# Запрос списка объектов профиля

    # OBIS код - 0.0.99.1.0.255 03 Журнал Профиль 1. 
    elif send[14:23] == b'\x00\x07\x01\x00c\x01\x00\xff\x03':
        general_function.print_term_and_write_log(f'Получение профиля нагрузки OBIS 1.0.99.1.0.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        load_profile_function.get_load_profile_object(send, ser, dict_device,)
# Запрос списка объектов журналов

    # OBIS код - 0.0.99.98.0.255 03 Журнал напряжений. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x00\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала напряжений> OBIS 1.0.99.98.0.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        volt_reg_function.get_voltage_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.1.255 03 Журнал токов. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x01\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала токов> OBIS 1.0.99.98.1.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        current_reg_function.get_current_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.2.255 03 Журнал включений/выключений.
    elif send[14:23] == b'\x00\x07\x00\x00cb\x02\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала включений/выключений> OBIS 1.0.99.98.2.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        on_off_reg_function.get_on_off_and_relay_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.3.255 03 Журнал коррекции данных.
    elif send[14:23] == b'\x00\x07\x00\x00cb\x03\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала коррекции данных> OBIS 1.0.99.98.3.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        reconfig_reg_function.get_reconfig_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.4.255 03 Журнал Внешних воздействий. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x04\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала внешних воздействий> OBIS 1.0.99.98.4.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        external_events_function.get_external_events_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.5.255 03 Журнал Коммуникационные события. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x05\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала коммуникационные события> OBIS 1.0.99.98.5.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        com_events_function.get_communication_events_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.6.255 03 Журнал контроль доступа. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x06\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала контроль доступа> OBIS 1.0.99.98.6.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        access_events_function.get_access_events_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.7.255 03 Журнал Самодиагностики. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x07\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала самодиагностики> OBIS 1.0.99.98.7.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        diagnostics_events_function.get_diagnostics_events_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.8.255 03 Журнал Превышение тангенса. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\x08\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала превышение тангенса> OBIS 1.0.99.98.8.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        tangent_reg_function.get_tangent_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.9.255 03 Журнал Параметры качества сети. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\t\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала превышение параметры качества сети> OBIS 1.0.99.98.9.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        quality_reg_function.get_quality_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.10.255 03 Журнал Состояний дискретных входов и выходов. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\n\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала состояний дискретных входов и выходов> OBIS 1.0.99.98.10.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        in_out_reg_function.get_input_output_register_object(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.13.255 03 Журнал коррекции времени. 
    elif send[14:23] == b'\x00\x07\x00\x00cb\r\xff\x03':
        general_function.print_term_and_write_log(f'Получение <Журнала коррекции времени> OBIS 1.0.99.98.13.255, адрес {send[3]}')
        general_function.print_term_and_write_log(send)
        time_correct_reg_function.get_time_correction_register_object(send, ser, dict_device,)

# Запрос списка масштабов

    # OBIS код - 1.0.94.7.2.255 Профиль масштаба для журнала ежесуточных показаний . Запрос списка объектов дневного архива
    elif send[14:23] == b'\x00\x07\x01\x00^\x07\x02\xff\x02':
        general_function.print_term_and_write_log(send)
        day_function.get_day_archive_scale(send, ser, dict_device,)    
    # OBIS код - 1.0.94.7.1.255 Профиль масштаба для журнала часовых показаний . Запрос списка масштабов часового архива
    elif send[14:23] == b'\x00\x07\x01\x00^\x07\x01\xff\x02':
        general_function.print_term_and_write_log(send)
        hourly_function.get_hourly_archive_scale(send, ser, dict_device,) 
    # OBIS код - 1.0.94.7.4.255 Профиль масштаба для получасового профиля 1 . Запрос масштабов объектов профиля 1
    elif send[14:23] == b'\x00\x07\x01\x00^\x07\x04\xff\x02':
        general_function.print_term_and_write_log(send)
        load_profile_function.get_load_profile_scale(send, ser, dict_device,)
    # OBIS код - 1.0.94.7.1.255 Профиль масштаба для журнала напряжений. Запрос списка объектов журнала напряжений
    #elif send[14:23] == b'\x00\x07\x01\x00^\x07\x01\xff\x02':
    #    volt_reg_function.get_voltage_register_scale(send, ser, dict_device,)




# Получение значений архивов

    # OBIS код - 1.0.98.2.0.255 Журнал ежесуточных показаний. Запрос списка объектов дневного архива
    elif send[14:23] == b'\x00\x07\x01\x00b\x02\x00\xff\x02': 
        general_function.print_term_and_write_log(send)
        day_function.get_day_archive(send, ser, dict_device,)
    # OBIS код - 1.0.99.2.0.255 Журнал часовых показаний. Запрос списка объектов часового архива
    elif send[14:23] == b'\x00\x07\x01\x00c\x02\x00\xff\x02': 
        general_function.print_term_and_write_log(send)
        hourly_function.get_hourly_archive(send, ser, dict_device,)
    # OBIS код - 1.0.98.1.0.255 Журнал месячных показаний. Запрос списка объектов месячного архива
    elif send[14:23] == b'\x00\x07\x01\x00b\x01\x00\xff\x02':
        general_function.print_term_and_write_log(send)
        monthly_function.get_monthly_archive(send, ser, dict_device,)
# Запрос значений профиля    

    # OBIS код - 1.0.99.2.0.255 Журнал получасовой профиль нагрузок. Запрос профиля нагрузок
    elif send[14:23] == b'\x00\x07\x01\x00c\x01\x00\xff\x02':
        general_function.print_term_and_write_log(send)
        load_profile_function.get_load_profile(send, ser, dict_device,)

# Запрос значений журналов    
    # OBIS код - 0.0.99.98.0.255 Журнал напряжений. Запрос значений журнала напряжений
    elif send[14:23] == b'\x00\x07\x00\x00cb\x00\xff\x02': 
        general_function.print_term_and_write_log(send)
        volt_reg_function.get_voltage_register(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.1.255 Журнал токов. Запрос значений журнала токов
    elif send[14:23] == b'\x00\x07\x00\x00cb\x01\xff\x02':
        general_function.print_term_and_write_log(send)
        current_reg_function.get_current_register(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.2.255 Журнал включений/выключений. Запрос значений журнала включений/выключений
    elif send[14:23] == b'\x00\x07\x00\x00cb\x02\xff\x02':
        general_function.print_term_and_write_log(send)
        on_off_reg_function.get_on_off_and_relay_register(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.3.255 Журнал коррекции данных. Запрос значений журнала коррекции данных
    elif send[14:23] == b'\x00\x07\x00\x00cb\x03\xff\x02': 
        general_function.print_term_and_write_log(send)
        reconfig_reg_function.get_reconfig_register(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.4.255 Журнал Внешних воздействий. Запрос значений журнала Внешних воздействий
    elif send[14:23] == b'\x00\x07\x00\x00cb\x04\xff\x02':
        general_function.print_term_and_write_log(send)
        external_events_function.get_external_events(send, ser, dict_device,)        
    # OBIS код - 0.0.99.98.5.255 Журнал Коммуникационные события. Запрос значений журнала Коммуникационные события
    elif send[14:23] == b'\x00\x07\x00\x00cb\x05\xff\x02':  
        general_function.print_term_and_write_log(send)
        com_events_function.get_communication_events(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.6.255 Журнал контроль доступа. Запрос значений журнала контроль доступа
    elif send[14:23] == b'\x00\x07\x00\x00cb\x06\xff\x02':
        general_function.print_term_and_write_log(send)
        access_events_function.get_access_events(send, ser, dict_device,)
    # OBIS код - 0.0.99.98.7.255 Журнал Самодиагностики. Запрос значений журнала Самодиагностики
    elif send[14:23] == b'\x00\x07\x00\x00cb\x07\xff\x02':
        general_function.print_term_and_write_log(send)
        diagnostics_events_function.get_diagnostics_events(send, ser, dict_device,)
        # OBIS код - 0.0.99.98.8.255 Журнал Превышение тангенса. Запрос значений журнала Превышение тангенса
    elif send[14:23] == b'\x00\x07\x00\x00cb\x08\xff\x02':
        general_function.print_term_and_write_log(send)
        tangent_reg_function.get_tangent_register(send, ser, dict_device,)
        # OBIS код - 0.0.99.98.9.255 Журнал Параметры качества сети. Запрос значений журнала Параметры качества сети
    elif send[14:23] == b'\x00\x07\x00\x00cb\t\xff\x02': 
        general_function.print_term_and_write_log(send)
        quality_reg_function.get_quality_register(send, ser, dict_device,)
        # OBIS код - 0.0.99.98.10.255 Журнал Состояний дискретных входов и выходов. Запрос значений журнала Состояний дискретных входов и выходов
    elif send[14:23] == b'\x00\x07\x00\x00cb\n\xff\x02': 
        general_function.print_term_and_write_log(send)
        in_out_reg_function.get_input_output_register(send, ser, dict_device,)
        # OBIS код - 0.0.99.98.13.255 Журнал коррекции времени. Запрос значений журнала коррекции времени
    elif send[14:23] == b'\x00\x07\x00\x00cb\r\xff\x02':
        general_function.print_term_and_write_log(send)
        time_correct_reg_function.get_time_correction_register(send, ser, dict_device,)

    #general_function.print_term_and_write_log(datetime.utcnow().strftime("%S"))
    else:
        
        general_function.print_term_and_write_log('Это OBIS-код не обработан')
        general_function.print_term_and_write_log(send)
    
    #sleep(0.1)

      

    
# Получение архивов и журналов

def main():
    
    #delete_archive.delete_archive_list()
    ser = general_function.initSerial()
    ser.open()
    dict_device = general_function.creat_dict_device()
    while True:
        send_all = b''
        len_send_all = -2
        checking_the_message = False
        while ser.inWaiting()==0:
            pass
        
        while True:    
            num_breake = 0
            while ser.inWaiting()==0:
                sleep(0.05)
                num_breake+=1
                if num_breake == 2400:
                    general_function.print_term_and_write_log('Нет данных от УСПД, проверьте соединение')
                    ser.close()
                    sleep(0.5)
                    ser.open()
                    num_breake = 0

            send = ser.read()#_until(b'~')#.rstrip(b'~')
            send_all += send

            if send_all[0] != 126:
                send_all = b''

            elif len(send_all) == 4 and send_all[0] == 126:
                if send_all[1] == 126:
                    len_send_all = send_all[3]
                    send_all = send_all[1:]
                else:
                    len_send_all = send_all[2]

            elif len(send_all)>128 or (len(send_all)==len_send_all+2 and send != b'~'):
                general_function.print_term_and_write_log('Ошибка длинны сообщения или флага конца сообщения')
                general_function.print_term_and_write_log(send_all)
                send_all = b''
                break

            elif send == b'':
                general_function.print_term_and_write_log('Нет связи с УСПД, проверьте соединение')
                send_all = b''
                break

            elif len(send_all)==len_send_all+2 and send == b'~':
                send_all = send_all.strip(b'~')
                break
            
        
        try:
            checking_the_message = str(send_all[3]) in dict_device.keys()
        except IndexError:
            general_function.print_term_and_write_log('Неверный формат сообщения')
            general_function.print_term_and_write_log(send_all)
            continue
        
        if checking_the_message:
            reply_message(send_all, dict_device, ser)
            send = b''
            send_all = b''
        else:
            general_function.print_term_and_write_log('Непредвиденный сбой обмена')
            general_function.print_term_and_write_log(send_all)
            send = b''
            send_all = b''
        #sleep(0.1)
        #ser.close()
        
if __name__ == "__main__":
    
    main()