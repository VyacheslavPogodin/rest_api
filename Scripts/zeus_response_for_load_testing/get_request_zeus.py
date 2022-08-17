
from datetime import datetime, timedelta
import os
import function_zeus
from time import sleep
import general_function
from threading import Thread


EUI_DEV = (
    #'000000000150AEA9', # Счетчик СПОДЭС_1
    #'000000000150B4F2', # Счетчик СПОДЭС_2
    #'00000000024D6874', # Счетчик Меркурий 234
    #'21841F16006F0D00', # Счетчик Zigbee
    '000000000057B661',
)


    #Аутентификация, открытие доступа на установку параметров
send_auth = '01000000000000000103000001EE2E7A65E869B7AC747DC29567E1F8183B'

    #Запрос на получение качества электросети  Код команды:  0x10
get_qulity = '0B01000010AA0203'


    #Запросы на получение состояния реле
get_relay = '01030000111A'

#Запрос на выключение реле
OUTPUT_STATE = '0100'               # Реле выключено
CONTROL_MODE = '00'                 # Параметр режима не задан
POWER_LIMIT_VALUE = '00' #'01020000F40100000000'            #'01020000ff0000000000 Лимит мощности не задан
TIME_DELAY__ON_OFF_VALUE = '00' #     # Время вкл/откл не задано
set_relay_off = '0103000010AB'+OUTPUT_STATE+CONTROL_MODE+POWER_LIMIT_VALUE#+TIME_DELAY__ON_OFF_VALUE
# 5501AB1200000000000150B4F20103000010110100 00 00F3E6
# 5501AB1F00000000000150B4F20103000010AB0100 00 0000FF0000000000012222C434

#Запрос на включение реле
OUTPUT_STATE = '0101'
CONTROL_MODE = '0104'
POWER_LIMIT_VALUE = '01020000ff0000000000' #'00'
TIME_DELAY_ON_OFF_VALUE =  '' #'011010'
set_relay_on = '0103000010AA'+OUTPUT_STATE+CONTROL_MODE+POWER_LIMIT_VALUE+TIME_DELAY_ON_OFF_VALUE



# Запросы на получение тарифа. Код команды: 0x15

# Получение информации о поставленной задаче на установку тарифа

# Получение задачи от текущего времени c заданием времени
def time_now_parser_hex():
    TIME_DEC = (datetime.utcnow()).strftime("%y %m %d %H %M %S").split()
    NEXT_TASK_DATETIME_VALUE = ''     # Время активации смещено на 30 секунд вперед
    for i in TIME_DEC:
        NEXT_TASK_DATETIME_VALUE += general_function.conv(i).zfill(2)
    return NEXT_TASK_DATETIME_VALUE
get_tarif_py_date_now = '0103000015AA0101'+time_now_parser_hex()

# Получение задачи от текущего времени c заданием времени
get_tarif_py_not_date = '0103000015AA00'

# Запросы на установку тарифа. Код команды: 0x14
# Установка тарифа с тремя тарифами без специальных дней и времени активации
TARIFF_WORK = (#  'чч' + 'мм'
    general_function.conv('00').zfill(2)+general_function.conv('00').zfill(2)+'01',
    general_function.conv('10').zfill(2)+general_function.conv('00').zfill(2)+'02',
    general_function.conv('21').zfill(2)+general_function.conv('00').zfill(2)+'03',
    )
TARIFF_WEEKENDS = (#  'чч' + 'мм'
    general_function.conv('00').zfill(2)+general_function.conv('00').zfill(2)+'01',
    general_function.conv('10').zfill(2)+general_function.conv('00').zfill(2)+'02',
    general_function.conv('21').zfill(2)+general_function.conv('00').zfill(2)+'03',
    )
TARIFF_HOLIDAY = (#  'чч' + 'мм'
    general_function.conv('00').zfill(2)+general_function.conv('00').zfill(2)+'01',
    general_function.conv('10').zfill(2)+general_function.conv('00').zfill(2)+'02',
    general_function.conv('21').zfill(2)+general_function.conv('00').zfill(2)+'03',
    )
SPECIAL_DAYS = '00'
ACTIVATING = '00'
set_tarif_py_not_day_not_act = '0103000014AA'+str(len(TARIFF_WORK)).zfill(2)+TARIFF_WORK[0]+TARIFF_WORK[1]+TARIFF_WORK[2]+str(len(TARIFF_WEEKENDS)).zfill(2)+TARIFF_WEEKENDS[0]+TARIFF_WEEKENDS[1]+TARIFF_WEEKENDS[2]+str(len(TARIFF_HOLIDAY)).zfill(2)+TARIFF_HOLIDAY[0]+TARIFF_HOLIDAY[1]+TARIFF_HOLIDAY[2]+SPECIAL_DAYS+ACTIVATING


# Установка тарифа с тремя тарифами временем активации без специальных дней 
TIME_DEC = (datetime.utcnow()+timedelta(seconds=30)).strftime("01 01 %y %m %d %H %M %S").split()
ACTIVATING = ''     # Время активации смещено на 30 секунд вперед
for i in TIME_DEC:
    ACTIVATING += general_function.conv(i).zfill(2)
