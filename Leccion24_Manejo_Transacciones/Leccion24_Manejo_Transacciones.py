# Leccion 24 - Manejo de Transacciones
# ------------------------------------

# Base de datos inicial
#   | id_persona | nombre | apellido | email
# 1 |       1    | Juan   | Perez    | jperez@email.com
# 2 |       2    | Carla  | Gomez    | cgomez@email.com

import psycopg2 as bd

psw = 'yourpsw'
conexion = bd.connect(user='postgres', password=psw,
                      host='127.0.0.1', port=5432, database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    # Si hay un error en la primera sentencia, no se ejecuta la segunda
    sentencia = 'INSERT INTO persona(nombre,apellido, email) VALUES (%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@email.com')
    cursor.execute(sentencia, valores)
    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Martin', 'Garcia', 'mgarcia@email.com', 1)
    cursor.execute(sentencia, valores)
    conexion.commit()
    print("Transaccion terminada")
except Exception as e:
    conexion.rollback()
    print('Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()

##############################################################################

psw = 'yourpsw'
conexion = bd.connect(user='postgres', password=psw,
                      host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido, email) VALUES (%s, %s, %s)'
            valores = ('Miguel', 'Dominguez', 'mdominguez@email.com')
            cursor.execute(sentencia, valores)
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Alex', 'Rojas', 'mgarcia@email.com', 2)
            cursor.execute(sentencia, valores)
            print("Transaccion terminada")
except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
