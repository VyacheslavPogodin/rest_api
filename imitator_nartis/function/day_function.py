
import binascii
from datetime import date, timedelta
from function import general_function
from constants import archives_constant_fun

arch_const = archives_constant_fun()


# Функция формирования ответа на запрос списка объектов дневного архива
def get_day_archive_object(send, ser, dict_device,):
    
    answer_data = binascii.unhexlify(b'e6e700c402c10000000001008201740126020412000809060000010000ff0f02120000020412000309060100010801ff0f02120000020412000309060100010802ff0f02120000020412000309060100010803ff0f02120000020412000309060100010804ff0f02120000020412000309060100')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<7:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[5:6] == b'Q':            
            answer_data = binascii.unhexlify(b'010805ff0f02120000020412000309060100010806ff0f02120000020412000309060100010807ff0f02120000020412000309060100010808ff0f02120000020412000309060100010800ff0f02120000020412000309060100020801ff0f02120000020412000309060100020802ff0f021200')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        elif send[5:6] == b'q':
            answer_data = binascii.unhexlify(b'00020412000309060100020803ff0f02120000020412000309060100020804ff0f02120000020412000309060100020805ff0f02120000020412000309060100020806ff0f02120000020412000309060100020807ff0f02120000020412000309060100020808ff0f0212000002041200030906')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[5:6] == b'\x91':
            answer_data = binascii.unhexlify(b'0100020800ff0f02120000020412000309060100030801ff0f0212000002041200030906010003')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1                    

        elif send[5:6] == b'\xb4':
            answer_data = binascii.unhexlify(b'e6e700c402c101000000020082013a0802ff0f02120000020412000309060100030803ff0f02120000020412000309060100030804ff0f02120000020412000309060100030805ff0f02120000020412000309060100030806ff0f02120000020412000309060100030807ff0f02120000020412')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[5:6] == b'\xd1':
            answer_data = binascii.unhexlify(b'000309060100030808ff0f02120000020412000309060100030800ff0f02120000020412000309060100040801ff0f02120000020412000309060100040802ff0f02120000020412000309060100040803ff0f02120000020412000309060100040804ff0f021200000204120003090601000408')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        
        elif send[5:6] == b'\xf1':
            answer_data = binascii.unhexlify(b'05ff0f02120000020412000309060100040806ff0f02120000020412000309060100040807ff0f02120000020412000309060100040808ff0f02120000020412000309060100040800ff0f02120000020412000309060000600800ff0f02120000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[5:6] == b'\x16':
            answer_data = binascii.unhexlify(b'e6e700c402c10110')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'\x90')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)


def get_day_archive_scale(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000101022502020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    n=0
    general_function.print_term_and_write_log(heading_answer)

    while n<2:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[5:6] == b'Q':
            answer_data = binascii.unhexlify(b'00161e02020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f0016')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        
        elif send[5:6] == b'q':
            answer_data = binascii.unhexlify(b'07')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)


def get_day_archive(send, ser, dict_device,):

    date_send = date(
        year=send[47]*256+send[48],
        month=send[49],
        day=send[50],
        )
    date_delta = date_send + timedelta(days=1)
    date_send =  binascii.unhexlify(general_function.conv(str(date_delta.year)).zfill(4))+binascii.unhexlify(general_function.conv(str(date_delta.month)).zfill(2))+binascii.unhexlify(general_function.conv(str(date_delta.day)).zfill(2)) + b'\xff\x00\x00\x00\x00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c10001010226090c' + binascii.hexlify(date_send) +b'06'+arch_const['A+_1']+b'06'+arch_const['A+_2']+b'06'+arch_const['A+_3']+b'06'+arch_const['A+_4']+b'06'+arch_const['A+_5']+b'06'+arch_const['A+_6']+b'06'+arch_const['A+_7']+b'06'+arch_const['A+_8']+b'06'+arch_const['A+_0']+b'06'+arch_const['A-_1']+b'06'+arch_const['A-_2']+b'06'+arch_const['A-_3']+b'06'+arch_const['A-_4']+b'06'+arch_const['A-_5']+b'06'+arch_const['A-_6']+b'06'+arch_const['A-_7']+b'06'+arch_const['A-_8'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'

    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<1:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[5:6] == b'Q':
            answer_data = binascii.unhexlify(b'06'+arch_const['A-_0']+b'06'+arch_const['R+_1']+b'06'+arch_const['R+_2']+b'06'+arch_const['R+_3']+b'06'+arch_const['R+_4']+b'06'+arch_const['R+_5']+b'06'+arch_const['R+_6']+b'06'+arch_const['R+_7']+b'06'+arch_const['R+_8']+b'06'+arch_const['R+_0']+b'06'+arch_const['R-_1']+b'06'+arch_const['R-_2']+b'06'+arch_const['R-_3']+b'06'+arch_const['R-_4']+b'06'+arch_const['R-_5']+b'06'+arch_const['R-_6']+b'06'+arch_const['R-_7']+b'06'+arch_const['R-_8']+b'06'+arch_const['R-_0']+b'06000007D0')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)
        