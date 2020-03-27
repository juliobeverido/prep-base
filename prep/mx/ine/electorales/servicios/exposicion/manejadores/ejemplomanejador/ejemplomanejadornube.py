"""
	Copyright (c)  INE, UNICOM, México.
	Todos los derechos reservados.

	nombre_archivo=
	fecha_creacion= date, time

	Este software es información confidencial, propiedad del
	INE (Instituto Nacional Electoral). Esta información 
	no deberá ser divulgada y solo se podrá utilizar con base
	a los términos que el propio Instituto determine.
"""

"""
	TODO [Agregar importaciones requeridas de la clase]
"""

from ....servicios.ejemploservicio.ejemploservicio import EjemploServicio
def nombre_funcion(event, context):
	ejemplo_1 = EjemploServicio()
	return "Mensaje: <br>" + ejemplo_1.ejecuta_algoritmo() + " <br> EjemploManejador: EndPoint accedido" 