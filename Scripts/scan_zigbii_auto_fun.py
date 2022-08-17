
from time import sleep, time
import serial
import os

reboot =  b'reboot\r'
status = b'status\r'
scan = b'query_networks\r'
leave = b'leave\r' 
form = b'form "747070536D617274"\r'
query = b'query_neighbor\r'

target_network = ('13', '0x1799') #Параметры целевой сети
EUI_dev = '21841F16006F0D00'
comport = 'COM9'




def scaning_zigbee():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = comport
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    ser.timeout = 10
    ser.open()
    
    
    LIST_NETWORK = network_scanning(ser)

    for network_config in LIST_NETWORK:

        channel_set_config(ser, network_config)
        set_coordination(ser)

        n = 0
        while True:
            FIND_DEV_NET = finding_device(ser, network_config)
            n+=1
            if FIND_DEV_NET or n < 4:
                print('Устройство осталось в этой же сети')
            else:
                print('Устройство удалено из этой сети')
                break
            FIND = True
        FIND = False
    


    ser.close()
    return FIND



def network_scanning(ser):

    send = b''
    CH_PAN_ID = []
    print('\n\tНачинаем сканирование сетей\n')
    print('TX:    ',scan)
    ser.write(scan)
    while send != b'QQ query end QQ\r\n':
        send = ser.readline()
        print('RX:    ', send)
        if send.decode()[19:21].isdigit():
            CH_PAN_ID.append((send.decode()[19:21], send.decode()[29:35]))
    
    return set(CH_PAN_ID)



def channel_set_config(ser, net_conf):

    channel, pan = net_conf

    channel_set = b'set_channel '+channel.encode()+b'\r'#Команда на подключение к каналу
    pan_id = b'set_pan_id '+pan.encode()+b'\r'#Команда на подключение к PAN ID

    while True: #Цикл подключения к сети
        
        print('\n\tПокидаем текущую сеть\n')
        print('TX:    ',leave)
        ser.write(leave)# Покидаем сеть
        send = b''
        while send != b'Attempting leave action\r\n':
            send = ser.readline()
            print('RX:    ',send)

        print('\n\tУстанавливаем канал: '+channel+'\n')
        print('TX:    ',channel_set)
        ser.write(channel_set)
        send = ser.readline()
        print('RX:    ',send)

        print('\n\tУстанавливаем PAN ID: '+pan+'\n')
        print('TX:    ',pan_id)
        ser.write(pan_id)
        send = ser.readline()
        print('RX:    ',send)

        if send == b'Pan ID set to '+pan.encode()+b', channel is '+channel.encode()+b'\r\n':
            break
        else:
            print('\n\tСеть не соответствует требуемой, повторяем подключение \n')



def set_coordination(ser):

    print('\n\tПереводим устройство в режим координатора \n')
    print('TX:    ',form)
    set_status_90 = False
    while not set_status_90:
        ser.write(form)
        while True:
            send = ser.readline()
            print('RX:    ',send)
            if send == b'Stack status 90\r\n':
                set_status_90 = True
            if send in ( b'', b'Form network: 00\r\n', b'Stack status 91\r\n'):
                break



def finding_device(ser, net_conf):

    channel, pan = net_conf

    print('\n\tСканируем сеть '+channel+' Pan ID '+pan+' и проверяем наличие требуемого устройства \n')
    print('TX:    ',query)
    ser.write(query)
   
    while True:
        send = ser.readline()
        print('RX:    ',send)
        if send == b'QQ query end QQ\r\n':
            print('\n\tТребуемое устройство не найдено, переходим к следующей сети \n')
            FIND_DEVICE = False
            break
        elif send.decode().find(EUI_dev) != -1:
            print('\n\n\n\tУстройство находится в сети channel is '+channel+', Pan ID set to '+pan )
            drop_device(ser, net_conf)
            FIND_DEVICE = True
            break
    return FIND_DEVICE




def drop_device(ser, net_conf):

    channel, pan = net_conf

    if target_network == net_conf:
        print('\n\t\033[32mУстройство в требуемой сети! \033[0m\n')
        return True
    else:
        query_target = b'query_target "'+EUI_dev.encode()+b'"\r'
        print('\n\t\033[31mЗапрос на разрешение программирования целевого устройства \033[0m\n')
        ser.write(query_target)
        print('TX:    ',query_target)
        send = b''
        while send != b'QQ query end QQ\r\n':
            send = ser.readline()
            print('RX:    ',send)
        drop_status = True
        while drop_status:
            drop = b'drop_target "'+EUI_dev.encode()+b'"\r'
            print(f'\n\t\033[31mЗапрос на удаление устройства из сети channel is '+channel+', Pan ID set to '+pan+'\033[0m\n')
            ser.write(drop)
            print('TX:    ',drop)
            send = None
            
            while send not in (b'', b'DD Start node discovering DD\r\n', ):
                if send == b' Message has been sent to node with EUI: '+EUI_dev.encode()+b'\r\n':
                    drop_status = False
                send = ser.readline()
                print('RX:    ',send)
        return False


                        
#971C21FEFF693494, 21841F16006F0D00

if __name__ == '__main__':
    
    os.system('color')
    FIND = False
    while not FIND:
        FIND = scaning_zigbee()
    

#ramina 'FA20EC03006F0D00' , 4982B30B006F0D00 , 81C4B716006F0D00, 21841F16006F0D00, 5A645D16006F0D00, 0F255C16006F0D00
