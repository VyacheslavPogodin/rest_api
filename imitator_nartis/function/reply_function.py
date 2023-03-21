from time import sleep
import collections
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
from function import test_get_relay



def reply_message(send:bytes, dict_device:dict, ser)-> None:
    #dict_device = dict_device
    number_position = 1
    if send == b"":
        return
    else:
        try:
            serial_number_dev = dict_device[str(send[number_position+3])]
        except IndexError as e:
            with open("IndexError.log", 'a') as outfile:
                outfile.write(str(send) +'  '+ f'  {e} ')
            
    # Команда на начало обмена и окончание обмена    7ea04d02214132a5e7e6e600c001c1 00070100620100ff0201010204020412000809060000010000ff0f02120000090c07e60c11060a1e02ff800000090c07e7010100000001ff800000010069397e
        match send:
            case bytes(send) if send[number_position+5:number_position+6] == b'\x93': # PING   
                general_function.print_term_and_write_log(f'Открытие сессии dlms, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.assotiate_dlms(send,)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)

            case bytes(send) if send[number_position+5:number_position+6] == b'S': # PING   
                general_function.print_term_and_write_log(f'Закрытие сессии dlms, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.assotiate_dlms(send,)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)
        
        # associate response с паролем для чтения данных 111       
            case bytes(send) if send[number_position+4:number_position+6] == b'A\x10':
                general_function.print_term_and_write_log(f'Аутентификация в режиме Чтения, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.auth_dlms_password(send)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)

            case bytes(send) if send[number_position+4:number_position+6] == b'a\x10':
                general_function.print_term_and_write_log(f'Аутентификация в режиме Конфигурирования, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                connect_dlms.auth_dlms_cripto(send, ser, dict_device,)

    # OBIS код запроса серийного номера  OBIS-код 0.0.96.1.0.255              
            case bytes(send) if send[number_position+16:number_position+23] == b'\x00\x00`\x01\x00\xff\x02': 
                general_function.print_term_and_write_log(f'Запрос серийного номера, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.get_serial_number(send, serial_number_dev,)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)
            
            # OBIS код запроса даты и времени OBIS-код 0.0.1.0.0.255
            case bytes(send) if send[number_position+4:number_position+6] == b'A2' and send[number_position+16:number_position+23] == b'\x00\x00\x01\x00\x00\xff\x02':
                general_function.print_term_and_write_log(f'Получение даты и времени, адрес {send[number_position+3]}')  
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.get_date(send,)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)

            # OBIS код установки даты и времени OBIS-код 0.0.1.0.0.255
            case bytes(send) if send[number_position+4:number_position+6] == b'aT' and send[number_position+16:number_position+23] == b'\x00\x00\x01\x00\x00\xff\x02':  
                general_function.print_term_and_write_log(f'Установка даты и времени, адрес {send[number_position+3]}')  
                general_function.print_term_and_write_log(send, )
                answer = connect_dlms.set_date(send,)
                ser.write(answer)
                general_function.print_term_and_write_log(answer)

        # Запрос списка объектов архивов    

            # OBIS код - 1.0.98.2.0.255 03 Журнал ежесуточных показаний. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00b\x02\x00\xff\x03':
                general_function.print_term_and_write_log(f'Получение суточного архива OBIS 1.0.98.2.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                day_function.get_day_archive_object(send, ser, dict_device,)
            # OBIS код - 1.0.99.2.0.255 03 Журнал часовых показаний. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00c\x02\x00\xff\x03':
                general_function.print_term_and_write_log(f'Получение часового архива OBIS 1.0.99.2.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                hourly_function.get_hourly_archive_object(send, ser, dict_device,)
            # OBIS код - 1.0.98.1.0.255 03 Журнал ежемесячных показаний.
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00b\x01\x00\xff\x03':
                general_function.print_term_and_write_log(f'Получение месячного архива OBIS 1.0.98.1.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                monthly_function.get_monthly_archive_object(send, ser, dict_device,)
        # Запрос списка объектов профиля

            # OBIS код - 0.0.99.1.0.255 03 Журнал Профиль 1. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00c\x01\x00\xff\x03':
                general_function.print_term_and_write_log(f'Получение профиля нагрузки OBIS 1.0.99.1.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                load_profile_function.get_load_profile_object(send, ser, dict_device,)
        # Запрос списка объектов журналов

            # OBIS код - 0.0.99.98.0.255 03 Журнал напряжений. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x00\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала напряжений> OBIS 1.0.99.98.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                volt_reg_function.get_voltage_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.1.255 03 Журнал токов. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x01\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала токов> OBIS 1.0.99.98.1.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                current_reg_function.get_current_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.2.255 03 Журнал включений/выключений.
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x02\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала включений/выключений> OBIS 1.0.99.98.2.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                on_off_reg_function.get_on_off_and_relay_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.3.255 03 Журнал коррекции данных.
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x03\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала коррекции данных> OBIS 1.0.99.98.3.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                reconfig_reg_function.get_reconfig_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.4.255 03 Журнал Внешних воздействий. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x04\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала внешних воздействий> OBIS 1.0.99.98.4.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                external_events_function.get_external_events_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.5.255 03 Журнал Коммуникационные события. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x05\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала коммуникационные события> OBIS 1.0.99.98.5.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                com_events_function.get_communication_events_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.6.255 03 Журнал контроль доступа. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x06\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала контроль доступа> OBIS 1.0.99.98.6.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                access_events_function.get_access_events_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.7.255 03 Журнал Самодиагностики. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x07\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала самодиагностики> OBIS 1.0.99.98.7.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                diagnostics_events_function.get_diagnostics_events_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.8.255 03 Журнал Превышение тангенса. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x08\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала превышение тангенса> OBIS 1.0.99.98.8.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                tangent_reg_function.get_tangent_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.9.255 03 Журнал Параметры качества сети. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\t\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала параметры качества сети> OBIS 1.0.99.98.9.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                quality_reg_function.get_quality_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.10.255 03 Журнал Состояний дискретных входов и выходов. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\n\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала состояний дискретных входов и выходов> OBIS 1.0.99.98.10.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                in_out_reg_function.get_input_output_register_object(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.13.255 03 Журнал коррекции времени. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\r\xff\x03':
                general_function.print_term_and_write_log(f'Получение <Журнала коррекции времени> OBIS 1.0.99.98.13.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                time_correct_reg_function.get_time_correction_register_object(send, ser, dict_device,)

        # Запрос списка масштабов

            # OBIS код - 1.0.94.7.2.255 Профиль масштаба для журнала ежесуточных показаний . Запрос списка объектов дневного архива
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00^\x07\x02\xff\x02':
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                day_function.get_day_archive_scale(send, ser, dict_device,)    
            # OBIS код - 1.0.94.7.1.255 Профиль масштаба для журнала часовых показаний . Запрос списка масштабов часового архива
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00^\x07\x01\xff\x02':
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                hourly_function.get_hourly_archive_scale(send, ser, dict_device,) 
            # OBIS код - 1.0.94.7.4.255 Профиль масштаба для получасового профиля 1 . Запрос масштабов объектов профиля 1
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00^\x07\x04\xff\x02':
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                load_profile_function.get_load_profile_scale(send, ser, dict_device,)
            # OBIS код - 1.0.94.7.1.255 Профиль масштаба для журнала напряжений. Запрос списка объектов журнала напряжений
            #case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00^\x07\x01\xff\x02':
            #    volt_reg_function.get_voltage_register_scale(send, ser, dict_device,)




        # Получение значений архивов

            # OBIS код - 1.0.98.2.0.255 Журнал ежесуточных показаний. Запрос списка объектов дневного архива
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00b\x02\x00\xff\x02':
                general_function.print_term_and_write_log(f'Получение суточного архива OBIS 1.0.98.2.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                day_function.get_day_archive(send, ser, dict_device,)
            # OBIS код - 1.0.99.2.0.255 Журнал часовых показаний. Запрос списка объектов часового архива
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00c\x02\x00\xff\x02': 
                general_function.print_term_and_write_log(f'Получение часового архива OBIS 1.0.99.2.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                hourly_function.get_hourly_archive(send, ser, dict_device,)
            # OBIS код - 1.0.98.1.0.255 Журнал месячных показаний. Запрос списка объектов месячного архива
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00b\x01\x00\xff\x02':
                general_function.print_term_and_write_log(f'Получение месячного архива OBIS 1.0.98.1.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                monthly_function.get_monthly_archive(send, ser, dict_device,)
        # Запрос значений профиля    

            # OBIS код - 1.0.99.2.0.255 Журнал получасовой профиль нагрузок. Запрос профиля нагрузок
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00c\x01\x00\xff\x02':
                general_function.print_term_and_write_log(f'Получение профиля нагрузки OBIS 1.0.99.1.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                load_profile_function.get_load_profile(send, ser, dict_device,)

        # Запрос значений журналов    
            # OBIS код - 0.0.99.98.0.255 Журнал напряжений. Запрос значений журнала напряжений
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x00\xff\x02': 
                general_function.print_term_and_write_log(f'Получение <Журнала напряжений> OBIS 1.0.99.98.0.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                volt_reg_function.get_voltage_register(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.1.255 Журнал токов. Запрос значений журнала токов
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x01\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала токов> OBIS 1.0.99.98.1.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                current_reg_function.get_current_register(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.2.255 Журнал включений/выключений. Запрос значений журнала включений/выключений
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x02\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала включений/выключений> OBIS 1.0.99.98.2.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                on_off_reg_function.get_on_off_and_relay_register(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.3.255 Журнал коррекции данных. Запрос значений журнала коррекции данных
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x03\xff\x02': 
                general_function.print_term_and_write_log(f'Получение <Журнала коррекции данных> OBIS 1.0.99.98.3.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                reconfig_reg_function.get_reconfig_register(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.4.255 Журнал Внешних воздействий. Запрос значений журнала Внешних воздействий
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x04\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала внешних воздействий> OBIS 1.0.99.98.4.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                external_events_function.get_external_events(send, ser, dict_device,)        
            # OBIS код - 0.0.99.98.5.255 Журнал Коммуникационные события. Запрос значений журнала Коммуникационные события
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x05\xff\x02':  
                general_function.print_term_and_write_log(f'Получение <Журнала коммуникационные события> OBIS 1.0.99.98.5.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                com_events_function.get_communication_events(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.6.255 Журнал контроль доступа. Запрос значений журнала контроль доступа
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x06\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала контроль доступа> OBIS 1.0.99.98.6.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                access_events_function.get_access_events(send, ser, dict_device,)
            # OBIS код - 0.0.99.98.7.255 Журнал Самодиагностики. Запрос значений журнала Самодиагностики
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x07\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала самодиагностики> OBIS 1.0.99.98.7.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                diagnostics_events_function.get_diagnostics_events(send, ser, dict_device,)
                # OBIS код - 0.0.99.98.8.255 Журнал Превышение тангенса. Запрос значений журнала Превышение тангенса
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\x08\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала превышение тангенса> OBIS 1.0.99.98.8.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                tangent_reg_function.get_tangent_register(send, ser, dict_device,)
                # OBIS код - 0.0.99.98.9.255 Журнал Параметры качества сети. Запрос значений журнала Параметры качества сети
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\t\xff\x02': 
                general_function.print_term_and_write_log(f'Получение <Журнала параметры качества сети> OBIS 1.0.99.98.9.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                quality_reg_function.get_quality_register(send, ser, dict_device,)
                # OBIS код - 0.0.99.98.10.255 Журнал Состояний дискретных входов и выходов. Запрос значений журнала Состояний дискретных входов и выходов
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\n\xff\x02': 
                general_function.print_term_and_write_log(f'Получение <Журнала состояний дискретных входов и выходов> OBIS 1.0.99.98.10.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                in_out_reg_function.get_input_output_register(send, ser, dict_device,)
                # OBIS код - 0.0.99.98.13.255 Журнал коррекции времени. Запрос значений журнала коррекции времени
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x00\x00cb\r\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Журнала коррекции времени> OBIS 1.0.99.98.13.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
                time_correct_reg_function.get_time_correction_register(send, ser, dict_device,)

            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x07\x01\x00^\x07\x00\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Параметров качества> OBIS 1.0.99.98.13.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                quality_reg_function.get_quality_stop_cadr(send, ser, dict_device,)

            case bytes(send) if send[number_position+14:number_position+23] == b'\x00\x03\x01\x00Q\x07\n\xff\x02':
                general_function.print_term_and_write_log(f'Получение <Фаз напряжения> OBIS 1.0.81.07.10.255, адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send, )
                quality_reg_function.get_quality_faze(send, ser, dict_device,)

        # Запросы состояния реле

            # OBIS код - 1.0.96.3.10.255 02 Состояние реле, булевое значение. 
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00F\x00\x00`\x03\n\xff\x02': 
                general_function.print_term_and_write_log(f'Получение <Состояния реле> , адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send)
                test_get_relay.get_relay(send, ser, )
                    
            # OBIS код - 1.0.96.3.10.255 04 Состояние реле mode, булевое значение
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00F\x00\x00`\x03\n\xff\x04':
                general_function.print_term_and_write_log(f'Получение <MODE реле> , адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send)
                test_get_relay.get_relay_mode(send, ser, )
            
            # OBIS код - 1.0.96.3.10.255 03 Состояние реле state, булевое значение
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00F\x00\x00`\x03\n\xff\x03': 
                general_function.print_term_and_write_log(f'Получение <State реле> , адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send)
                test_get_relay.get_relay_state(send, ser, )

            # OBIS код - 1.0.96.3.10.255 03 Значение лимитера,
            case bytes(send) if send[number_position+14:number_position+23] == b'\x00G\x00\x00\x11\x00\x00\xff\x04': 
                general_function.print_term_and_write_log(f'Получение <Значение лимитера> , адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send)
                test_get_relay.get_limiter_val(send, ser, )    

                # OBIS код - 1.0.96.3.10.255 03 Значение времени действия лимитера, булевое значение
            case bytes(send) if send[number_position+14:number_position+23] in (b'\x00G\x00\x00\x11\x00\x00\xff\x06', b'\x00G\x00\x00\x11\x00\x00\xff\x07'): 
                general_function.print_term_and_write_log(f'Получение <Значение времени действия лимитера> , адрес {send[number_position+3]}')
                general_function.print_term_and_write_log(send) 
                test_get_relay.get_time_limiter(send, ser, )

            case _:
                
                general_function.print_term_and_write_log('Это OBIS-код не обработан')
                #general_function.print_term_and_write_log('\t\t'+ str(send[number_position+47]*256+send[number_position+48])+'-'+str(send[number_position+49]).zfill(2)+'-'+str(send[number_position+50]).zfill(2)+' '+str(send[number_position+52]).zfill(2)+':'+str(send[number_position+53]).zfill(2)+':'+str(send[number_position+54]).zfill(2)) 
                general_function.print_term_and_write_log(send, )
    
    sleep(0.1)