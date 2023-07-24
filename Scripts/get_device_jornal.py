import psycopg2
from psycopg2 import OperationalError

def set_device_list():

    connection = None
    try:
        connection = psycopg2.connect(database='uspd', user='admin', password='kPZa83Uz2#0', host='localhost', port='5432',)
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        quit()

    
    cur = connection.cursor()
    cur.execute('SELECT device_eui, myrmidon_journal_id FROM public.record_journal_delete') #id_interface = 5 ORDER BY eui id = 855")
    list_divice = cur.fetchall()
    cur.execute('SELECT eui FROM meter_device ') #id_interface = 5 ORDER BY eui id = 855")
    all_device = cur.fetchall()
    connection.commit()

    list_device_dict = set()
    eui_jornal = set()
    
    for i in list_divice:
        list_device_dict.add(i[0])
        eui_jornal.add(i[0] +' : '+ str(i[1]))


    print(str(len(list_device_dict))+'/'+str(len(all_device)), *sorted(eui_jornal), sep='\n')



if __name__ == '__main__':

    set_device_list()