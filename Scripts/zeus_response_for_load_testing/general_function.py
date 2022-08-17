
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
            host='10.10.29.108',
            port='5432',
        )
        #print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    cur = connection.cursor()

    cur.execute(
            f"SELECT address, serial, id_model FROM meter_device"
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
        
        adress = str((i[0]<<1)^1)
        if i[2] == 1:
            serial_number = str(i[1]).encode()
        elif i[2] == 2:
            serial_number = binascii.unhexlify(conv(str(i[1])).zfill(8))
        
        dict_device[str(adress)] = serial_number
    return dict_device


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
                #mask = 0x8408
                mask = 0xA001
            else:
                mask = 0x00
            crc = ((crc >> 1)) ^ mask
            
            j += 1
        i += 1
    if crc < 0:
       crc -= 256
    #crc = crc ^ 0xFFFF
    
    return data + chr(crc % 256).encode('latin-1') + chr(crc // 256).encode('latin-1')

def crc8(data, ):
    crc = 0
    # Iterate bytes in data
    for byte in data:
        # Iterate bits in byte
        for _ in range(0, 8):
            if (crc >> 7) ^ (byte & 0x01):
                crc = ((crc << 1) ^ 0x07) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
            # Shift to next bit
        byte = byte >> 1
    return data + chr(crc ).encode('latin-1')


# Функция формирования значения длинны фрейма в байтах
def len_send(send):
    return conv(str(len(send)//2)).zfill(2) + '00' + send

def len_send_rs(send):
    return conv(str(len(send)//2)).zfill(2) +send