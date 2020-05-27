import time as tm 
import numpy as np 
import motores as mt 
import gps
import math

def EvitarObstaculos():
    #Sensores para evitar que el barco choque
    return 1

def DireccionActual():
	Gps.lectura()
	return Gps.cur

def DireccionDeseada(waypoint):
	Gps.lectura()
	return gps.cursoHacia(Gps.lat, Gps.lng, waypoint)

def Girar(waypoint):

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
			timon.girarH(10)
			giro=1
		else:
			timon.girarAH(10)
			giro=0

		#se mantiene girando hasta que corrija el rumbo
		while(abs(DeltaD) >= 5):
			DD= DireccionDeseada(waypoint)
			DA= DireccionActual()
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
	Gps.lectura()
	dis= gps.distancia(Gps.lat, Gps.lng, destino)

	if(abs(dis) <= 5):
		return 0
	else:
		return 1
	
#inicio el gps
Gps= gps.Gps()

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
		tm.sleep(0.05)
