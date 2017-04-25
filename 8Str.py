#!/usr/bin/env python

strUsuarios = 'rpulley  ,    jsmith, svai,  jsatriani    ,ymalmsteen    '
listaUsuarios = strUsuarios.split(',')

for usuario in listaUsuarios:
    trimUser = user.strip()
    trimUserR = user.rstrip()
    trimUserL = user.lstrip()

    primeraInicial = trimUser[:1]
    ultimaInicial = trimUser[1:2]
    apellido = trimUser[1:]

    print ('Usuario : \'' + usuario + '\'')
    print ('LTrim: \'' + trimUserL + '\'')
    print ('RTrim: \'' + trimUserR + '\'')
    print (' Trim: \'' + trimUser + '\'')

    print ('Primera Inicial:', primeraInicial.upper())
    print ('Ultima Inicial: ', ultimaInicial.upper())
    print ('Apellido:', apellido)

    print ()
