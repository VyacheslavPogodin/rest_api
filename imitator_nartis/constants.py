# Набор тестовых значений для архивов и журналов
# Для журналов в корне таблица с возможными значениями событий СПОДЕС и соответствие событиям ZEUS

from function import general_function

archve_constant_dec = {
    'A+_0' : 1000,              # 1.0.1.8.0.255 Активная энергия, импорт суммарный
    'A+_1' : 101,               # 1.0.1.8.1.255 Активная энергия, импорт по 1 тарифу
    'A+_2' : 102,               # 1.0.1.8.2.255 Активная энергия, импорт по 2 тарифу
    'A+_3' : 103,               # 1.0.1.8.3.255 Активная энергия, импорт по 3 тарифу
    'A+_4' : 104,               # 1.0.1.8.4.255 Активная энергия, импорт по 4 тарифу
    'A+_5' : 105,               # 1.0.1.8.5.255 Активная энергия, импорт по 5 тарифу
    'A+_6' : 106,               # 1.0.1.8.6.255 Активная энергия, импорт по 6 тарифу
    'A+_7' : 107,               # 1.0.1.8.7.255 Активная энергия, импорт по 7 тарифу
    'A+_8' : 108,               # 1.0.1.8.8.255 Активная энергия, импорт по 8 тарифу
    'A-_0' : 2000,              # 1.0.2.8.0.255 Активная энергия, экспорт суммарный
    'A-_1' : 201,               # 1.0.2.8.1.255 Активная энергия, экспорт по 1 тарифу
    'A-_2' : 202,               # 1.0.2.8.2.255 Активная энергия, экспорт по 2 тарифу
    'A-_3' : 203,               # 1.0.2.8.3.255 Активная энергия, экспорт по 3 тарифу
    'A-_4' : 204,               # 1.0.2.8.4.255 Активная энергия, экспорт по 4 тарифу
    'A-_5' : 205,               # 1.0.2.8.5.255 Активная энергия, экспорт по 5 тарифу
    'A-_6' : 206,               # 1.0.2.8.6.255 Активная энергия, экспорт по 6 тарифу
    'A-_7' : 207,               # 1.0.2.8.7.255 Активная энергия, экспорт по 7 тарифу
    'A-_8' : 208,               # 1.0.2.8.8.255 Активная энергия, экспорт по 8 тарифу
    'R+_0' : 3000,              # 1.0.3.8.0.255 Реактивная энергия, импорт суммарный
    'R+_1' : 301,               # 1.0.3.8.1.255 Реативная энергия, импорт по 1 тарифу
    'R+_2' : 302,               # 1.0.3.8.2.255 Реативная энергия, импорт по 2 тарифу
    'R+_3' : 303,               # 1.0.3.8.3.255 Реативная энергия, импорт по 3 тарифу
    'R+_4' : 304,               # 1.0.3.8.4.255 Реативная энергия, импорт по 4 тарифу
    'R+_5' : 305,               # 1.0.3.8.5.255 Реативная энергия, импорт по 5 тарифу
    'R+_6' : 306,               # 1.0.3.8.6.255 Реативная энергия, импорт по 6 тарифу
    'R+_7' : 307,               # 1.0.3.8.7.255 Реативная энергия, импорт по 7 тарифу
    'R+_8' : 308,               # 1.0.3.8.8.255 Реативная энергия, импорт по 8 тарифу
    'R-_0' : 4000,              # 1.0.4.8.0.255 Активная энергия, экспорт суммарный
    'R-_1' : 401,               # 1.0.3.8.1.255 Реативная энергия, экспорт по 1 тарифу
    'R-_2' : 402,               # 1.0.3.8.2.255 Реативная энергия, экспорт по 2 тарифу
    'R-_3' : 403,               # 1.0.3.8.3.255 Реативная энергия, экспорт по 3 тарифу
    'R-_4' : 404,               # 1.0.3.8.4.255 Реативная энергия, экспорт по 4 тарифу
    'R-_5' : 405,               # 1.0.3.8.5.255 Реативная энергия, экспорт по 5 тарифу
    'R-_6' : 406,               # 1.0.3.8.6.255 Реативная энергия, экспорт по 6 тарифу
    'R-_7' : 407,               # 1.0.3.8.7.255 Реативная энергия, экспорт по 7 тарифу
    'R-_8' : 408,               # 1.0.3.8.8.255 Реативная энергия, экспорт по 8 тарифу
}