SPECIAL_DAYS = '00'
set_tarif_py_not_day_act = '0103000014AA'+str(len(TARIFF_WORK)).zfill(2)+TARIFF_WORK[0]+TARIFF_WORK[1]+TARIFF_WORK[2]+str(len(TARIFF_WEEKENDS)).zfill(2)+TARIFF_WEEKENDS[0]+TARIFF_WEEKENDS[1]+TARIFF_WEEKENDS[2]+str(len(TARIFF_HOLIDAY)).zfill(2)+TARIFF_HOLIDAY[0]+TARIFF_HOLIDAY[1]+TARIFF_HOLIDAY[2]+SPECIAL_DAYS+ACTIVATING

# Установка тарифа с тремя тарифами со специальными днями (тариф 3 должен отличаться) без времени активации 
TARIFF_HOLIDAY = (#  'чч' + 'мм'
    general_function.conv('00').zfill(2)+general_function.conv('00').zfill(2)+'01',
    general_function.conv('09').zfill(2)+general_function.conv('00').zfill(2)+'02',
    general_function.conv('22').zfill(2)+general_function.conv('00').zfill(2)+'03',
    )
SPECIAL_DAYS = (
    general_function.conv('01').zfill(2)+general_function.conv('01').zfill(2),
    general_function.conv('05').zfill(2)+general_function.conv('05').zfill(2),
    general_function.conv('07').zfill(2)+general_function.conv('06').zfill(2),
)
ACTIVATING = '00'
set_tarif_py_day_not_act = '0103000014AA'+str(len(TARIFF_WORK)).zfill(2)+TARIFF_WORK[0]+TARIFF_WORK[1]+TARIFF_WORK[2]+str(len(TARIFF_WEEKENDS)).zfill(2)+TARIFF_WEEKENDS[0]+TARIFF_WEEKENDS[1]+TARIFF_WEEKENDS[2]+str(len(TARIFF_HOLIDAY)).zfill(2)+TARIFF_HOLIDAY[0]+TARIFF_HOLIDAY[1]+TARIFF_HOLIDAY[2]+str(len(SPECIAL_DAYS)).zfill(2)+SPECIAL_DAYS[0]+SPECIAL_DAYS[1]+SPECIAL_DAYS[2]+ACTIVATING


# Установка тарифа с тремя тарифами со специальными днями (тариф 3 должен отличаться) c временем активации 
TARIFF_HOLIDAY = (
    general_function.conv('00').zfill(2)+general_function.conv('00').zfill(2)+'01',
    general_function.conv('09').zfill(2)+general_function.conv('00').zfill(2)+'02',
    general_function.conv('22').zfill(2)+general_function.conv('00').zfill(2)+'03',
    )
SPECIAL_DAYS = (
    general_function.conv('01').zfill(2)+general_function.conv('01').zfill(2),
    general_function.conv('05').zfill(2)+general_function.conv('05').zfill(2),
    general_function.conv('07').zfill(2)+general_function.conv('06').zfill(2),
)
TIME_DEC = (datetime.utcnow()+timedelta(seconds=30)).strftime("01 01 %y %m %d %H %M %S").split()
ACTIVATING = ''     # Время активации смещено на 30 секунд вперед
for i in TIME_DEC:
    ACTIVATING += general_function.conv(i).zfill(2)
set_tarif_py_day_act = '0103000014AA'+str(len(TARIFF_WORK)).zfill(2)+TARIFF_WORK[0]+TARIFF_WORK[1]+TARIFF_WORK[2]+str(len(TARIFF_WEEKENDS)).zfill(2)+TARIFF_WEEKENDS[0]+TARIFF_WEEKENDS[1]+TARIFF_WEEKENDS[2]+str(len(TARIFF_HOLIDAY)).zfill(2)+TARIFF_HOLIDAY[0]+TARIFF_HOLIDAY[1]+TARIFF_HOLIDAY[2]+str(len(SPECIAL_DAYS)).zfill(2)+SPECIAL_DAYS[0]+SPECIAL_DAYS[1]+SPECIAL_DAYS[2]+ACTIVATING




get_profile = '000000000150AEA9010300001302011606140000000116061607000002050F'

def start_thread(EUI_DEV, send_list, repiat):
    n=1
    THREAD = {}
    for y in range(repiat):
        for i in EUI_DEV:
            args=( i, send_list)
            THREAD[f'thread{n}'] = Thread(target=function_zeus.socket_connect, args=args)
            n+=1
            #thread1 = Thread(target=function_zeus.socket_connect, args=args)
    for i in THREAD.keys():
        THREAD[i].start()

    for i in THREAD.keys():
        THREAD[i].join()    



if __name__ == '__main__':
    os.system('color')
    send_list = (#send_auth,
        #get_relay,
        #set_relay_off,
        #set_relay_on,
        #get_tarif_py_date_now,
        #get_tarif_py_not_date,
        #get_tarif_py,
        #set_tarif_py_not_day_not_act,
        #send_auth,
        #set_tarif_py_not_day_act,
        #send_auth,
        #set_tarif_py_day_not_act,
        #send_auth,
        #set_tarif_py_day_act,
        get_qulity,
        #get_profile,
        )
    

    start_thread(EUI_DEV, send_list, 1)