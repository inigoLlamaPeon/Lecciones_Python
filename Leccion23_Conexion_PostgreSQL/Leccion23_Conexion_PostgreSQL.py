# Leccion 23 - Conexion PostgreSQL
# --------------------------------


# Base de datos inicial
#   | id_persona | nombre | apellido | email
# 1 |       1    | Juan   | Perez    | jperez@email.com
# 2 |       2    | Carla  | Gomez    | cgomez@email.com

import psycopg2

psw = 'ingganafis91'
# Leer Todo
conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

# Si se usa with, los cambios se guardan automaticamente
# en la base de datos (se puede hacer rollback).
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print('Todos los registros son:\n', registros)
except Exception as e:
    print('Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Leer fila cuyo id_persona es igual a 1
conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona=1'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print("El registro 1 es: \n", registros)
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Leer fila cuyo id_persona es igual al numero que introduzcamos
# %s -> Placeholder / Parámetro Posicional
conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona=%s'
            id_persona = input('Proporciona el valor id_persona: ')
            cursor.execute(sentencia, (id_persona,))# Al poner la coma,
                                                    # se indica que se
                                                    # trata de una tupla
            registro = cursor.fetchone()# Un único resgistro para 
                                        # optimizar el código
            print('El registro elegido es: ', id_persona)
            print('Registro numero', id_persona, ': ', registro)
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Leer filas numero 1, 2, 3 y 4. Devuelve las únicas que hay disponibles

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2,3,4)'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            x = 1
            print('Los registros introducidos son:')
            for registro in registros:
                print('Registro numero', x, ': ', registro)
                x += 1
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Identico al caso anterior, pero metiendo desde el teclado id_personas
# separados por comas.

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id\'s a buscar separados por comas: ')
            llavesPrimarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llavesPrimarias)
            registros = cursor.fetchall()
            x = 1
            print('Los registros leidos son:')
            for registro in registros:
                print('Registro numero', x, ': ', registro)
                x += 1
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()


##############################################################################

# Insertar registro

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Carlos', 'Garcia', 'jgarcia@email.com')
            cursor.execute(sentencia, valores)
            # conexion.commit() -> Se hace automaticamente al usar with
            reg_insertados = cursor.rowcount
            print(f'Registros insertados: {reg_insertados}')
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Insertar varios registros

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Juan', 'Rodriguez', 'jgarcia@email.com'),
                ('Ana', 'Martinez', 'amartinez@email.com'),
                ('Ruben', 'Sanchez', 'rsanchez@email.com'),
            )
            cursor.executemany(sentencia, valores)
            reg_insertados = cursor.rowcount
            print(f'Registros insertados: {reg_insertados}')
except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Actualizar un registro

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Rodrigo', 'Suarez', 'rsuarez@email.com', '1')
            cursor.execute(sentencia, valores)
            reg_actualizado = cursor.rowcount
            print(f'Registro actualizado: {reg_actualizado}')

except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Actualizar varios resgistros

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Rodrigo', 'Suarez', 'rsuarez@email.com', '1'),
                ('Marta', 'Garcia', 'mgarcia@email.com', '2')
            )
            cursor.executemany(sentencia, valores)
            reg_actualizado = cursor.rowcount
            print(f'Registro actualizado: {reg_actualizado}')

except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Eliminar un resgistro

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporciona el id_persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            reg_eliminado = cursor.rowcount
            print(f'Registro eliminado: {reg_eliminado}')

except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()

##############################################################################

# Eliminar varios resgistros

conexion = psycopg2.connect(user='postgres', password=psw,
                            host='127.0.0.1', port=5432, database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar: ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            reg_eliminados = cursor.rowcount
            print(f'Registros eliminados: {reg_eliminados}')

except Exception as e:
    print(f'Ocurrio un error:  {e}')
finally:
    conexion.close()