load_profile_constant_dec = {
    'A+' : 101,             # 1.0.1.29.0.255  Импорт активной энергии за период записи
    'A-' : 102,             # 1.0.2.29.0.255  Экспорт активной энергии за период записи
    'R+' : 103,             # 1.0.3.29.0.255  Реактивная энергия, импорт за период записи
    'R-' : 104,             # 1.0.4.29.0.255  Реактивная энергия, экспорт за период записи
    'No_name_1': 1,        # 1.0.1.53.0.255  неизвестный OBIS-код
    'No_name_2': 2,        # 1.0.2.53.0.255  неизвестный OBIS-код
    'No_name_3': 3,        # 1.0.3.53.0.255  неизвестный OBIS-код
    'No_name_4': 4,        # 1.0.4.53.0.255  неизвестный OBIS-код
    'Ua' : 11,              # 1.0.32.27.0.255 Напряжение фазы А
    'Ub' : 12,              # 1.0.52.27.0.255 Напряжение фазы B
    'Uc' : 13,              # 1.0.72.27.0.255 Напряжение фазы C
    'Term': 20,             # 0.0.96.9.0.255  Температура, С°
    'uptime' : 500,        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Контроль доступа meter_access_events (access_events_function.py)
# event: 9; source: 69; timestamp: 2022-06-21 12:59:59; comment: uptime: 6000; 
access_reg_constant = {
    'event' : 1, # 0т 1 до 2       # 0.0.96.11.6.255   Код события СПОДЭС
    'cannel' : 1,                  # 0.0.96.12.4.255  Номер канала (интерфейс)
    'client': 20,  # 10,20 или 30  # 0.0.96.12.6.255  Адрес (клиента)
    'uptime' : 6000,               # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Комуникационных событий meter_communication_events (com_events_function.py)
# event: 26; source: 68; timestamp: 2022-06-23 03:59:59; comment: uptime: 255;  
com_events_reg_constant = {
    'event' : 1, # 0т 1 до 2       # 0.0.96.11.5.255   Код события СПОДЭС
    'cannel' : 1,                  # 0.0.96.12.4.255  Номер канала (интерфейс)
    'client': 20,  # 10,20 или 30  # 0.0.96.12.6.255  Адрес (клиента)
    'uptime' : 5000,               # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Токов meter_current_register (current_reg_function.py)
# event: 29; source: 70; timestamp: 2022-06-21 12:59:59; comment: uptime: 255; 
current_reg_constant = {
    'event' : 1,           # до 1 от 31     # 0.0.96.11.1.255  Код события 
    'uptime' : 1000,                        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Самодиагностики meter_diagnostics_events (diagnostics_events_function.py)
# event: 29; source: 70; timestamp: 2022-06-21 12:59:59; comment: uptime: 255; 
diagnostics_reg_constant = {
    'event' : 1,           # до 1 от 4     # 0.0.96.11.7.255  Код события 
    'uptime' : 7000,                        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Внешних воздействий meter_external_eventsr (external_events_function.py)
# event: 8; source: 67; timestamp: 2022-06-21 12:59:59; comment: uptime: 255;  
external_reg_constant = {
    'event' : 1,           # до 1 от 4     # 0.0.96.11.4.255  Код события 
    'uptime' : 4000,                        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Включений выключений meter_on_off_and_relay_register (on_off_reg_function.py)
# event: 4; source: 45; timestamp: 2022-06-21 12:59:59; comment: uptime: 255;  
on_off_reg_constant = {
    'event' : 1,           # до 1 от 17     # 0.0.96.11.2.255  Код события 
    'uptime' : 2000,                        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Пареметров качества сети meter_quality_register (quality_reg_function.py)
# event: 33; source: 78; timestamp: 2022-06-21 12:59:59; comment: uptime: 255; 
quality_reg_constant = {
    'quality' : 1, #1,2,4,8,10,20,40,80      # 0.0.96.5.1.255  Статус качества сети 
    'uptime' : 9000,                        # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Коррекции данных meter_reconfig_register (reconfig_reg_function.py)
# event: 24; source: 63; timestamp: 2022-06-24 14:29:07; comment: uptime: 79523556; 
reconfig_reg_constant = {
    'event' : 1,                   # 0.0.96.11.3.255   Код события СПОДЭС, значения от 1 до 68
    'cannel' : 1,                  # 0.0.96.12.4.255  Номер канала (интерфейс)
    'client': 20,  # 10,20 или 30  # 0.0.96.12.6.255  Адрес (клиента)
    'uptime' : 3000,               # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Превышение тангенса meter_tangent_register (tangent_reg_function.py)
# event: 11; source: 77; timestamp: 2022-06-21 12:59:59; comment: uptime: 255; 
tangent_reg_constant = {
    'event' : 1,                 # 0.0.96.11.8.255   Код события СПОДЭС, значения 1 или 2
    'uptime' : 8000,             # 0.0.96.8.0.255   Время работы ПУ
}

# Данные для журнала Коррекции времени meter_time_correction_register (time_correct_reg_function.py)
#event: 31; source: 96; timestamp: 2022-06-22 06:44:19; comment: uptime: 1781110; old_time: 2022-06-22  06:44:18;
# Новое время в ответном сообщении формируется на конец часа времени запроса xx:59:59, старое на 59 секунд меньше xx:59:00
time_correct_reg_constant = {
    'uptime' : 13000,               # 0.0.96.8.0.255   Время работы ПУ
}

#  Данные для журнала Напряжений meter_voltage_register (volt_reg_function.py)
#  event: 10; source: 15; timestamp: 2022-06-21 16:59:59; comment: uptime: 255; phase_voltage: 0.001000; voltage_deviation_value: 0.002000; voltage_deviation_time: 30.000000;
volt_reg_constants = {
    'event' : 10,                           # 0.0.96.11.0.255   Код события СПОДЭС, значения от 1 до 26
    'uptime' : 100,                         # 0.0.96.8.0.255   Время работы ПУ
    'phase_voltage' : 1,                    # 1.0.12.7.0.255  Напряжение любой фазы
    'voltage_deviation_value' : 2,          # 1.0.12.7.4.255  Глубина провала/ перенапряжения
    'voltage_deviation_time' : 30 #min 10   # 0.0.96.8.10.255  Длительность провала/ перенапряжения
}

requestr_quality_dec = {
    'voltage_a' : 0,
    'voltage_b' : 1,
    'voltage_c' : 2,
    'current_a' : 3,
    'current_b' : 4,
    'current_c' : 5,
    'frequency' : 6,
    'phase_a_pow_fact' : 9,
    'phase_b_pow_fact' : 10,
    'phase_c_pow_fact' : 11,
    'angle_1' : 120,
    'angle_2' : 0,
    'angle_3' : 0,
    'activ_power_a' : 16,
    'activ_power_b' : 17,
    'activ_power_c' : 18,
    'react_pow_a' : 19,
    'react_pow_b' : 20,
    'react_pow_c' : 21,
    'full_pow' : 22,
    'activ_power' : 101,
    'common_pow_fact': 111,
    'full_pow_a': 113,
    'full_pow_b': 114,
    'full_pow_c': 115,
    'react_pow' : 116,
    'line_voltage_ab' : 124,
    'line_voltage_bc' : 125,
    'line_voltage_ca' : 126,
    'tang_fi_A' : 128,
    'tang_fi_B' : 129,
    'tang_fi_C' : 130,
    'tang_fi_full' : 131,

}



def archives_constant_fun():
    archve_constant = {}
    for i in archve_constant_dec.keys():
        archve_constant[i] = general_function.conv(str(archve_constant_dec[i])).zfill(8).encode()
    return archve_constant

def load_profile_constant_fun():
    load_profile_constant = {}
    load_profile_constant['A+'] = general_function.conv(str(load_profile_constant_dec['A+'])).zfill(8).encode()
    load_profile_constant['A-'] = general_function.conv(str(load_profile_constant_dec['A-'])).zfill(8).encode()
    load_profile_constant['R+'] = general_function.conv(str(load_profile_constant_dec['R+'])).zfill(8).encode()
    load_profile_constant['R-'] = general_function.conv(str(load_profile_constant_dec['R-'])).zfill(8).encode()
    load_profile_constant['No_name_1'] = general_function.conv(str(load_profile_constant_dec['No_name_1'])).zfill(8).encode()
    load_profile_constant['No_name_2'] = general_function.conv(str(load_profile_constant_dec['No_name_2'])).zfill(8).encode()
    load_profile_constant['No_name_3'] = general_function.conv(str(load_profile_constant_dec['No_name_3'])).zfill(8).encode()
    load_profile_constant['No_name_4'] = general_function.conv(str(load_profile_constant_dec['No_name_4'])).zfill(8).encode()
    load_profile_constant['Ua'] = general_function.conv(str(load_profile_constant_dec['Ua'])).zfill(8).encode()
    load_profile_constant['Ub'] = general_function.conv(str(load_profile_constant_dec['Ub'])).zfill(8).encode()
    load_profile_constant['Uc'] = general_function.conv(str(load_profile_constant_dec['Uc'])).zfill(8).encode()
    load_profile_constant['Term'] = general_function.conv(str(load_profile_constant_dec['Term'])).zfill(4).encode()
    load_profile_constant['uptime'] = general_function.conv(str(load_profile_constant_dec['uptime'])).zfill(8).encode()
    return load_profile_constant

def access_reg_constant_fun():
    access_reg_constant['event'] = general_function.conv(str(access_reg_constant['event'])).zfill(2).encode()
    access_reg_constant['cannel'] = general_function.conv(str(access_reg_constant['cannel'])).zfill(2).encode()
    access_reg_constant['client'] = general_function.conv(str(access_reg_constant['client'])).zfill(2).encode()
    access_reg_constant['uptime'] = general_function.conv(str(access_reg_constant['uptime'])).zfill(8).encode()
    return access_reg_constant

def com_events_reg_constant_fun():
    com_events_reg_constant['event'] = general_function.conv(str(com_events_reg_constant['event'])).zfill(2).encode()
    com_events_reg_constant['cannel'] = general_function.conv(str(com_events_reg_constant['cannel'])).zfill(2).encode()
    com_events_reg_constant['client'] = general_function.conv(str(com_events_reg_constant['client'])).zfill(2).encode()
    com_events_reg_constant['uptime'] = general_function.conv(str(com_events_reg_constant['uptime'])).zfill(8).encode()
    return com_events_reg_constant

def current_reg_constant_fun():
    current_reg_constant['event'] = general_function.conv(str(current_reg_constant['event'])).zfill(2).encode()
    current_reg_constant['uptime'] = general_function.conv(str(current_reg_constant['uptime'])).zfill(8).encode()
    return current_reg_constant

def diagnostics_reg_constant_fun():
    diagnostics_reg_constant['event'] = general_function.conv(str(diagnostics_reg_constant['event'])).zfill(2).encode()
    diagnostics_reg_constant['uptime'] = general_function.conv(str(diagnostics_reg_constant['uptime'])).zfill(8).encode()
    return diagnostics_reg_constant

def external_reg_constant_fun():
    external_reg_constant['event'] = general_function.conv(str(external_reg_constant['event'])).zfill(2).encode()
    external_reg_constant['uptime'] = general_function.conv(str(external_reg_constant['uptime'])).zfill(8).encode()
    return external_reg_constant

def on_off_reg_constant_fun():
    on_off_reg_constant['event'] = general_function.conv(str(on_off_reg_constant['event'])).zfill(2).encode()
    on_off_reg_constant['uptime'] = general_function.conv(str(on_off_reg_constant['uptime'])).zfill(8).encode()
    return on_off_reg_constant

def quality_reg_constant_fun():
    quality_reg_constant['quality'] = general_function.conv(str(quality_reg_constant['quality'])).zfill(2).encode()
    quality_reg_constant['uptime'] = general_function.conv(str(quality_reg_constant['uptime'])).zfill(8).encode()
    return quality_reg_constant

def reconfig_reg_constant_fun():
    reconfig_reg_constant['event'] = general_function.conv(str(reconfig_reg_constant['event'])).zfill(2).encode()
    reconfig_reg_constant['cannel'] = general_function.conv(str(reconfig_reg_constant['cannel'])).zfill(2).encode()
    reconfig_reg_constant['client'] = general_function.conv(str(reconfig_reg_constant['client'])).zfill(2).encode()
    reconfig_reg_constant['uptime'] = general_function.conv(str(reconfig_reg_constant['uptime'])).zfill(8).encode()
    return reconfig_reg_constant

def tangent_reg_constant_fun():
    tangent_reg_constant['event'] = general_function.conv(str(tangent_reg_constant['event'])).zfill(2).encode()
    tangent_reg_constant['uptime'] = general_function.conv(str(tangent_reg_constant['uptime'])).zfill(8).encode()
    return tangent_reg_constant

def time_correct_reg_constant_fun():
    time_correct_reg_constant['uptime'] = general_function.conv(str(time_correct_reg_constant['uptime'])).zfill(8).encode()
    return time_correct_reg_constant

def volt_reg_constants_fun():
    volt_reg_constants['event'] = general_function.conv(str(volt_reg_constants['event'])).zfill(2).encode()
    volt_reg_constants['uptime'] = general_function.conv(str(volt_reg_constants['uptime'])).zfill(8).encode()
    volt_reg_constants['phase_voltage'] = general_function.conv(str(volt_reg_constants['phase_voltage']*1000)).zfill(8).encode()
    volt_reg_constants['voltage_deviation_value'] = general_function.conv(str(volt_reg_constants['voltage_deviation_value']*1000)).zfill(8).encode()
    volt_reg_constants['voltage_deviation_time'] = general_function.conv(str(int(volt_reg_constants['voltage_deviation_time']/10))).zfill(8).encode()
    return volt_reg_constants

def request_quality_fun():
    requestr_quality = {}
    requestr_quality['frequency'] = general_function.conv(str(requestr_quality_dec['frequency']*1000)).zfill(8).encode()
    requestr_quality['current_a'] = general_function.conv(str(requestr_quality_dec['current_a']*1000)).zfill(8).encode()
    requestr_quality['current_b'] = general_function.conv(str(requestr_quality_dec['current_b']*1000)).zfill(8).encode()
    requestr_quality['current_c'] = general_function.conv(str(requestr_quality_dec['current_c']*1000)).zfill(8).encode()
    requestr_quality['voltage_a'] = general_function.conv(str(requestr_quality_dec['voltage_a']*1000)).zfill(8).encode()
    requestr_quality['voltage_b'] = general_function.conv(str(requestr_quality_dec['voltage_b']*1000)).zfill(8).encode()
    requestr_quality['voltage_c'] = general_function.conv(str(requestr_quality_dec['voltage_c']*1000)).zfill(8).encode()
    requestr_quality['common_pow_fact'] = general_function.conv(str(requestr_quality_dec['common_pow_fact']*1000000)).zfill(8).encode()
    requestr_quality['phase_a_pow_fact'] = general_function.conv(str(requestr_quality_dec['phase_a_pow_fact']*1000000)).zfill(8).encode()
    requestr_quality['phase_b_pow_fact'] = general_function.conv(str(requestr_quality_dec['phase_b_pow_fact']*1000000)).zfill(8).encode()
    requestr_quality['phase_c_pow_fact'] = general_function.conv(str(requestr_quality_dec['phase_c_pow_fact']*1000000)).zfill(8).encode()
    requestr_quality['full_pow'] = general_function.conv(str(requestr_quality_dec['full_pow']*1000)).zfill(8).encode()
    requestr_quality['full_pow_a'] = general_function.conv(str(requestr_quality_dec['full_pow_a']*1000)).zfill(8).encode()
    requestr_quality['full_pow_b'] = general_function.conv(str(requestr_quality_dec['full_pow_b']*1000)).zfill(8).encode()
    requestr_quality['full_pow_c'] = general_function.conv(str(requestr_quality_dec['full_pow_c']*1000)).zfill(8).encode()
    requestr_quality['activ_power'] = general_function.conv(str(requestr_quality_dec['activ_power']*1000)).zfill(8).encode()
    requestr_quality['activ_power_a'] = general_function.conv(str(requestr_quality_dec['activ_power_a']*1000)).zfill(8).encode()
    requestr_quality['activ_power_b'] = general_function.conv(str(requestr_quality_dec['activ_power_b']*1000)).zfill(8).encode()
    requestr_quality['activ_power_c'] = general_function.conv(str(requestr_quality_dec['activ_power_c']*1000)).zfill(8).encode()
    requestr_quality['react_pow'] = general_function.conv(str(requestr_quality_dec['react_pow']*1000)).zfill(8).encode()
    requestr_quality['react_pow_a'] = general_function.conv(str(requestr_quality_dec['react_pow_a']*1000)).zfill(8).encode()
    requestr_quality['react_pow_b'] = general_function.conv(str(requestr_quality_dec['react_pow_b']*1000)).zfill(8).encode()
    requestr_quality['react_pow_c'] = general_function.conv(str(requestr_quality_dec['react_pow_c']*1000)).zfill(8).encode()
    requestr_quality['line_voltage_ab'] = general_function.conv(str(requestr_quality_dec['line_voltage_ab']*1000)).zfill(8).encode()
    requestr_quality['line_voltage_bc'] = general_function.conv(str(requestr_quality_dec['line_voltage_bc']*1000)).zfill(8).encode()
    requestr_quality['line_voltage_ca'] = general_function.conv(str(requestr_quality_dec['line_voltage_ca']*1000)).zfill(8).encode()
    requestr_quality['angle_1'] = general_function.conv(str(requestr_quality_dec['angle_1']*1000)).zfill(8).encode()
    requestr_quality['angle_2'] = general_function.conv(str(requestr_quality_dec['angle_2']*1000)).zfill(8).encode()
    requestr_quality['angle_3'] = general_function.conv(str(requestr_quality_dec['angle_3']*1000)).zfill(8).encode()
    requestr_quality['tang_fi_A'] = general_function.conv(str(requestr_quality_dec['tang_fi_A']*10000)).zfill(8).encode()
    requestr_quality['tang_fi_B'] = general_function.conv(str(requestr_quality_dec['tang_fi_B']*10000)).zfill(8).encode()
    requestr_quality['tang_fi_C'] = general_function.conv(str(requestr_quality_dec['tang_fi_C']*10000)).zfill(8).encode()
    requestr_quality['tang_fi_full'] = general_function.conv(str(requestr_quality_dec['tang_fi_full']*10000)).zfill(8).encode()

    return requestr_quality
