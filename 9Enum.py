#!/usr/bin/env python

from enum import Enum
class Genero(Enum):
	MASCULINO = 0
	FEMENINO = 1
	NO_ESPECIFICADO = 2

class Usuario:
	
	def __init__(self):
		self.nombre = ''
		self.edad = 0
		self.genero = Genero.NO_ESPECIFICADO

	def mostrar(self):
		if self.genero == Genero.MASCULINO:
			print (self.nombre, 'Es un hombre')
		elif (self.genero == Genero.FEMENINO):
			print (self.nombre, 'Es una mujer')
		else:
			print (self.nombre, 'Sin especificar')


user1 = Usuario()
user1.nombre = 'Mike'
user1.genero = Genero.MASCULINO

user2 = Usuario()
user2.nombre = 'Sally'
user2.genero = Genero.FEMENINO

user1.mostrar()
user2.mostrar()
