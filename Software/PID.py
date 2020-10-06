import RPi.GPIO as GPIO
import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt 
import math
import serial


#--------------Variable Global que guarda los datos-------------
class Data():

	def __init__(self):

		self.lat=0
		self.long=0
		self.curso=0
		self.escan=0
		self.final=0

#---------------------------------------------------------------GPS------------------------------------------------------------
def GPS():
	while True:
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout=pynmea2.NMEAStreamReader()
		data=ser.readline()

		if data[0:6] == b'$GPRMC':
		    data = data.decode("utf-8","ignore")
		    datos=pynmea2.parse(data)
		    lat=datos.latitude
		    lng=datos.longitude
		    cur=datos.true_course
		    DATOS.lat = lat
		    DATOS.long = lng
		    DATOS.curso = cur

		#Lo paro cuando termina el recorrido
		if DATOS.final == 1:
			break

	return 0
#--------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------Recorrido---------------------------------------------------------------------
def recorrido():
	#-----------------------------------------Funciones de distancia y curso--------------------------------
	def distancia(lat1, lng1 , waypoint):
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		r=6371000
		c=(math.pi)/180
		#Fórmula de haversine
		d = 2*r*math.asin(math.sqrt(math.sin(c*(lat2-lat1)/2)**2 + math.cos(c*lat1)*math.cos(c*lat2)*math.sin(c*(lng2-lng1)/2)**2))
		return d

	def DireccionDeseada(lat1, lng1, waypoint):
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		dlon=lng2-lng1 
		a1=math.sin(dlon)*math.cos(lat2)
		a2=(math.cos(lat1)*math.sin(lat2))-(math.sin(lat1)*math.cos(lat2)*math.cos(dlon))
		curso=math.atan2(a1, a2)

		if(curso < 0):
			curso += 2*math.pi

		return math.degrees(curso)

	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 2):
			return 0
		else:
			return 1
	#--------------------------------------------------------------------------------------------------------

	#-----------------------------------------------------Control PID----------------------------------------------------------------
	def controlPID(waypoint):
		KP = 1 #Constante Proporcional
		KI = 0.1 #Constante Integral
		KD = 0.2 #Constante Derivativa
		ZI = 5 #Zona activa de la Integral

		while DeltaD >= 0.005 or DeltaD <= -0.005: #Le pusimos que funcione hasta un error un poco mayor a 0 debido a el margen de error del GPS
			#Primero calculo el error
			DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
			DA= DATOS.curso #Direccion actual dado por el modulo gps
			DeltaD= DD - DA
			
			if DeltaD <= ZI and (DeltaD >= 0.005 or DeltaD <= -0.005):
				#Si estamos en la zona activa de la integral empezamos a sumar ángulo
				errorT += DeltaD
			else:
				#Si estamos fuera de la zona activa de la integral, asignamos un 0 a la integral
				errorT = 0

			if errorT >= 50/KI:
				#Le ponemos un límite a la integral
				errorT = 50/KI

			Proporcional = DeltaD * KP
			Integral = errorT * KI
			Derivativa = (DeltaD - UltimoError) * KD

			UltimoError = DeltaD #Guardo el último error

			#Obtengo el valor del ángulo para el timón
			angulo = Proporcional + Integral + Derivativa

			if abs(angulo) >= 30 and DeltaD > 0: #Caso: DeltaD positivo
				#Si el ángulo es mayor que el máximo de giro del timón giro 30°
				angulo = 30

			if abs(angulo) >= 30 and DeltaD < 0: #Caso: DeltaD negativo
				#Si el ángulo es mayor que el máximo de giro del timón giro 30°
				angulo = -30

			return angulo
	#----------------------------------------------------------------------------------------------------------------------------------------------


	#en esta array se guardan los waypoints a recorrer 
	#cada waypoint se guarda en una fila distinta
	waypoints = np.array([latitud, longitud], [latitud, longitud])

	for i in range (0, len(waypoints)):
		#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			timon = controlPID(waypoints[i])
			print(timon)
			time.sleep(1)

		DATOS.final = 1

	print("Finalizó el recorrido")
#------------------------------------------------------------------------------------------------------------------------------------------------------




#////////////////////////////////////////////////////////////////////Inicio el programa/////////////////////////////////////////////////////////////////

DATOS = Data()

TGPS = threading.Thread(name="GPS", target=GPS)
TPID = threading.Thread(name="PID", target=recorrido)
TGPS.start()

time.sleep(5)
TPID.start()