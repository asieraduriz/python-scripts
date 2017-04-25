#!/usr/bin/env python
# Edad hasta 100
import sys

nombre = ''

if len(sys.argv) > 1:
    nombre = sys.argv[1]
else:
    nombre = input('Escribe nombre: ')

edad = 0

if len(sys.argv) > 2:
    edad = int(sys.argv[2])
else:
    edad = int(input('Escribe edad: '))

frase_inicio = 'Hola ' + nombre + ', '

if edad == 100:
    frase_inicio = 'Tienes exactamente 100 años!'
elif edad < 100:
    frase_inicio = 'Tendrás 100 años en ' + str(100 - edad) + ' años!'
else:
    frase_inicio = 'Cumpliste los 100 hace ' + str(edad - 100) + ' años!'

print (nombre, frase_inicio)
