
# from time import sleep, time
import serial
import os

EUI_scan = 'FADF9600006F0D00'

reboot =  b'reboot\r'
status = b'status\r'
scan = b'query_networks\r'
leave = b'leave\r' 
form = b'form "747070536D617274"\r'
query = b'query_neighbor\r'
join_network = b'join 0xFF\r'
role = b'get_id\r'


target_network = ('11', '0x1111', '') #Параметры целевой сети
EUI_dev = '3FA1F8FEFF8D79E0' #, '0F255C16006F0D00' '0FA0F8FEFF8D79E0' '3211FC16006F0D00' '709EF8FEFF8D79E0' '21841F16006F0D00' 9B04A514006F0D00  EC64A7FEFF8D79E0, EEA06A16006F0D00 'E7B99600006F0D00'
#ramina 'FA20EC03006F0D00' , 4982B30B006F0D00 , 81C4B716006F0D00, 21841F16006F0D00, 5A645D16006F0D00, 0F255C16006F0D00

comport = 'COM8'




def scaning_zigbee():
    with serial.Serial(comport, 115200, timeout=40) as ser:
    
        LIST_NETWORK = network_scanning(ser)

        for network_config in LIST_NETWORK:
            if network_config[0] == target_network[0] and network_config[1] == target_network[1]:
                STOP_STEP = False
            else:
                channel_set_config(ser, network_config) #Устанавливаем нужную сеть
                # if network_config[2] == 'NO match\r\n':
                set_coordination(ser, network_config)     #Если сеть закрыта то заходим в нее как координатор    
                # elif network_config[2] == 'MATCH\r\n':
                #     set_join(ser, network_config)
                # else:
                #     pass
                while True:
                    if finding_device(ser, network_config):
                        drop_device(ser, network_config, target_network)
                    else:
                        break

        channel_set_config(ser, target_network) #Устанавливаем целевую сеть
        set_coordination(ser, target_network)     #Если сеть закрыта то заходим в нее как координатор    
        STOP_STEP = finding_device(ser, target_network)
    return STOP_STEP


'SCAN: nwk found ch 26, panID 0x313D, xpan: 416E746F6E466174, lqi 255: NO match'

def network_scanning(ser):

    send = b''
    CH_PAN_ID = []
    print('\n\t\033[31mНачинаем сканирование сетей\033[0m\n')
    print('TX:    ',scan)
    ser.write(scan)
    while send != b'QQ query end QQ\r\n':
        send = ser.readline()
        print('RX:    ', send)
        if send.decode()[19:21].isdigit():
            CH_PAN_ID.append((send.decode()[19:21], send.decode()[29:35], send.decode()[70:]))
    
    return set(CH_PAN_ID) #(('11', '0x0204'),) 



def channel_set_config(ser, net_conf):  #Устанавливаем нужную сеть

    channel, pan, match_status = net_conf

    channel_set = b'set_channel '+channel.encode()+b'\r'#Команда на подключение к каналу
    pan_id = b'set_pan_id '+pan.encode()+b'\r'#Команда на подключение к PAN ID

    while True: #Цикл подключения к сети
        
        print('\n\t\033[31mПокидаем текущую сеть\033[0m\n')
        print('TX:    ',leave)
        ser.write(leave)# Покидаем сеть
        send = b''
        while send != b'Attempting leave action\r\n':
            send = ser.readline()
            print('RX:    ',send)

        print('\n\t\033[31mПерезагружаем устройство\033[0m\n')
        print('TX:    ',reboot)
        ser.write(reboot)# Перезагружаемся
        send = b''
        while send not in (b'Network init status 93\r\n' , b'Network init status 00\r\n'):
            send = ser.readline()
            print('RX:    ',send)
            if send == b'':
                break

        
        print('\n\t\033[31mУстанавливаем PAN ID: '+pan+'\033[0m\n')
        print('TX:    ',pan_id)
        ser.write(pan_id)
        send = ser.readline()
        print('RX:    ',send)

        print('\n\t\033[31mУстанавливаем канал: '+channel+'\033[0m\n')
        print('TX:    ',channel_set)
        ser.write(channel_set)
        send = ser.readline()
        print('RX:    ',send)

        print('\n\t\033[31mПроверяем роль роутера\033[0m\n')
        print('TX:    ',role)
        ser.write(role)
        while True:
            send = ser.readline()
            print('RX:    ',send)
            if send.decode().find('TxPower') !=-1:
                break
            
        if send.decode().find('Channel '+channel) !=-1 and send.decode().find('panId '+pan) !=-1:
            break
        else:
            print('\n\t\033[31mСеть не соответствует требуемой, повторяем подключение \033[0m\n')



