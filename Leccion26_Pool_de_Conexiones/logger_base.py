import logging as log

# Se muestran mensajes en funcion de la configuracion
# Nivel DEBUG: debug, info, warning, error, critical
# Nivel INFO: info, warning, error, critical
# Nivel WARNING: warning, error, critical
# Nivel ERROR: error, critical
# Nivel CRITICAL: critical 

#log.basicConfig(level=log.DEBUG)
#log.basicConfig(level=log.INFO)
#log.basicConfig(level=log.WARNING) # Configuracion por defecto
#log.basicConfig(level=log.ERROR)
#log.basicConfig(level=log.CRITICAL)

log.basicConfig(level=log.DEBUG, 
				format = '%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)s] %(message)s',
				datefmt = '%I:%M:%S:%p',
				handlers = [
						log.FileHandler('capa_datos.log'),
						log.StreamHandler()
				])

if __name__ == '__main__':
	log.debug('Mensaje a nivel Debug')
	log.info('Mensaje a nivel de Info')
	log.warning('Mensaje a nivel de Warning')
	log.error('Mensaje a nivel Error')
	log.critical('Mensaje a nivel Critico')