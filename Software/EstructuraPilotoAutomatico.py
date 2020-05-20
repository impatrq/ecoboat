import time as tm 
import numpy as np 
import motores as mt 
import gps
import math

def EvitarObstaculos():
    #Sensores para evitar que el barco choque
    return 1

def DireccionActual():
	#determinar la direccion actual, esta funcion ya esta en la libreria del gps
	#para que el gps determine la direccion debemos recorrer unos metros
	return 1

def DireccionDeseada(waypoint):
	#determinar la direccion deseada, esta funcion ya esta en la libreria del gps
	#al gps le debemos decir hacia donde queremos ir y nos dera la direccion en grados
	return 1 

def Girar(motor, waypoint):

	#primero hace un primer chequeo de la diferencia de direccion
	DD= DireccionDeseada(waypoint)
	DA= DireccionActual()
	DeltaD= DD - DA

	#si no es demaciado no gira
	if (abs(DeltaD)<= 10):
		return 0
	#si es mucho lo corrije
	else:
		#verifica si hay que girar a la derecha o izquierda
		if(DeltaD<0):
			motor.girarH(10)
			giro=1
		else:
			motor.girarAH(10)
			giro=0

		#se mantiene girando hasta que corrija el rumbo
		while(abs(DeltaD) >= 5):
			DD= DireccionDeseada(waypoint)
			DA= DireccionActual()
			DeltaD= DD - DA
			tm.sleep(0.5)

		#vuelve a su posicion el timon
		if (giro==1):
			motor.girarAH(10)
		else:
			motor.girarH(10)

	return 0

def LlegadaAlWP(destino):
	#comparar nuestra direccion con el destino
	dis= gps.distancia(pos, destino)

	if(abs(dis) <= 5):
		return 0
	else:
		return 1
	

pos= gps.Gps()

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
		Girar(timon, waypoints[i])
		tm.sleep(30)
