
import binascii
from function import general_function
from constants import volt_reg_constants_fun

volt_reg_constants = volt_reg_constants_fun()

# Функция формирования ответа на запрос списка объектов дневного архива
def get_voltage_register_object(send, ser, dict_device,):

    answer_data = binascii.unhexlify(b'e6e700c401c1000106020412000809060000010000ff0f02120000020412000109060000600b00ff0f021200000204120003090601000c0700ff0f021200000204120003090601000c0704ff0f0212000002041200030906000060080aff0f02120000020412000309060000600800ff0f021200')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa8'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)
    n=0
    while n<1:
        send = general_function.function_read_rs_485(ser, dict_device,)
        general_function.print_term_and_write_log(send)
        if send[6:7] == b'Q':
            answer_data = binascii.unhexlify(b'00')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'T')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)
        

def get_voltage_register_scale(send, ser, dict_device,):

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
            answer_data = binascii.unhexlify(b'07')
            heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'V')+answer_data)+b'~'
            ser.write(heading_answer)
            n+=1
        else:
            break
        general_function.print_term_and_write_log(heading_answer)

def get_voltage_register(send, ser, dict_device,):
    send=send.strip(b'~')
    date_send_1 = send[47:55] + b'\x00\x80\x00\x00'
    date_send_2 = send[61:69] + b'\x00\x80\x00\x00'

    answer_data = binascii.unhexlify(b'e6e700c401c10001020206090c' + binascii.hexlify(date_send_1) +b'16'+volt_reg_constants['event']+b'06'+volt_reg_constants['phase_voltage']+\
        b'06'+volt_reg_constants['voltage_deviation_value']+b'06'+volt_reg_constants['voltage_deviation_time']+b'06'+volt_reg_constants['uptime']+ b'020e090c' + \
            binascii.hexlify(date_send_2)+b'16'+volt_reg_constants['event']+b'06'+volt_reg_constants['phase_voltage']+b'06'+volt_reg_constants['voltage_deviation_value']+\
                b'06'+volt_reg_constants['voltage_deviation_time']+b'06'+volt_reg_constants['uptime'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

    # 07e6 09 0d 00 07 3b 34 ff 80 00 00
    # 07e6 09 15 00 08 3b 3a ff 80 00 00