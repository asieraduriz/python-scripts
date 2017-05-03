#!/usr/bin/env python
import sys

class Usuario:
	def __init__(self):
		self.nombre = ''
		self.edad = 0
		self.altura = 0.0
		self.peso = 0.0
    
	def mostrar(self):
		print ()
		print ('Informacion de usuario :')
		print ('Nombre usuario : ', self.nombre)
		print ('Edad   usuario : ', self.edad)
		print ('Altura usuario : ', self.altura)
		print ('Peso   usuario : ', self.peso)
    
	def cargarUsuario(self):
		self.nombre = input('Escribe usuario: ')
		self.edad = int(input('Escribe edad: '))
		self.altura = float(input('Escribe altura en metros: '))
		self.peso = float(input('Escribe peso en kilogramos: '))
    
	def almacenar(self):
		f = open('usuarios.info','w')
		f.write(self.nombre + '\n')
		f.write(str(self.edad) + '\n')
		f.write(str(self.altura) + '\n')
		f.write(str(self.peso) + '\n')
		f.close()

	def cargarFichero(self):
		f = open('usuarios.info', 'r')
		self.nombre = f.readline().rstrip()
		self.edad = int(f.readline())
		self.altura = float(f.readline())
		self.peso = float(f.readline())


theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'LECTURA':
    theUser = Usuario()
    theUser.cargarFichero()
else:
    theUser = Usuario()
    theUser.cargarUsuario()
    theUser.almacenar()
    
theUser.mostrar()
