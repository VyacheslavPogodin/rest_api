

import binascii
from function import general_function

# Запрос состояния реле
def get_relay(send, ser, ):
    answer_data = binascii.unhexlify(b'e6e700c401c1000300')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_relay_mode(send, ser, ):
    answer_data = binascii.unhexlify(b'e6e700c401c1001604')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_relay_state(send, ser, ):
    answer_data = binascii.unhexlify(b'e6e700c401c1000500000000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    
def get_limiter_val(send, ser, ):   #0100010700ff03
    answer_data = binascii.unhexlify(b'e6e700c401c10002020ffd161b')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_time_limiter(send, ser, ):   #0000110000ff03
    answer_data = binascii.unhexlify(b'e6e700c401c100060000000a')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
