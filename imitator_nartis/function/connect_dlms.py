
import binascii
from datetime import datetime, timedelta
from function import general_function
from Crypto.Cipher import AES
'''
Имитатор счетчика Нартис 
Функции ассоциации
'''


# Функция формирования ответа на ассоциацию DLMC
def assotiate_dlms(send):
    answer_data = binascii.unhexlify(b"8180140502008006020080070400000001080400000001") #'\x81\x80\x14\x05\x02\x00\x80\x06\x02\x00\x80\x07\x04\x00\x00\x00\x01\x08\x04\x00\x00\x00\x01'
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b's')+answer_data)+b'~'  
    return heading_answer

   
# Функция формирования ответа на аутентификацию
def auth_dlms_password(send):
    answer_data = binascii.unhexlify(b"e6e7006129a109060760857405080101a203020100a305a103020100be10040e0800065f1f040000101d00640007") #'\xe6\xe7\x00a)\xa1\t\x06\x07`\x85t\x05\x08\x01\x01\xa2\x03\x02\x01\x00\xa3\x05\xa1\x03\x02\x01\x00\xbe\x10\x04\x0e\x08\x00\x06_\x1f\x04\x00\x00\x10\x1d\x00d\x00\x07'        
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'0')+answer_data)+b'~'
    return heading_answer

def auth_dlms_cripto(send, ser, dict_device,):
    answer_data = binascii.unhexlify(b'e6e700614aa109060760857405080101a203020100a305a10302010e88020780890760857405080202aa12801000000000000000000000000000000000be10040e0800065f1f0400001a9d01800007')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'0')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    key = b'2222222222222222'
    in_send = send[41:57]
    n=0
    while n<1:    
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        n+=1
        if send[5:6] == b'2':
            encryptor = AES.new(key, AES.MODE_ECB)
            cripto_answer = encryptor.encrypt(in_send)
            answer_data = binascii.unhexlify(b'e6e700c701c10001000910'+ binascii.hexlify(cripto_answer))
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'2')+answer_data)+b'~'
            ser.write(heading_answer)
            general_function.print_term_and_write_log(heading_answer)
            send = b''
        else:
            break

# OBIS код запроса серийного номера  38627439              
def get_serial_number(send, serial_number_dev):
    answer_data = b'\xe6\xe7\x00\xc4\x01\xc1\x00\x06'+serial_number_dev
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    return heading_answer
    
# OBIS код запроса даты и времени OBIS 0.0.1.0.0.255
def get_date(send):
    with open('C:/pogodinvv/Test_uspd/imitator_nartis/function/delta_time.txt', 'r') as f: 
        DELTATIME =  int(f.read())
    print('\n\n'+ str(DELTATIME))
    date = b''
    with_delta_time = datetime.now() + timedelta(seconds = DELTATIME) 
    for i in with_delta_time.strftime("%Y %m %d 0%w %H %M %S 00 00 00 00").split():
        date += binascii.unhexlify(general_function.conv(i).zfill(len(i)))    
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0\x1f'+general_function.form_answer_adres(send)+b'R')+b'\xe6\xe7\x00\xc4\x01\xc1\x00\t\x0c'+date)+b'~'
    return heading_answer

def set_date(send,):
    answer_data = binascii.unhexlify(b'e6e700c501c100')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    with open('C:/pogodinvv/Test_uspd/imitator_nartis/function/delta_time.txt', 'w') as f: 
        f.write('0')    
    return heading_answer

# Ответ что нет данных

def ansver_none(send, ser, dict_device,):
    answer_data = binascii.unhexlify(b'e6e700c401c1000100')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    