
from datetime import datetime
import serial, os
import binascii
import psycopg2
from psycopg2 import OperationalError
'''
Имитатор счетчика Нартис Основные функции
'''

# Считываем номера устройств из БД
def assign_port():
    
    try:
        connection = psycopg2.connect(
            database='uspd',
            user='admin',
            password='kPZa83Uz2#0',
            host='10.10.29.110',
            port='5432',
        )
        #print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    cur = connection.cursor()

    cur.execute(
            f"SELECT address, serial, id_model, id_interface FROM meter_device"
        )
    device = cur.fetchall()
    cur.close()
    connection.close()
    
    return device


# Создание словаря с номером устройства и серийным номером
def creat_dict_device():
    
    device = assign_port()
    dict_device = {}
    
    for i in device:
        
        #adress = chr(((i[0]<<1))^1).encode()
        if i[3] != 5:
            adress = str((i[0]<<1)^1)
            if i[2] == 1:
                serial_number = str(i[1]).encode()
            elif i[2] == 2:
                serial_number = binascii.unhexlify(conv(str(i[1])).zfill(8))
            
            dict_device[str(adress)] = serial_number
    return dict_device


# Настройки подключение по RS_485
def initSerial():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM6'
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
    ser.timeout = None
    return ser

def conv(n,ri=10,ro=16):  #переводим из ri в ro
    digs="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=0
    for a in n:
        k=digs.find(a)
        acc=acc*ri+k
    res=""
    while(acc>0):
        k=acc%ro
        res=digs[k]+res
        acc=acc//ro
    return res


def crc16(data):
    
    crc = 0xFFFF #Init 
    l = len(data)
    i = 0
    while i < l:
        j = 0
        crc = crc ^ data[i]
        while j < 8:
            if (crc & 0x1):
                mask = 0x8408
            else:
                mask = 0x00
            crc = ((crc >> 1)) ^ mask
            
            j += 1
        i += 1
    if crc < 0:
       crc -= 256
    crc = crc ^ 0xFFFF
    
    return data + chr(crc % 256).encode('latin-1') + chr(crc // 256).encode('latin-1')

# Функция формирования значения длинны фрейма в байтах
def len_send(send):
    return binascii.unhexlify(conv(str(len(send)+10)).zfill(2))


def print_term_and_write_log(info_send):
    os.system('color')
    if type(info_send) == bytes:
        print("\033[33m{}".format(datetime.utcnow().strftime("%Y %m %d %H:%M:%S     ")), "\033[0m{}".format(binascii.hexlify(info_send).decode()))
        with open('log_imitator_nartis.log', 'a') as f:
            print(datetime.utcnow().strftime("%Y %m %d %H:%M:%S     "), binascii.hexlify(info_send).decode(), file=f)

    else:
        print("\n\t\t" + "\033[32m{}".format(info_send) + "\n")
        with open('log_imitator.log', 'a') as f:
            print("\n\t\t" + info_send + "\n", file=f)


def function_read_rs_485(ser, dict_device):
    send_all=b''
    len_send_all = -2
    checking_the_message = False
    while ser.inWaiting()==0:
        pass
    while True:
        send = ser.read()
        send_all += send
        if len(send_all) == 3 and send_all[0] == 126:
            len_send_all = send[0]
        elif send == b'':
            break
        elif len(send_all)==len_send_all+2 and send == b'~':
            send_all = send_all.strip(b'~')
            break
    try:
        checking_the_message = str(send_all[3]) in dict_device.keys()
    except IndexError:
        print_term_and_write_log('Неверный формат сообщения')
        print_term_and_write_log(send_all)
    if checking_the_message == False:
        send_all = b'0000000000'
    return send_all
            

