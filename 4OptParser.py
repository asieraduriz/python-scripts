#!/usr/bin/env python
# Years till 100
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', '--nombre', dest='nombre', help='Tu nombre')
parser.add_option('-e', '--edad', dest='edad', help='Tu edad', type=int)

(options, args) = parser.parse_args()

if options.nombre is None:
    options.nombre = nput('Enter Name:')

if options.edad is None:
    options.edad = int(raw_input('Enter Age:'))

frase_inicio = 'Hola ' + options.nombre + ','

if options.age == 100:
    sayAge = 'You are already 100 years old!'
elif options.age < 100:
    sayAge = 'You will be 100 in ' + str(100 - options.age) + ' years!'
else:
    sayAge = 'You turned 100 ' + str(options.age - 100) + ' years ago!'

print sayHello, sayAge
