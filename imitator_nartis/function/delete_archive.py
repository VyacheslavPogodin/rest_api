
import psycopg2
from psycopg2 import OperationalError


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
        print("Delete archive and jornal")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection



def delete_archive_list():
    
    arhives = ('archive_daily',
        'archive_monthly',
        'archive_hourly',
        'load_profile',
        'meter_voltage_register',
        'meter_current_register',
        'meter_on_off_and_relay_register',
        'meter_reconfig_register',
        'meter_external_events',
        'meter_communication_events',
        'meter_access_events',
        'meter_diagnostics_events',
        'meter_tangent_register',
        'meter_quality_register',
        'meter_discrete_inputs_outputs',
        'meter_time_correction',
    )

    connection = create_connection(
    "uspd", "admin", "kPZa83Uz2#0", "10.10.29.109", "5432")

    cur = connection.cursor()  
        
    for i in arhives:
        cur.execute(f"DELETE FROM {i}")
        print('DELETE '+ f'{i}')
    connection.commit()
    connection.close()

if __name__ == "__main__":
    
    delete_archive_list()