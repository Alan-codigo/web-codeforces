import json
import mysql.connector
from datetime import datetime


with open('contests.json', 'r', encoding='utf-8', errors='ignore') as file:
    contests = json.load(file)




# Conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',  # Por ejemplo, 'localhost'
    user='root',
    password='Roof',
    database='codeforces'
)

# Crea un cursor para ejecutar las consultas
cursor = conn.cursor()

# Inserta los datos en la tabla
for contest in contests:
    contest_name = contest['data'][0]
    author = contest['data'][1]

    # Extrae y convierte la fecha y hora
    date_str = contest['data'][2]  # Ejemplo: 'Nov/30/2023 19:35'
    date_format = '%b/%d/%Y %H:%M'  # Define el formato de la fecha original
    try:
        date_obj = datetime.strptime(date_str.split()[0], date_format)
        creation_date = date_obj.strftime('%Y-%m-%d')  # Convierte a formato MySQL
        time = date_obj.strftime('%H:%M:%S')
    except ValueError:
        creation_date = None  # O maneja el error como prefieras
        time = None

    start_info = contest['data'][4]
    registration_info = contest['data'][5]
    links_str = ', '.join(contest['links'])

    # La consulta SQL, asegúrate de incluir los campos de fecha y hora
    query = 'INSERT INTO contests (contest_name, author, creation_date, time, start_info, registration_info, links) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (contest_name, author, creation_date, time, start_info, registration_info, links_str))


import mysql.connector
from mysql.connector import Error

try:
    # Establece la conexión a la base de datos
    conn = mysql.connector.connect(
        host='localhost',  # Asegúrate de que estos son los detalles correctos de tu base de datos
        user='root',
        password='Roof',
        database='codeforces'
    )
    
    if conn.is_connected():
        cursor = conn.cursor()
        
        # Aquí iría tu código para insertar datos...
        # Inserta los datos en la tabla
        for contest in contests:
            contest_name = contest['data'][0]
            author = contest['data'][1]

            # Extrae y convierte la fecha y hora
            date_str = contest['data'][2]  # Ejemplo: 'Nov/30/2023 19:35'
            date_format = '%b/%d/%Y %H:%M'  # Define el formato de la fecha original
            try:
                date_obj = datetime.strptime(date_str.split()[0], date_format)
                creation_date = date_obj.strftime('%Y-%m-%d')  # Convierte a formato MySQL
                time = date_obj.strftime('%H:%M:%S')
            except ValueError:
                creation_date = None  # O maneja el error como prefieras
                time = None

            start_info = contest['data'][4]
            registration_info = contest['data'][5]
            links_str = ', '.join(contest['links'])

            # La consulta SQL, asegúrate de incluir los campos de fecha y hora
            query = 'INSERT INTO contests (contest_name, author, creation_date, time, start_info, registration_info, links) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(query, (contest_name, author, creation_date, time, start_info, registration_info, links_str))

                # No olvides hacer commit y cerrar el cursor y la conexión
        conn.commit()
        cursor.close()
        conn.close()
        print("Datos insertados correctamente.")
    else:
        print("No se pudo conectar a la base de datos")
except Error as e:
    print("Error durante la conexión o la ejecución de la consulta:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
