
import binascii
from function import general_function
from constants import com_events_reg_constant_fun

com_events_constant = com_events_reg_constant_fun()

def get_communication_events_object(send, ser, dict_device,):
    answer_data = binascii.unhexlify(b'e6e700c401c1000105020412000809060000010000ff0f02120000020412000109060000600b05ff0f02120000020412000109060000600c04ff0f02120000020412000109060000600c06ff0f02120000020412000309060000600800ff0f02120000')
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)

def get_communication_events(send, ser, dict_device,):
    send=send.strip(b'~')
    date_send_1 = send[47:55] + b'\x00\x80\x00\x00'
    date_send_2 = send[61:69] + b'\x00\x80\x00\x00'
    answer_data = binascii.unhexlify(b'e6e700c401c10001020205090c' + binascii.hexlify(date_send_1) +b'16'+com_events_constant['event']+b'0901'+com_events_constant['cannel']+\
        b'0901'+com_events_constant['client']+b'06'+com_events_constant['uptime']+\
            b'020e090c'+ binascii.hexlify(date_send_2)+b'16'+com_events_constant['event']+b'0901'+com_events_constant['cannel']+b'0901'+com_events_constant['client']+b'06'+com_events_constant['uptime'])
    heading_answer = b'~'+general_function.crc16(general_function.crc16(b'\xa0'+general_function.len_send(answer_data)+general_function.form_answer_adres(send)+b'R')+answer_data)+b'~'
    ser.write(heading_answer)
    general_function.print_term_and_write_log(heading_answer)