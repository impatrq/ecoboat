import RPi.GPIO as GPIO
import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt 
import math


#------------Variable Global que guarda los datos-------------
class Data():

	def __init__(self):

		self.lat=0
		self.long=0
		self.curso=0
		self.escan=0

#---------------------------------------------------------------GPS------------------------------------------------------------
def GPS():

	def disponible():
            #funcion que detecte disponibilidad de datos
            port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                datos=pynmea2.parse(newdata)
                while True:
                    if datos.status == A:
                        break

                DATOS.escan==1
            return 0
        
	def lectura():
	    port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                pos=pynmea2.parse(newdata)
		DATOS.lat=pos.latitude
		DATOS.long=pos.longitude
		DATOS.curso=pos.direction

	    time.sleep(0.5)
	    return 0

        disponible()

        if (DATOS.escan==1):
            while True:
                lectura()
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
		d = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
		return d

	def DireccionDeseada(lat1, lng1, waypoint):
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		dlon=lng2-lng1 
		a1=sin(dlon)*cos(lat2)
		a2=(cos(lat1)*sin(lat2))-(sin(lat1)*cos(lat2)*cos(dlon))
		curso=atan2(a1, a2)

		if(curso < 0):
			curso += 2*math.pi

		return degrees(curso)

	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 5):
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

			print(angulo)
			return angulo
	#----------------------------------------------------------------------------------------------------------------------------------------------


	#en esta array se guardan los waypoints a recorrer 
	#cada waypoint se guarda en una fila distinta
	waypoints = np.empty((TotaldeWaypoints, 2))

	for i in range (0, len(waypoints)):
		#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			controlPID(waypoints[i])
			time.sleep(1)
		i++

	print("Finalizó el recorrido")
#------------------------------------------------------------------------------------------------------------------------------------------------------




#////////////////////////////////////////////////////////////////////Inicio el programa/////////////////////////////////////////////////////////////////

TGPS = threading.Thread(name="GPS", target=GPS)
TPID = threading.Thread(name="PID", target=recorrido)
TGPS.start()

while True:
    if(DATOS.escan==1): #Empiezo con el programa una vez que el GPS empieza a mostrar posición
    	break

TPID.start()