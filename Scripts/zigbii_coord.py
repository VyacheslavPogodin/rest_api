
# from time import sleep, time
import serial
from time import sleep
import binascii
import crc8

channel = '0B'
pid = '1111'
epid_USPD = '747070536D617274' # 0101199701011999  747070536D617274
epid_target = '0000062301000031'
command_for_uspd = '010111111111000000000000000000' #код каманды 0x01, 0x01 + тэг команды 4 любых байта + статус (в запросе не используется) + резерв 8 байт
command_for_meter = '0701000010' #идентификатор опции 0x0107, атрибут команды 0x00, тип отчета 0x00, код команды 0x10

EUI_DEV_LIST = ['4673C2FEFF313AB4',]# '709EF8FEFF8D79E0', '5A645D16006F0D00', '0F255C16006F0D00', 'C4F01016006F0D00', '0FA0F8FEFF8D79E0',]#,C21B21FEFF693494 '0F255C16006F0D00' '0FA0F8FEFF8D79E0' '3211FC16006F0D00' '709EF8FEFF8D79E0' '21841F16006F0D00' 9B04A514006F0D00  EC64A7FEFF8D79E0, EEA06A16006F0D00 'E7B99600006F0D00'
#ramina 'FA20EC03006F0D00' , 4982B30B006F0D00 , 81C4B716006F0D00, 21841F16006F0D00, 5A645D16006F0D00, 0F255C16006F0D00 AA 01 05 08 6A FC 96 17 00 6F 0D 00 CB 

comport = 'COM16'
# 434 expanidset C21B21FEFF693494 0101199701011997
# AA01AB15C21B21FEFF69349407010000103031303131393937FF
# AA01AB15C21B21FEFF69349407010000100101199701011997F


def get_send_for_uspd(eui_uspd_fun:str = 'FFFFFFFFFFFFFFFF', command_for_uspd_fun:str = command_for_uspd, epid_fun:str = epid_USPD, channel_fun:str = channel, pid_fun:str=pid) -> list:

    return [binascii.unhexlify(f'AA011908{eui_uspd_fun}BA'),
            binascii.unhexlify('AA')+crc(binascii.unhexlify(b'01B0' + len_send(eui_uspd_fun + command_for_uspd_fun + epid_fun + eui_uspd_fun + channel_fun + pid_fun).encode())),
            binascii.unhexlify('AA')+crc(binascii.unhexlify(b'010900')),
    ]

def get_send_for_meter(EUI_METER:str ,  command_for_meter_fun:str = command_for_meter, epid_fun:str = epid_target,) -> bytes:

    return binascii.unhexlify('AA') + crc(binascii.unhexlify(b'01AB' + len_send(EUI_METER + command_for_meter_fun + epid_fun).encode()))



def parser_meter_send(data):
    
    data_hex = binascii.hexlify(data)
    print('\033[33m Сообщение: ' + '\033[37m{}'.format(data_hex.upper().decode()))
    send_print = '\033[33m MAC: ' + '\033[37m{}'.format(binascii.hexlify(data[4:12]).upper().decode())
    send_print = send_print + '\033[33m Статус:' + '\033[37m{}'.format(
        binascii.hexlify(data[14:15]).upper().decode())
    send_print = send_print + '\033[33m EPID:' + '\033[37m{}'.format(binascii.hexlify(data[17:26]).upper().decode())
    
    print(send_print)


def parser_uspd_send(data):
    data_hex = binascii.hexlify(data)
    print('\033[33m Сообщение: ' + '\033[37m{}'.format(data_hex.upper().decode()))
    #могут приходить два вида ответа: формата AA01090C1911110101199701011997FF59 и формата AA01B02AD01A1116006F0D000101111111110100000000000000000101199701011997D01A1116006F0D0019111179
    if data[2:3] == b'\x09':
        i_channel = 4
        i_epid = 7
    else:
        i_channel = 43
        i_epid = 27
    send_print = '\033[0m Канал: ' + '\033[32m{}'.format(binascii.hexlify(data[i_channel:i_channel+1]).upper().decode())
    send_print = send_print + '\033[0m PAN ID: ' + '\033[32m{}'.format(binascii.hexlify(data[i_channel+1:i_channel+3]).upper().decode())
    send_print = send_print + '\033[0m EPID: ' + '\033[32m{}\033[0m'.format(binascii.hexlify(data[i_epid:i_epid+8]).upper().decode())

    print(send_print)


def len_send(send):
    return format(len(send)//2, 'X').zfill(2)+send

def crc(send:bytes) -> bytes:
    import crc8
    return send+crc8.crc8(send).digest()  #hexdigest

def set_epid(ser):

    try: 
        starting_the_function_number = int(input('  1 - Установка EPID на координатор\n  2 - Отправка команды ПУ\n> ' ))
    except TypeError:
        set_epid()

    
    SEND_LIST_COORDIN_COM = get_send_for_uspd()
    
    match starting_the_function_number:

        #устанавливаем epid на УСПД
        case 1:
            for send_uspd in SEND_LIST_COORDIN_COM:
                try:
                    print('\033[33m Отправка пакета на УСПД: \033[0m')
                    print(binascii.hexlify(send_uspd).upper())
                    ser.write(send_uspd)
                    send_all =b''
                    while True:
                        while ser.inWaiting() == 0:
                            pass
                        send = ser.read()
                        if crc8.crc8(send_all.lstrip(b'\xaa')).digest() == send:
                            send_all += send
                            break

                        send_all += send
                    if send_all[2] == 25:
                        eui_uspd = binascii.hexlify(send_all[4:12])
                        print(eui_uspd.upper())
                        SEND_LIST_COORDIN_COM[1] = get_send_for_uspd(eui_uspd.decode().upper())[1]
                    else:
                        parser_uspd_send(send_all)

                except TimeoutError as err:
                    print('\033[31m{}'.format(f"The error '{err}' occurred"))
        
        #устанавливаем epid на ПУ
        case 2:
            for EUI_METER in EUI_DEV_LIST:
                data: bytes = b''
                print('\033[33m Отправка пакета на ПУ: ', '\033[37m', EUI_METER)
                send_meter = get_send_for_meter(EUI_METER)
                print(binascii.hexlify(send_meter).upper())
                ser.write(send_meter)
                send_all =b''
                while True:
                    while ser.inWaiting() == 0:
                        pass
                    send = ser.read()

                    if crc8.crc8(send_all.lstrip(b'\xaa')).digest() == send:
                        send_all += send
                        break

                    send_all += send

                print('RX:  ', binascii.hexlify(send_all).upper())
                parser_meter_send(data)
            


    #устанавливаем epid на УСПД
    # try:
    #     print('\033[33m Отправка пакета на УСПД: ')
    #     print(binascii.hexlify(send_uspd).upper())
    #     sock.send(send_uspd)
    #     data = sock.recv(1024)
    #     if data:
    #         parser_uspd_send(data)
    #     else:
    #         print('\033[31m Нет ответа')
    # except TimeoutError as err:
    #     print('\033[31m{}'.format(f"The error '{err}' occurred"))
        
  
#971C21FEFF693494, 21841F16006F0D00
if __name__ == '__main__':

    with serial.Serial(comport, 38400, timeout=10) as ser:
        

        set_epid(ser)

# AA01B02A7527A514006F0D000101000000000000000000000000003031303131393937FFFFFFFFFFFFFFFF 0B11112E 
# AA01B02A7527A514006F0D0001011111111100000000000000000001011997010119997527A514006F0D00 1911110B'