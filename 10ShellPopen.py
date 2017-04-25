#!/usr/bin/env python
import subprocess

proc = subprocess.Popen(['tail', '-500', 'usuarios.info'], stdout=subprocess.PIPE)

for linea in proc.stdout.readlines():
    print (linea.rstrip())
