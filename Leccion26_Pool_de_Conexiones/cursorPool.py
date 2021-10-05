from conexion import Conexion
from logger_base import log


class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicip del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

	# Tipo, valor y detalle de la excepción    
    def __exit__(self, t_Excption, v_Excption, d_Excption):
        log.debug(f'Se Ejecuta el método __exit__')
        if v_Excption:
            self._conexion.rollback()
            log.error(f'Rollback:{t_Excption},{v_Excption},{d_Excption}')
        else:
        	self._conexion.commit()
        	log.debug('Commit de la transacción')
        self._cursor.close()
       	Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
	with CursorPool() as cursor:
		log.debug('Dentro del bloque with')
		cursor.execute("SELECT * FROM persona")
		log.debug(cursor.fetchall())
