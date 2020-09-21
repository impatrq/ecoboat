import time
import RPi.GPIO as GPIO
import numpy as np 

def USconfig(){
	#libreria para el control de los sensores us
	#estado = verde

	TRIG1 = 5
	TRIG2 = 2 
	ECHO = 26 

	GPIO.setmode(GPIO.BCM)
	# Establecer que TRIG es un canal de salida.
	GPIO.setup(TRIG1, GPIO.OUT)
	GPIO.setup(TRIG2, GPIO.OUT)
	# Establecer que ECHO es un canal de entrada.
	GPIO.setup(ECHO, GPIO.IN)

	#pines de control
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)

	#hay que darle unos segundos a los sensores para que se estabilicen
	GPIO.output(TRIG1, 0)
	GPIO.output(TRIG2, 1)
	time.sleep(2)
}

def medicion():

	# Prender el pin activador por 10 microsegundos
	# y después volverlo a apagar.
	GPIO.output(TRIG1, 1)
	GPIO.output(TRIG2, 0)
	time.sleep(0.00001)
	GPIO.output(TRIG1, 0)
	GPIO.output(TRIG2, 1)

	# En este momento el sensor envía 8 pulsos
	# y pone a ECHO en HIGH
	# cuando llegan los pulsos lo pone en LOW
	# hay que medir el tiempo 

	while True:	
		if (GPIO.input(ECHO) == 1):
			break

	pulso_inicio = time.time()
	while True:
		if (GPIO.input(ECHO) == 0):
			break
	pulso_fin = time.time()

	# La medición del tiempo es en segundos.
	duracion = pulso_fin - pulso_inicio

	# Calcular la distancia usando la velocidad del
	# sonido y considerando que la duración incluye
	# la ida y vuelta.
	distancia = (17150 * duracion)

	return distancia

def lectura():
	datos= np.empty((1, 8))
	pos=0
	for i in (0, 1):
		for j in (0, 1):
			for k in (0, 1):
				GPIO.output(23, i)
				GPIO.output(24, j)
				GPIO.output(25, k)
				datos[0, pos]= medicion()
				
				if (datos[pos] > 400):
					datos[pos]=0

				pos+=1
	return datos
			