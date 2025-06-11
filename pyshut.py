# -*- coding: utf-8 -*-

import os
import time
import sys

def temporizar(tiempo):
        t = 0
        while t < tiempo:
                print("Minuto {}".format(t))
                time.sleep(60)
                t += 1

def apagar():
        print("Ejecutando poweroff")
        os.system("sudo poweroff")

if __name__ == "__main__":
    mins = 0
    if len(sys.argv) > 1:
        try:
            mins = int(sys.argv[1])
        except ValueError:
            print("El parámetro debe ser numérico")
            sys.exit(1)
    mensaje = "Advertencia el sistema se apagará en {} minutos"
    if mins is not None and mins > 0:
        print(mensaje.format(mins))
        temporizar(mins)
    else:
        print(mensaje.format(10))
        temporizar(10)
    apagar()
