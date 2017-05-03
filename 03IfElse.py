#!/usr/bin/env python
import sys

pswd = 'secreto' # Mi password

entrada_usuario = input('Introduce contraseña: ')

if entrada_usuario == pswd:
    print ('Acceso autorizado!')
else:
    print ('Acceso denegado!')
    sys.exit(0)

print ('Bienvenido/a')
