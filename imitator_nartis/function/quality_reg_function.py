
import binascii
from datetime import datetime
from function import general_function
from constants import quality_reg_constant_fun, request_quality_fun, archives_constant_fun

quality_constant = quality_reg_constant_fun()
req_quality = request_quality_fun()
arch_const = archives_constant_fun()


def get_quality_register_object(send, ser, dict_device,):
    answer_data = binascii.unhexlify(b'e6e700c401c1000103020412000809060000010000ff0f02120000020412000109060000600501ff0f02120000020412000309060000600800ff0f02120000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_quality_register(send, ser, dict_device,):
    send = send.strip(b'~')
    date_send_1 = send[47:55] + b'\x00\x80\x00\x00'
    date_send_2 = send[61:69] + b'\x00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c10001020203090c' + binascii.hexlify(date_send_1) +b'11'+quality_constant['quality']+b'06'+quality_constant['uptime']+\
        b'020e090c'+ binascii.hexlify(date_send_2)+b'11'+quality_constant['quality']+b'06'+quality_constant['uptime'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_quality_stop_cadr(send, ser, dict_device,):
    date = b''
    for i in datetime.utcnow().strftime("%Y %m %d 0%w %H %M %S 00 00 00 00").split():
        date += binascii.unhexlify(general_function.conv(i).zfill(len(i)))
    answer_data = binascii.unhexlify(b'e6e700c402c10000000001008201740101024d090c' + binascii.hexlify(date) +b'06'+arch_const['A+_0']+b'06'+arch_const['A+_1']+b'06'+arch_const['A+_2']+b'06'+arch_const['A+_3']+b'06'+arch_const['A+_4']+b'06'+arch_const['A+_5']+b'06'+arch_const['A+_6']+b'06'+arch_const['A+_7']+b'06'+arch_const['A+_8']+b'06'+arch_const['A-_0']+b'06'+arch_const['A-_1']+b'06'+arch_const['A-_2']+b'06'+arch_const['A-_3']+b'06'+arch_const['A-_4']+b'06'+arch_const['A-_5']+b'06'+arch_const['A-_6']+b'06'+arch_const['A-_7'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<4:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[6:7] == b'Q':            
            answer_data = binascii.unhexlify(b'06'+arch_const['A-_8']+b'06'+arch_const['R+_0']+b'06'+arch_const['R+_1']+b'06'+arch_const['R+_2']+b'06'+arch_const['R+_3']+b'06'+arch_const['R+_4']+b'06'+arch_const['R+_5']+b'06'+arch_const['R+_6']+b'06'+arch_const['R+_7']+b'06'+arch_const['R+_8']+b'06'+arch_const['R-_0']+b'06'+arch_const['R-_1']+b'06'+arch_const['R-_2']+b'06'+arch_const['R-_3']+b'06'+arch_const['R-_4']+b'06'+arch_const['R-_5']+b'06'+arch_const['R-_6']+b'06'+arch_const['R-_7']+b'06'+arch_const['R-_8']+b'06'+req_quality['frequency']+b'06'+req_quality['tang_fi_full']+b'0500000000'+b'05'+req_quality['current_a'])
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        elif send[6:7] == b'q':
            answer_data = binascii.unhexlify(b'05'+req_quality['current_b']+b'05'+req_quality['current_c'] + b'0500000000'+b'06'+req_quality['voltage_a']+b'06'+req_quality['voltage_b']+b'06'+req_quality['voltage_c']+b'05'+req_quality['common_pow_fact']+b'05'+req_quality['phase_a_pow_fact']+b'05'+req_quality['phase_b_pow_fact']+b'05'+req_quality['phase_c_pow_fact']+b'06'+req_quality['full_pow']+b'06'+req_quality['full_pow_a']+b'06'+req_quality['full_pow_b']+b'06'+req_quality['full_pow_c']+b'06'+req_quality['activ_power']+b'05'+req_quality['activ_power_a']+b'05'+req_quality['activ_power_b']+b'05'+req_quality['activ_power_c']+b'05'+req_quality['react_pow']+b'05'+req_quality['react_pow_a']+b'05'+req_quality['react_pow_b']+b'05'+req_quality['react_pow_c'])
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        elif send[6:7] == b'\x91':
            answer_data = binascii.unhexlify(b'06000000000600000000'+b'06'+req_quality['line_voltage_ab']+b'06'+req_quality['line_voltage_bc']+b'06'+req_quality['line_voltage_ca']+b'05000000000500000000'+b'05'+req_quality['tang_fi_A']+b'05'+req_quality['tang_fi_B']+b'05'+req_quality['tang_fi_C']+b'05'+req_quality['angle_1']+b'05'+req_quality['angle_2']+b'05000000000500000000')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1                    

        elif send[6:7] == b'\xb4':
            answer_data = binascii.unhexlify(b'e6e700c402c10110')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1

        else:
            break
        general_function.print_term_and_write_log(heading_answer)


def get_quality_faze(send, ser, dict_device,):
    answer_data = binascii.unhexlify(b'e6e700c401c100'+b'05'+req_quality['angle_1'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

    # e6e700c401c100	05ffffdb53
#        a01a02234132a317e6e600c001c10003010051070aff0200019e
    