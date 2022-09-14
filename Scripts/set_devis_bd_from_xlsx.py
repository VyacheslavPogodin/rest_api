from datetime import datetime
import psycopg2
from psycopg2 import OperationalError
from openpyxl import load_workbook

PATH = 'C:\pogodinvv\Work_BD\dev_list.xlsx'


def get_eui_dev_from_xlsx():

    wb = load_workbook(PATH)
    sheet = wb['Sheet']
    DEV_LIST = []
    start = 3316
    stop = 4143
    for i in range(start, stop):
        EUI_DEV = sheet[f'CQ{i}'].value
        SERIAL_NUM = sheet[f'CH{i}'].value
        
        if sheet[f'CG{i}'].value == 'НАРТИС-12-МТ-SP3-A1R1-230-5-80A-ST-RF433/1-RF2400/2-P2HKMOV3-D' and EUI_DEV != None:
            
            DEV_LIST.append([SERIAL_NUM[4:], EUI_DEV,])

    return DEV_LIST


#col_time_one = datetime.now().replace(microsecond=0)
#col_time_too = datetime.today().replace(hour=0, minute=0,second=0, microsecond=0)

ip = ['10.10.29.126']#, '10.10.28.70', '10.10.29.106', '10.10.28.47', '10.10.30.202', '10.10.28.62']

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def cur_execute():
    
    LIST_DEV = get_eui_dev_from_xlsx()

    connection = create_connection(
    "uspd", "admin", "kPZa83Uz2#0", "10.10.29.126", "5432")

    connection.set_client_encoding('UTF8')

    cur = connection.cursor()

    postgres_insert_query = """ INSERT INTO meter_device ( id_model, serial, eui, id_interface, in_time, archive, included_in_survey, tariff_mask, integral, current_transformation_ratio, voltage_transformation_ratio, loss_ratio, added, name, channel_mask, port_zigbee )
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
    port_dev = 7002

    for i in LIST_DEV:

        SERIAL_NUM, EUI_NUM = i
        record_to_insert = (5, SERIAL_NUM, EUI_NUM, 5, 'now()', 'False', 'True', 4, 30, 1, 1, 1, 'now()', 'Нартис-12М', 1, port_dev)
        port_dev+=1
        cur.execute(postgres_insert_query, record_to_insert)
    
    connection.commit()
    cur.close()
    connection.close()


    
if __name__ == "__main__":
    

    cur_execute()