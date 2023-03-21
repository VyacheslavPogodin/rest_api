
from function import general_function, reply_function, delete_archive


'''
Имитатор счетчика Нартис 
'''

def main():
    
    # delete_archive.delete_archive_list()
    config_parameter = general_function.InitConfigParameters(__file__)
    ser = general_function.initSerial(config_parameter.get_config_com())
    # ser.open()
    dict_device = general_function.GetSerialNumberDevice(config_parameter.get_config_database()).creat_dict_device()
    
    while True:
        send = general_function.function_read_rs_485(ser, dict_device)
        reply_function.reply_message(send, dict_device, ser )

        
if __name__ == "__main__":
    
    main()