import os
import time


def temporizar(tiempo):
	t = 1
	while (t < tiempo):
		print "Minuto {}".format(t)
		time.sleep(60)
		t = t + 1

def apagar():
	print "Ejecucion poweroff"

if __name__ == "__main__":
	mins = sys.argv[1]
	mensaje = "Advertencia el sistema se apagará en {} minutos"
	if mins is not None and mins > 0:
		print mensaje.format(mins)
		temporizar(mins)
	else:
		print mensaje.format(10)
		temporizar(10)
	apagar()
