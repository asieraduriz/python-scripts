#!/usr/bin/env python
import sys

logLevel = int(sys.argv[1])

def logit(level, msg):
    if level >= logLevel:
        print 'MSG' + str(level) + ':', msg

def getUser():
    logit(2, 'Entrando metodo getUser()...')
    user = input('Escribe usuario: ')
    logit(1, 'Terminando metodo getUser()...')
    return user

logit(3, 'Comenzando script...')
logit(3, 'Usuario creado: ' + getUser())
logit(3, 'Finalizando script.')
