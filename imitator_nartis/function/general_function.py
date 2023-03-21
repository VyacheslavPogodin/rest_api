
from datetime import datetime
from time import sleep
import serial
import os
import re
import copy
import binascii
import psycopg2
from psycopg2 import OperationalError
'''
Имитатор счетчика Нартис Основные функции
'''

# Считываем номера устройств из БД

class InitConfigParameters:

    def __init__(self, name_skripts) -> None:
        self.path_to_file_config = os.path.realpath(name_skripts).replace(os.path.basename(name_skripts), ".config")
        # print(self.path_to_file_config)

    def read_file(self) -> list:
        try:
            with open(self.path_to_file_config, 'r') as file:
                self.config_all_parameter = file.readlines()
        except FileNotFoundError:
            print("\t Файл настройки не найден! ")
            quit()
        return self.config_all_parameter

    def sorter_config(self, config_all_parameter, parameter) -> dict:
        
        self.config_all_parameter = config_all_parameter
        self.parameter=parameter
        self.config_dict = {}
        for i in self.config_all_parameter:
            if i.find(parameter) != -1:
                try:
                    self.config_dict[i.split("=")[0]]=int(i.split("=")[1].rstrip())
                except ValueError:
                    self.config_dict[i.split("=")[0]]=i.split("=")[1].rstrip()

        return self.config_dict
    
    def get_config_com(self) -> dict:
        return self.sorter_config(self.read_file(), "serial")

    def get_config_database(self) -> dict:
        return self.sorter_config(self.read_file(), "database")





# Создание словаря с номером устройства и серийным номером
class GetSerialNumberDevice:
# Считываем номера устройств из БД
    def __init__(self, config) -> None:
        self.config=config
    
    def decorator_connection(func):
        def connection_from_database(self):
            try:
                self.connection = psycopg2.connect(
                    database=self.config["database.name"],  #'uspd',
                    user=self.config["database.user"], #'admin',
                    password=self.config["database.password"] , #'kPZa83Uz2#0',
                    host= self.config["database.host"], #'10.10.29.109',
                    port=self.config["database.port"],  #'5432',
                )
                # print("Connection to PostgreSQL DB successful")
            except OperationalError as e:
                print(f"The error '{e}' occurred")
                quit()
            self.connection.set_client_encoding('UTF8')
            self.cur = self.connection.cursor()

            self.list_device = func(self, self.cur)

            self.cur.close()
            self.connection.close()
            return self.list_device
        return connection_from_database

    @decorator_connection
    def get_serial(self, cur) -> list:
        # self.cur = cur
        cur.execute(
                f"SELECT address, serial, id_model, id_interface, id FROM meter_device WHERE id_interface = 4"
            )
        self.device = cur.fetchall()
        return self.device

# Создание словаря с номером устройства и серийным номером
    def creat_dict_device(self):
        device = self.get_serial()
        dict_device = {}
        for i in device:
            #adress = chr(((i[0]<<1))^1).encode()
            if i[3] != 5:
                try:
                    adress = str((i[0]<<1)^1)
                except TypeError as er:
                    print_term_and_write_log(f'ДЛЯ УСТРОЙСТВА ID {i[4]} НЕ СФОРМИРОВАН АДРЕС ЗАДАН ПО УМОЛЧАНИЮ 33(67)')
                    adress = '67'
                if i[2] == 1:
                    serial_number = str(i[1]).encode()
                elif i[2] == 2:
                    serial_number = binascii.unhexlify(conv(i[1]).zfill(8))
                    # print(serial_number, conv(i[1]).zfill(8))
                else:
                    serial_number = b'20202020'
                dict_device[str(adress)] = serial_number
        return dict_device


# Настройки подключение по RS_485
def initSerial(config):
        serial_connect = serial.Serial(
        port = config["serial.port"], #'COM2',
        baudrate = config["serial.baudRate"], #9600,
        # stopbits = serial.STOPBITS_ONE,
        bytesize =config["serial.dataBits"],# 8,
        # parity = serial.PARITY_NONE,
        rtscts =config["serial.parity"],# 0,
        timeout = None,
        )
        return serial_connect

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

def form_answer_adres(send):
    if re.match(rb"~", send) is not None: #7ea008 0221419350b47e
        start_bit = 0
    else:
        start_bit = -1
    return send[start_bit+5:start_bit+6]+send[start_bit+3: start_bit+5]

def form_date_send(send):
    date_send = datetime(
        year=send[48]*256+send[49],
        month=send[50],
        day=send[51],
        hour=send[53],
        )
    return date_send



def print_term_and_write_log(info_send,):
    os.system('color')
    log_name = os.path.realpath(__file__).replace("function\\"+os.path.basename(__file__), "log_imitator_nartis.log")
    if type(info_send) == bytes:
        print("\033[33m{}".format(datetime.utcnow().strftime("%Y %m %d %H:%M:%S     ")), "\033[0m{}".format(binascii.hexlify(info_send).decode()))
        with open(log_name, 'a') as f:
            print(datetime.utcnow().strftime("%Y %m %d %H:%M:%S     "), binascii.hexlify(info_send).decode(), file=f)

    else:
        print("\n\t\t" + "\033[32m{}".format(info_send) + "\n")
        with open(log_name, 'a') as f:
            print("\n\t\t" + info_send + "\n", file=f)


def function_read_rs_485(ser, dict_device):

    send_all = b""
    return_send_all = b""
    len_send_all = -2
    checking_the_message = False
    num_breake = 0

    while ser.inWaiting()==0:
        sleep(0.05)
        num_breake+=1
        if num_breake == 24000:
            print_term_and_write_log('Нет данных от УСПД, проверьте соединение')
            ser.close()
            sleep(0.5)
            ser.open()
            num_breake = 0
    while True:    
        send = ser.read()#_until(b'~')#.rstrip(b'~')
        send_all += send
        # print(re.match(rb"~.*", send_all) is None)
        match send_all:

            case bytes(x) if re.match(rb"~~", x) is not None:
                send_all = send_all[1:]            
            
            case bytes(x) if re.match(rb"~", x) is None:
                send_all = b""

            case bytes(x) if len(x) == 4:
                len_send_all = send_all[2]+2

            case bytes(x) if len(x)>128:
                print_term_and_write_log('Ошибка длинны сообщения или флага конца сообщения')
                print_term_and_write_log(send_all)
                send_all = b""
                break

            case bytes(x) if x == b"":
                print_term_and_write_log('Нет связи с УСПД, проверьте соединение')
                send_all = b""
                break

            case bytes(x) if len(x) == len_send_all: #re.fullmatch(rb"~.*~", x) and
                return_send_all = copy.deepcopy(send_all)#.strip(b'~')
                send_all=b""
                break
            case _:
                pass
                # print(binascii.hexlify(send_all))
            
    try:
        checking_the_message = str(return_send_all[4]) in dict_device.keys()
    except (IndexError, TypeError) as e:
        print_term_and_write_log(f'{e} Ошибка принятого сообщения')
        print_term_and_write_log(return_send_all)
        return b""
    
    if checking_the_message:
        # print(binascii.hexlify(return_send_all))
        return return_send_all

    else:
        print_term_and_write_log('Непредвиденный сбой обмена')
        print_term_and_write_log(return_send_all)
        quit()

