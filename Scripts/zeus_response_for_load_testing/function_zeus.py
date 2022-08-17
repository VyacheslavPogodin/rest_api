
from datetime import datetime
import socket
import binascii
import general_function

host= '10.10.29.127'
port=4052
buffer=65536

def parser_send(data):
    data_hex = binascii.hexlify(data).upper()
    data = data[:-2]
    list_measuring_type = {
        '00': 'PHASE_VOLTAGE_A',
        '01': 'PHASE_VOLTAGE_B',
        '02': 'PHASE_VOLTAGE_C',
        '03': 'PHASE_AMPERAGE_A',
        '04': 'PHASE_AMPERAGE_B',
        '05': 'PHASE_AMPERAGE_C',
        '06': 'FREQUENCY_VOLTAGE',
        '07': '07',
        '08': '08',
        '09': 'POWER_COEFFICIENT_PHASE_A',
        '10': 'POWER_COEFFICIENT_PHASE_B',
        '11': 'POWER_COEFFICIENT_PHASE_C',
        '13': 'ANGLE_BETWEEN_PHASE_VOLTAGES_A_B',
        '12': '12',
        '14': 'ANGLE_BETWEEN_PHASE_VOLTAGES_A_C',
        '15': 'ANGLE_BETWEEN_PHASE_VOLTAGES_B_C',
        '16': 'ACTIVE_POWER_A',
        '17': 'ACTIVE_POWER_B',
        '18': 'ACTIVE_POWER_C',
        '19': 'REACTIVE_POWER_A',
        '20': 'REACTIVE_POWER_B',
        '21': 'REACTIVE_POWER_C',
        '22': 'SUM_POWER'
}
    # Статус отчета
    status_response = {'00': 'Опция не найдена', '01':'Команда выполнена','03': 'Неверное состояние опции', '04': 'Недопустимая команда', '05': 'Неверная длина "параметры команды опции" в сообщении-запросе', '06': 'Недопустимое значение параметра команды', }
    # Тип отчета
    report_type = {'01' : 'Исполнено успешно с отчетом', '02':"Исполнено успешно без отчёта", '07':'Завершено по тайм-ауту', '33':'Команда не поддерживается измерительным прибором'}

    code_option_comand = {'11':'Получить параметры управления реле нагрузки и его состояние', '10':'Установить параметры управления реле нагрузки и его состояние', '15':'Получить результат и условия задачи на установку тарифного расписания',}

    print('\033[33m{}'.format('Сообщение: '), '\033[0m{}'.format(data_hex.decode().upper()))
    if binascii.hexlify(data[5:13]) == b'0100000000000000':
        send_print = '\033[0m{}'.format('Длинна сообщения: ')+ '\033[32m{}'.format(data[3])
        send_print = send_print + '\033[0m{}'.format('  EUI отправителя: ')+ '\033[32m{}'.format(binascii.hexlify(data[5:13]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  id опции: ')+ '\033[32m{}'.format(binascii.hexlify(data[13:15]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  Статус: ')+ '\033[32m{}'.format(status_response[str(data[15]).zfill(2)])
        send_print = send_print + '\033[0m{}'.format('  Атрибут команды опции: ')+ '\033[32m{}'.format(binascii.hexlify(data[16:17]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  Код команды опции: ')+ '\033[32m{}'.format(binascii.hexlify(data[17:18]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  Тип отчета: ')+ '\033[32m{}'.format(report_type[str(data[18]).zfill(2)])
        send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}\033[0m'.format(binascii.hexlify(data[19:20]).decode().upper())

    else:
        
        send_print = '\033[0m{}'.format('Длинна сообщения: ')+ '\033[32m{}'.format(data[3])
        send_print = send_print + '\033[0m{}'.format('  EUI отправителя: ')+ '\033[32m{}'.format(binascii.hexlify(data[5:13]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  id опции: ')+ '\033[32m{}'.format(binascii.hexlify(data[13:15]).decode().upper())
        send_print = send_print + '\033[0m{}'.format('  Статус: ')+ '\033[32m{}'.format(status_response[str(data[15]).zfill(2)])
        send_print = send_print + '\033[0m{}'.format('  Атрибут команды опции: ')+ '\033[32m{}'.format(binascii.hexlify(data[16:17]).decode().upper())
        
# Парсер запроса состояния реле
        if binascii.hexlify(data[17:18]).decode() == '11': 
            send_print = send_print + '\033[m{}'.format('  Код команды опции: ')+ '\033[32m{}\033[0m'.format(code_option_comand[binascii.hexlify(data[17:18]).decode()])
            if binascii.hexlify(data[18:19]).decode().upper() == '01':
                send_print = send_print + '\033[0m{}'.format('  Тип отчета: ')+ '\033[32m{}'.format(report_type[str(data[18]).zfill(2)])
                send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}'.format(binascii.hexlify(data[19:20]).decode().upper())
                DATE = str(data[24]).zfill(2) +'-'+ str(data[23]).zfill(2) +'-20'+ str(data[22]).zfill(2)
                TIME = str(data[25]).zfill(2) +':'+ str(data[26]).zfill(2) +':'+ str(data[27]).zfill(2)
                send_print = send_print + '\033[0m{}'.format('  DATE : ')+ '\033[32m{}'.format(DATE)
                send_print = send_print + '\033[0m{}'.format('  TIME : ')+ '\033[32m{}'.format(TIME)
                if data[28] == 0:
                    send_print = send_print + '\033[0m{}'.format('  OUTPUT_STATE: ')+ '\033[32m{}'.format('Не задан')
                    n=1
                else:
                    n=0
                    send_print = send_print + '\033[0m{}'.format('  OUTPUT_STATE: ')+ '\033[32m{}'.format(binascii.hexlify(data[29:30]).decode())
                
                if data[30-n] == 0:
                    send_print = send_print + '\033[0m{}'.format('  CONTROL_STATE: ')+ '\033[32m{}'.format('Не задан')
                    n+=1
                else:
                    send_print = send_print + '\033[0m{}'.format('  CONTROL_STATE: ')+ '\033[32m{}'.format(binascii.hexlify(data[31:32]).decode())
                
                if data[32-n] == 0:
                    send_print = send_print + '\033[0m{}'.format('  CONTROL_MODE: ')+ '\033[32m{}'.format('Не задан')
                    n+=1
                else:
                    send_print = send_print + '\033[0m{}'.format('  CONTROL_MODE: ')+ '\033[32m{}'.format(binascii.hexlify(data[33:34]).decode())
                
                if data[34-n] == 0:
                    send_print = send_print + '\033[0m{}'.format('  POWER_LIMIT_VALUE: ')+ '\033[32m{}'.format('Не задан')
                    n+=1
                else:
                    send_print = send_print + '\033[0m{}'.format('  POWER_LIMIT_VALUE: ')+ '\033[32m{}\033[0m'.format(float(data[38] + data[39]*256 + data[40]*(256**2) + data[41]*(256**3)+ data[42]*(256**4)+ data[43]*(256**5)) +(data[36]/65536+data[37]/256))

#Парсер команды на установку состояния реле  5501AB0F00000000000150AEA9010301001002AAA80E
        
        elif binascii.hexlify(data[17:18]).decode() == '10' and binascii.hexlify(data[13:15]).decode().upper()== '0103':
            send_print = send_print + '\033[m{}'.format('  Код команды опции: ')+ '\033[32m{}\033[0m'.format(code_option_comand[binascii.hexlify(data[17:18]).decode()])
            send_print = send_print + '\033[0m{}'.format('  Тип отчета: ')+ '\033[32m{}'.format(report_type[str(data[18]).zfill(2)])
            send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}\033[0m'.format(binascii.hexlify(data[19:20]).decode().upper())

# Парсер команды Получить тарифное расписание
        elif binascii.hexlify(data[17:18]).decode() == '15':
            if binascii.hexlify(data[18:19]).decode().upper() == '0A':
                send_print = send_print + '\033[31m{}\033[0m'.format('  Информация о задаче на установку тарифного расписания не найдена в базе ')
                send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}'.format(binascii.hexlify(data[19:20]).decode().upper())
                DATE = str(data[24]).zfill(2) +'-'+ str(data[23]).zfill(2) +'-20'+ str(data[22]).zfill(2)
                TIME = str(data[25]).zfill(2) +':'+ str(data[26]).zfill(2) +':'+ str(data[27]).zfill(2)
                send_print = send_print + '\033[0m{}'.format('  DATE : ')+ '\033[32m{}'.format(DATE)
                send_print = send_print + '\033[0m{}'.format('  TIME : ')+ '\033[32m{}'.format(TIME)
            else:
                send_print = send_print + '\033[m{}'.format('  Код команды опции: ')+ '\033[32m{}\033[0m'.format(code_option_comand[binascii.hexlify(data[17:18]).decode()])
                send_print = send_print + '\033[0m{}'.format('  Тип отчета: ')+ '\033[32m{}'.format(report_type[str(data[18]).zfill(2)])
                send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}'.format(binascii.hexlify(data[19:20]).decode().upper())
                DATE = str(data[23]).zfill(2) +'-'+ str(data[22]).zfill(2) +'-20'+ str(data[21]).zfill(2)
                TIME = str(data[24]).zfill(2) +':'+ str(data[25]).zfill(2) +':'+ str(data[26]).zfill(2)
                send_print = send_print + '\033[0m{}'.format('  DATE : ')+ '\033[32m{}'.format(DATE)
                send_print = send_print + '\033[0m{}'.format('  TIME : ')+ '\033[32m{}'.format(TIME)
                for i in range(3):
                    DAY_TARIF = {'0': '  RD_TARIF ', '1': '  WD_TARIF ', '2':'  HD_TARIF '}
                    send_print = send_print + '\033[33m{}\033[0m'.format( DAY_TARIF[str(i)])
                    for y in range(data[28+i*(3*data[28]+1)]):
                        send_print = send_print + '\033[0m{}'.format('  TARIF: ')+ '\033[32m{}'.format(str(data[31+3*y+i*(3*data[28]+1)]))+ ' \033[0mTIME: ' + '\033[32m{}'.format(str(data[29+3*y+i*(3*data[28]+1)]).zfill(2)+':'+str(data[30+3*y+i*(3*data[28]+1)]).zfill(2))
                        NUW_INT_DATA = (32+3*y+i*(3*data[28]+1))
                if data[NUW_INT_DATA] != 0:
                    send_print = send_print + '\033[33m{}\033[0m'.format('  HOLIDAY: ')
                    for i in range(data[NUW_INT_DATA]):
                        send_print = send_print + ' \033[0mDATE: ' + '\033[32m{}'.format(str(data[NUW_INT_DATA+1+i*2]).zfill(2)+'-'+str(data[NUW_INT_DATA+2+i*2]).zfill(2))
                        NUW_INT_DATA_1 = NUW_INT_DATA+3+i*2
                NUW_INT_DATA_1 = NUW_INT_DATA
                if data[NUW_INT_DATA_1] != 0:
                    DATE = str(data[NUW_INT_DATA_1+4]).zfill(2) +'-'+ str(data[NUW_INT_DATA_1+3]).zfill(2) +'-20'+ str(data[NUW_INT_DATA_1+2]).zfill(2)
                    TIME = str(data[NUW_INT_DATA_1+5]).zfill(2) +':'+ str(data[NUW_INT_DATA_1+6]).zfill(2) +':'+ str(data[NUW_INT_DATA_1+7]).zfill(2)
                    send_print = send_print + '\033[0m{}'.format(' ACTIVATING DATE : ')+ '\033[32m{}'.format(DATE)
                    send_print = send_print + '\033[0m{}'.format(' TIME : ')+ '\033[32m{}\033[0m'.format(TIME)
                
        elif binascii.hexlify(data[17:18]).decode() == '10' and binascii.hexlify(data[13:15]).decode().upper()== '0B01':

            if binascii.hexlify(data[18:19]).decode().upper() == '1A':
                send_print = send_print + '\033[31m{}\033[0m'.format('  Не удалось получить параметр качества электрической энергии: ')
                send_print = send_print +'\033[0m{}'.format(' '+list_measuring_type[str(data[31]).zfill(2)])
            elif binascii.hexlify(data[18:19]).decode().upper() == '01':
                send_print = send_print + '\033[0m{}'.format('  Тип отчета: ')+ '\033[32m{}'.format(report_type[str(data[18]).zfill(2)])
                send_print = send_print + '\033[0m{}'.format('  id опции прибора: ')+ '\033[32m{}'.format(binascii.hexlify(data[19:21]).decode().upper())
                send_print = send_print + '\033[0m{}'.format('  sequence: ')+ '\033[32m{}'.format(binascii.hexlify(data[21:22]).decode().upper())
                DATE = str(data[26]).zfill(2) +'-'+ str(data[25]).zfill(2) +'-20'+ str(data[24]).zfill(2)
                TIME = str(data[27]).zfill(2) +':'+ str(data[28]).zfill(2) +':'+ str(data[29]).zfill(2)
                send_print = send_print + '\033[0m{}'.format('  DATE : ')+ '\033[32m{}'.format(DATE)
                send_print = send_print + '\033[0m{}'.format('  TIME : ')+ '\033[32m{}'.format(TIME)
                send_print = send_print + '\033[0m{}'.format(' '+list_measuring_type[str(data[35]).zfill(2)]+': ')+ '\033[32m{}'.format(float(data[38] + data[39]*256 + data[40]*(256**2) + data[41]*(256**3)+ data[42]*(256**4)+ data[43]*(256**5)) +(data[36]/65536+data[37]/256))
                
        
        if binascii.hexlify(data[18:19]).decode().upper() == '02':
            print(send_print)
            print('\n\t\033[36mСообщение приняты полностью\033[0m')
            send_print = ''
        #b'5501AB100021841F16006F0D00 0B01 0000 10 18 0203 A7AB'
        #'5501AB27 00 000000000150AEA90B01010010013201180001160701072611 0000 02 02 03 00 0000000000000000 7EBF'
    print(send_print)


def send_answer(send):
    return general_function.crc16(binascii.unhexlify('01AB'+general_function.len_send(send)))


def socket_connect(EUI_DEV, send_list, ):
    sock = socket.socket()  #socket.AF_INET, socket.SOCK_DGRAM, 0
    sock.connect((host, port))
    
    for i in send_list:
        if i[:16] == '0100000000000000':
            sock.settimeout(2)
            send = i
        else:
            sock.settimeout(50)
            send = EUI_DEV + i
        send_out = binascii.hexlify((b'U'+send_answer(send))).upper()
        print('\n\r'+datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")+'\n\nTX:    '+send_out.decode().upper()+'\n\r')
        sock.send(b'U'+send_answer(send))
        RIAD = True
        with open('Zevs_response.log', 'a') as outfile:
            outfile.write( '\n\r'+datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S\n\r"+'TX:    '+send_out.decode().upper()+'\n\r'))

        while RIAD:
            try:
                data = sock.recv(buffer)
                #send_in = binascii.hexlify(data).upper()
                #print('RX:    ',send_in)
                parser_send(data)
            except TimeoutError:
                RIAD = False

            #with open('Zevs_response.log', 'a') as outfile:
            #    outfile.write('RX:    '+send_in.decode().upper()+'\n')
    sock.close()