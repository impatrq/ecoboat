#Esta es la librería que utilizamos para controlar las mediciones de los sensores Ultrasónicos
import time
import RPi.GPIO as GPIO
import numpy as np 

#--------------------Configuración de los Pines-----------------------
TRIG1 = 5
TRIG2 = 2 
ECHO = 26 

GPIO.setmode(GPIO.BCM)
# Establecer que TRIG es un canal de salida.
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(TRIG2, GPIO.OUT)
# Establecer que ECHO es un canal de entrada.
GPIO.setup(ECHO, GPIO.IN)

#Pines de control de los multiplexores
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

#hay que darle unos segundos a los sensores para que se estabilicen
GPIO.output(TRIG1, 0)
GPIO.output(TRIG2, 1)
time.sleep(2)
#---------------------------------------------------------------------

def medicion():	#Esta es la función que realiza la medición con los sensores

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

def lectura():	#Esta función va variando los pines selectores de los multiplexores para medir de forma sincrónica
#con los 8 sensores. Además los guarda en un array para mayor facilidad.

	datos= np.empty((1, 8))	#Array que guarda los datos de distancia de los sensores
	pos=0	#Numero que se va sumando para ir pasando de sensor en sensor
	#Realizamos varios bucles para poder llamar a todos los ultrasónicos con los pines selectores
	for i in (0, 1):
		for j in (0, 1):
			for k in (0, 1):
				GPIO.output(23, i)
				GPIO.output(24, j)
				GPIO.output(25, k)
				datos[0, pos]= medicion()
				
				if (datos[pos] > 400):	#Acá indicamos que si el sensor no mide nada (mayor a 400m) indique un 0
					datos[pos]=0

				pos+=1
	return datos
			