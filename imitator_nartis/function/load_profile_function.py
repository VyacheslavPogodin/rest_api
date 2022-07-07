

import binascii
from function import general_function
from constants import load_profile_constant_fun

load_profile = load_profile_constant_fun()

# Функция формирования ответа на запрос списка объектов дневного архива
def get_load_profile_object(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c100010e020412000809060000010000ff0f02120000020412000309060100011d00ff0f02120000020412000309060100021d00ff0f02120000020412000309060100031d00ff0f02120000020412000309060100041d00ff0f02120000020412000309060100013500ff0f021200')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<2:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)

        if send[5:6] == b'Q':
            answer_data = binascii.unhexlify(b'00020412000309060100023500ff0f02120000020412000309060100033500ff0f02120000020412000309060100043500ff0f02120000020412000309060100201b00ff0f02120000020412000309060100341b00ff0f02120000020412000309060100481b00ff0f0212000002041200030906')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            general_function.print_term_and_write_log(heading_answer)
            n+=1
        
        elif send[5:6] == b'q':
            answer_data = binascii.unhexlify(b'0000600900ff0f02120000020412000309060000600800ff0f02120000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            general_function.print_term_and_write_log(heading_answer)
            n+=1
        else:
            break


def get_load_profile_scale(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000101020d02020f00161e02020f00161e02020f00162002020f00162002020ffd161b02020ffd161b02020ffd161d02020ffd161d02020fff162302020fff162302020fff162302020f00160902020f001607')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

#7ea04d02214132a5e7e6e600c001c100070100630100ff0201010204020412000809060000010000ff0f02120000090c07e6011fff15003b00ff4c00090c07e6051aff081e0f00ff4c000100d6387e
def get_load_profile(send, ser, dict_device,):
    
    date_send_1 = send[47:52] + binascii.unhexlify(general_function.conv(str(send[52])).zfill(2)) + b'\x1e\x00\x00\x80\x00\x00'
    date_send_2 = send[47:52] + binascii.unhexlify(general_function.conv(str(send[52]+1)).zfill(2)) + b'\x00\x00\x00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c100010102020e090c' + binascii.hexlify(date_send_1) + b'06'+load_profile['A+']+b'06'+load_profile['A-'] + b'06'+load_profile['R+'] + b'06'+load_profile['R-']+b'06'+load_profile['No_name_1']+b'06'+load_profile['No_name_2']+b'06'+load_profile['No_name_3']+b'06'+load_profile['No_name_4']+b'06'+load_profile['Ua']+b'06'+load_profile['Ub']+b'06'+load_profile['Uc']+b'10'+load_profile['Term']+b'06'+load_profile['uptime']+b'020e090c' + binascii.hexlify(date_send_2) +b'06'+load_profile['A+']+b'06'+load_profile['A-']+b'06'+load_profile['R+'][:2])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<1:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[5:6] == b'Q':
            answer_data = binascii.unhexlify(load_profile['R+'][2:]+b'06'+load_profile['R-']+b'06'+load_profile['No_name_1']+b'06'+load_profile['No_name_2']+b'06'+load_profile['No_name_3']+b'06'+load_profile['No_name_4']+b'06'+load_profile['Ua']+b'06'+load_profile['Ub']+b'06'+load_profile['Uc']+b'10'+load_profile['Term']+b'06'+load_profile['uptime'])
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            general_function.print_term_and_write_log(heading_answer)
            n+=1
        else:
            break