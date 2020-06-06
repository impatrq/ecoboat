import time
import RPi.GPIO as GPIO
import numpy as np 

#libreria para el control de los sensores us
#estado = verde

TRIG = 23 #hay que especificar los puertos
ECHO = 24 #estos son ejemplos

GPIO.setmode(GPIO.BCM)
# Establecer que TRIG es un canal de salida.
GPIO.setup(TRIG, GPIO.OUT)
# Establecer que ECHO es un canal de entrada.
GPIO.setup(ECHO, GPIO.IN)

#pines de control
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

def medicion():


	# Apagar el pin activador y permitir un par de
	# segundos para que se estabilice.
	GPIO.output(TRIG, "False")
	time.sleep(2)

	# Prender el pin activador por 10 microsegundos
	# y después volverlo a apagar.
	GPIO.output(TRIG, "True")
	time.sleep(0.00001)
	GPIO.output(TRIG, "False")

	# En este momento el sensor envía 8 pulsos
	# y pone a ECHO en HIGH
	# cuando llegan los pulsos lo pone en LOW
	# hay que medir el tiempo 

	pulso_fin = time.time()
	while True:
		if (GPIO.input(ECHO) == "False"):
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
	for i in ("False", "True"):
		for j in ("False", "True"):
			for k in ("False", "True"):
				GPIO.output(1, i)
				GPIO.output(2, j)
				GPIO.output(3, k)
				datos[0, pos]= medicion()
				pos+=1
	return datos
	
lectura()			