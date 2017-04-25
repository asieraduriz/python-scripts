#!/usr/bin/env python

ristraNumeros = input('Escribe numeros separados con 1 espacio separado: ')
listaNums = ristraNumeros.split()

for numero in listaNums:
    if not numero.isdigit():
        priNegativo o no letra:', numero)
    elif int(numero) < 1:
        print ('Digito menor a 1:', numero)
    elif int(numero) > 100:
        print ('Numero superior a 100:', numero)
    else:
        print ('Number is valid:', numero)
