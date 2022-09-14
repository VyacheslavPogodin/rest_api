
import binascii
from datetime import datetime
from function import general_function
from constants import quality_reg_constant_fun, request_quality_fun

quality_constant = quality_reg_constant_fun()
req_quality = request_quality_fun()

def get_quality_register_object(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000103020412000809060000010000ff0f02120000020412000109060000600501ff0f02120000020412000309060000600800ff0f02120000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_quality_register(send, ser, dict_device,):
    
    date_send = send[47:53] + b';;\00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c10001010203090c' + binascii.hexlify(date_send) +b'11'+quality_constant['quality']+b'06'+quality_constant['uptime'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_quality_stop_cadr(send, ser, dict_device,):

    date = b''
    for i in datetime.utcnow().strftime("%Y %m %d 0%w %H %M %S 00 00 00 00").split():
        date += binascii.unhexlify(general_function.conv(i).zfill(len(i)))
    answer_data = binascii.unhexlify(b'e6e700c402c10000000001008201740101024d090c' + binascii.hexlify(date) +b'0600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<3:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[5:6] == b'Q':            
            answer_data = binascii.unhexlify(b'00000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000060000000006000000000600000000'+b'06'+req_quality['frequency']+b'0600000000'+b'0500000000'+b'05'+req_quality['current_a'])
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        elif send[5:6] == b'q':
            answer_data = binascii.unhexlify(b'05'+req_quality['current_b']+b'05'+req_quality['current_c'] + b'0500000000'+b'06'+req_quality['voltage_a']+b'06'+req_quality['voltage_b']+b'06'+req_quality['voltage_c']+b'05'+req_quality['common_pow_fact']+b'05'+req_quality['phase_a_pow_fact']+b'05'+req_quality['phase_b_pow_fact']+b'05'+req_quality['phase_c_pow_fact']+b'06'+req_quality['full_pow']+b'06'+req_quality['full_pow_a']+b'06'+req_quality['full_pow_b']+b'06'+req_quality['full_pow_c']+b'06'+req_quality['activ_power']+b'05'+req_quality['activ_power_a']+b'05'+req_quality['activ_power_b']+b'05'+req_quality['activ_power_c']+b'05'+req_quality['react_pow']+b'05'+req_quality['react_pow_a']+b'05'+req_quality['react_pow_b']+b'05'+req_quality['react_pow_c']+b'0600000000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[5:6] == b'\x91':
            answer_data = binascii.unhexlify(b'06'+req_quality['line_voltage_ab']+b'06'+req_quality['line_voltage_bc']+b'06'+req_quality['line_voltage_ca']+b'05000000000500000000050000000005000000000500000000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+send[4:5]+send[2:4]+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1                    

        else:
            break
        general_function.print_term_and_write_log(heading_answer)
    