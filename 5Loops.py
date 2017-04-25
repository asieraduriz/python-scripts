#!/usr/bin/env python

import random

respuesta = random.randint(1, 10)
num = 0

while num != respuesta:
    num = int(input('¿Podrías acertar el número? '))

    if num != respuesta:
        print ('Eeeeeeeeeeegggggggg, error')

print ('Woohoo, acertaste')
