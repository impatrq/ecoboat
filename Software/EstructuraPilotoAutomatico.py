import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt 
import math

#estado del codigo= naranja

#//////////////// defino la lista que va a guardar las variables/////////////

data= [0,0,0,0]
#data 0 = latitud
#data 1 = longitud
#data 2 = curso
#data 3 = fin de escaneo

#//////////////// funciones de Piloto Automatico////////////////

def pilotoAutomatico():

	def EvitarObstaculos():
    #Sensores para evitar que el barco choque
    return 1

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

	def Girar(waypoint):

		#primero hace un primer chequeo de la diferencia de direccion
		DD= DireccionDeseada(data[0], data[1], waypoint)
		DA= data[2] #Direccion actual dado por el modulo gps
		DeltaD= DD - DA

		#si no es demaciado no gira
		if (abs(DeltaD)<= 10):
			return 0
		#si es mucho lo corrije
		else:
			#verifica si hay que girar a la derecha o izquierda
			if(DeltaD<0):
				timon.girarH(10)
				giro=1
			else:
				timon.girarAH(10)
				giro=0

			#se mantiene girando hasta que corrija el rumbo
			while(abs(DeltaD) >= 5):
				DD= DireccionDeseada(data[0], data[1], waypoint)
				DA= data[2]
				DeltaD= DD - DA
				tm.sleep(0.5)

			#vuelve a su posicion el timon
			if (giro==1):
				timon.girarAH(10)
			else:
				timon.girarH(10)

		return 0

	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(data[0], data[1], destino)

		if(abs(dis) <= 5):
			return 0
		else:
			return 1

	timon= mt.PaP(1, 2, 3, 4)
	motorDirec= mt.puenteH(1,2)
	#meto primera
	motorDirec.girarD()

	#en esta array se guardan los waypoints a recorrer 
	#cada waypoint se guarda en una fila distinta
	waypoints= np.empty((TotaldeWaypoints, 2))

	#se recorren todos los watpoints uno por uno
	for i in range (0, len(waypoints)):
		#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			Girar(waypoints[i])
			time.sleep(5)

#//////////////// funciones de RF //////////////////////

def comRF():
	#codigo de modulos RF

#//////////////// funciones de GPS //////////////////////

def GPS():

	def lectura():
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout=pynmea2.NMEAStreamReader()
		data=ser.readline()

		if data[0:6] == "$GPRMC":
			datos=pynmea2.parse(newdata)
			data[0]=datos.latitude
			data[1]=datos.longitude
			data[2]=datos.direction

		time.sleep(0.05)
		return 0

	while True:
		lectura()
		time.sleep(1)

#//////////////// programa /////////////////////////

#espero a que haya data para arrancar

def disponible():
	#funcion que detecte disponibilidad de datos
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout=pynmea2.NMEAStreamReader()
	data=ser.readline()
	#falta terminar
	return 0

while True:
	if (disponible()==1):
		data[3]==1
		break

#////////////// inicio los hilos ////////////////////

TGPS = threading.Thread(name="GPS", target=GPS)
TPA = threading.Thread(name="PA", target=pilotoAutomatico)
TRF = threading.Thread(name="RF", target=comRF)

TPA.start()
TRF.start()
TGPS.start()

TPA.join()
TRF.join()
TGPS.join()