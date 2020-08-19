import RPi.GPIO as GPIO
import motores as mt

GPIO.setmode(GPIO.BCM)

timon= mt.PaP(4, 17, 27, 22)
Cangilon= mt.Cangilon(6, 13, 50)			#Con un 1 en el pin de selección giramos horario, con un 0 antihorario.
motorDirec= mt.Propulsion(18, 12, 50)		#Con el 12 giro horario y con el 18 antihorario.

while giro != 3:
	giro = input()

	if giro == 1:
		motorDirec.girarD()

	if giro == 2:
		motorDirec.girarI()

	if giro == 0:
		motorDirec.detener()