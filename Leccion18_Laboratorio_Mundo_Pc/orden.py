from computadora import Computadora

class Orden:
	cntOrden = 0
	def __init__(self, computadoras):
		Orden.cntOrden += 1
		self._idOrden = Orden.cntOrden
		self._computadora = computadoras

	def addPc(self, computadora):
		self._computadora.append(computadora)


	def __str__(self):
		strPc = ''
		for computadora in self._computadora:
			strPc  += computadora.__str__()

		return f'Orden: {self._idOrden} \nComputadoras: {strPc}'
			