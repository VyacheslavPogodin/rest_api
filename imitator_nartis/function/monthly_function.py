
import binascii
from function import general_function
from constants import archives_constant_fun

arch_const = archives_constant_fun()

# Функция формирования ответа на запрос списка объектов дневного архива
def get_monthly_archive_object(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c402c10000000001008201740126020412000809060000010000ff0f02120000020412000309060100010801ff0f02120000020412000309060100010802ff0f02120000020412000309060100010803ff0f02120000020412000309060100010804ff0f02120000020412000309060100')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<8:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[6:7] == b'Q':
            answer_data = binascii.unhexlify(b'010805ff0f02120000020412000309060100010806ff0f02120000020412000309060100010807ff0f02120000020412000309060100010808ff0f02120000020412000309060100010800ff0f02120000020412000309060100020801ff0f02120000020412000309060100020802ff0f021200')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'q':
            answer_data = binascii.unhexlify(b'00020412000309060100020803ff0f02120000020412000309060100020804ff0f02120000020412000309060100020805ff0f02120000020412000309060100020806ff0f02120000020412000309060100020807ff0f02120000020412000309060100020808ff0f0212000002041200030906')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'\x91':
            answer_data = binascii.unhexlify(b'0100020800ff0f02120000020412000309060100030801ff0f0212000002041200030906010003')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1                    

        elif send[6:7] == b'\xb4':
            answer_data = binascii.unhexlify(b'e6e700c402c10000000002008201740802ff0f02120000020412000309060100030803ff0f02120000020412000309060100030804ff0f02120000020412000309060100030805ff0f02120000020412000309060100030806ff0f02120000020412000309060100030807ff0f02120000020412')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'\xd1':
            answer_data = binascii.unhexlify(b'000309060100030808ff0f02120000020412000309060100030800ff0f02120000020412000309060100040801ff0f02120000020412000309060100040802ff0f02120000020412000309060100040803ff0f02120000020412000309060100040804ff0f021200000204120003090601000408')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        
        elif send[6:7] == b'\xf1':
            answer_data = binascii.unhexlify(b'05ff0f02120000020412000309060100040806ff0f02120000020412000309060100040807ff0f02120000020412000309060100040808ff0f02120000020412000309060100040800ff0f02120000020412000309060101832c00ff0f02120000020412000309060102832b00ff0f0212000002')# 0000600800ff0f02120000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'\x11':
            answer_data = binascii.unhexlify(b'70005e0412000309060101832600ff0f02120000020412000309060102832600ff0f0212000002041200')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'\x90')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'6':
            answer_data = binascii.unhexlify(b'e6e700c402c10100000003000e0309060000600800ff0f02120000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'\x90')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)


def get_monthly_archive_scale(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000101022502020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f00161e02020f')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<2:        
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[6:7] == b'Q':
            answer_data = binascii.unhexlify(b'00161e02020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f00162002020f0016')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        
        elif send[6:7] == b'q':
            answer_data = binascii.unhexlify(b'0702020f00160702020ffd16fe02020ffd16fe02020f001607')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)


def get_monthly_archive(send, ser, dict_device, ):

    date_send = send[62:63] + b'\x01\xff\x00\x00\x00\x00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c1000101022a090c' + binascii.hexlify(date_send) +b'06'+arch_const['A+_1']+b'06'+arch_const['A+_2']+b'06'+arch_const['A+_3']+b'06'+arch_const['A+_4']+b'06'+arch_const['A+_5']+b'06'+arch_const['A+_6']+b'06'+arch_const['A+_7']+b'06'+arch_const['A+_8']+b'06'+arch_const['A+_0']+b'06'+arch_const['A-_1']+b'06'+arch_const['A-_2']+b'06'+arch_const['A-_3']+b'06'+arch_const['A-_4']+b'06'+arch_const['A-_5']+b'06'+arch_const['A-_6']+b'06'+arch_const['A-_7']+b'06'+arch_const['A-_8'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<1:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[6:7] == b'Q':
            answer_data = binascii.unhexlify(b'06'+arch_const['A-_0']+b'06'+arch_const['R+_1']+b'06'+arch_const['R+_2']+b'06'+arch_const['R+_3']+b'06'+arch_const['R+_4']+b'06'+arch_const['R+_5']+b'06'+arch_const['R+_6']+b'06'+arch_const['R+_7']+b'06'+arch_const['R+_8']+b'06'+arch_const['R+_0']+b'06'+arch_const['R-_1']+b'06'+arch_const['R-_2']+b'06'+arch_const['R-_3']+b'06'+arch_const['R-_4']+b'06'+arch_const['R-_5']+b'06'+arch_const['R-_6']+b'06'+arch_const['R-_7']+b'06'+arch_const['R-_8']+b'06'+arch_const['R-_0']+b'060000000106000000010600000001060000000106000000ff')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)
