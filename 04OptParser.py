#!/usr/bin/env python
# Years till 100
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', '--nombre', dest='nombre', help='Tu nombre')
parser.add_option('-e', '--edad', dest='edad', help='Tu edad', type=int)

(options, args) = parser.parse_args()

if options.nombre is None:
    options.nombre = input('Escribe nombre: ')

if options.edad is None:
    options.edad = int(input('Escribe edad: '))

frase_inicio = 'Hola ' + options.nombre + ','

if options.edad == 100:
    frase_inicio = 'Tines 100 años!'
elif options.edad < 100:
    frase_edad = 'Serás 100 en ' + str(100 - options.edad) + ' años!'
else:
    frase_edad = 'Cumpliste 100 años hace ' + str(options.age - 100) + ' años!'

print (options.nombre, frase_edad)