def set_coordination(ser, network_config):

    print('\n\t\033[31mПереводим устройство в режим координатора \033[0m\n')
    print('TX:    ',form)
    set_status_90 = False
    while not set_status_90:
        ser.write(form)
        while True:
            send = ser.readline()
            print('RX:    ',send)
            if send == b'Form network: 00\r\n':
                set_status_90 = True
                break
            elif send in ( b'', b'Stack status 91\r\n', b'Scan error 3D\r\n', b'Error: send broadcast 0xA1\r\n'):
                channel_set_config(ser, network_config)
                break


def set_join(ser, net_conf):
    while True:
        print('\n\t\033[31mЗапрос на присоединение к открытой сети \033[0m\n')
        ser.write(join_network)
        print('TX:    ',join_network)
        send = b''
        while True:
            send = ser.readline()
            print('RX:    ',send)
            if send == b'Stack status 90\r\n':
                send = b'True'
                break
            elif send == b'':
                channel_set_config(ser, net_conf)
                break
        if send == b'True':
            break


def finding_device(ser, net_conf):

    channel, pan, match_status = net_conf
    discover = b'discover_node "'+EUI_dev.encode()+b'"\r'
    print('\n\t\033[33mПроверяем наличие требуемого устройства в сети channel is '+channel+', Pan ID set to '+pan+'\033[0m\n')
    print('TX:    ',discover)
    ser.write(discover)
    FIND_DEVICE = False
    while True:
        send = ser.readline()
        print('RX:    ',send)
        if send.decode().find(EUI_dev) != -1:
            print('\n\n\n\t\033[32mУстройство находится в сети channel is '+channel+', Pan ID set to '+pan + '\033[0m\n')
            FIND_DEVICE = True
        if send == b'QQ query end QQ\r\n' or send == b'':
            if not FIND_DEVICE:
                print('\n\t\033[33mТребуемое устройство не найдено, переходим к следующей сети \033[0m\n')
            break

    return FIND_DEVICE


def drop_device(ser, net_conf, tar_net):

    channel, pan, match_status = net_conf
    drop = b'drop_target "'+EUI_dev.encode()+b'"\r'
    close_net = b'join 0x00\r'

    print(f'\n\t\033[31mЗапрос на закрытие сети сети \033[0m\n')
    ser.write(close_net)
    print('TX:    ',close_net)
    send = ser.readline()
    print('RX:    ',send)

#    drop_all = b'drop_all\r'
    print(f'\n\t\033[31mЗапрос на удаление устройства из сети channel is '+channel+', Pan ID set to '+pan+'\033[0m\n')
    ser.write(drop)
    print('TX:    ',drop)
    send = None
    while True:
        send = ser.readline()
        print('RX:    ',send)
        if send == b' Message has been sent to node with EUI: '+EUI_dev.encode()+b'\r\n':
            print(f'\n\t\033[33mЗапрос на исключение устройства отправлен!\033[0m\n')
            break
        elif send == b'DD Node discovering has been canceled DD\r\n':
            # finding_device(ser, net_conf)
            break
        elif send == b'':
            break

                        
#971C21FEFF693494, 21841F16006F0D00

if __name__ == '__main__':
    
    os.system('color')
    FIND = False
    while not FIND:
        FIND = scaning_zigbee()


