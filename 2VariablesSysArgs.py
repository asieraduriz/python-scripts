#!/usr/bin/env python
# Script con entradas

import sys

nombre = sys.argv[1]
edad = int(sys.argv[2])

print ('Hola,', nombre + '. Serás 100 en', (100 - edad), 'años!')
