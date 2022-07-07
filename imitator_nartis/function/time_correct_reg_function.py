
import binascii
from function import general_function
from constants import time_correct_reg_constant_fun

time_constant = time_correct_reg_constant_fun()

def get_time_correction_register_object(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000103020412000809060000010000ff0f02120000020412000809060000010001ff0f02120000020412000309060000600800ff0f02120000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_time_correction_register(send, ser, dict_device,):
    
    date_send_new = send[47:53] + b';;\x00\x80\x00\x00'
    date_send_old = send[47:53] + b';\x00\x00\x80\x00\x00'

    answer_data = binascii.unhexlify(b'e6e700c401c10001040203090c' + binascii.hexlify(date_send_new) +b'090c'+binascii.hexlify(date_send_old)+b'06'+ time_constant['uptime'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
