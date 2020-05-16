import time as tm 
import numpy as np 
import motores as mt 
#uso numpy ya que tiene un mejor manejo de matrices

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
			motor.girarD(10)
			giro=1
		else:
			motor.girarI(10)
			giro=0

		#se mantiene girando hasta que corrija el rumbo
		while(abs(DeltaD) >= 5):
			DD= DireccionDeseada(waypoint)
			DA= DireccionActual()
			DeltaD= DD - DA
			tm.sleep(0.5)

		#vuelve a su posicion el timon
		if (giro==1):
			motor.girarI(10)
		else:
			motor.girarD(10)

	return 0

def LlegadaAlWP(destino):
	#comparar nuestra direccion con el destino
	return 0

timon= mt.PaP(1, 2, 3, 4)

#en esta array se guardan los waypoints a recorrer 
#cada waypoint se guarda en una fila distinta
waypoints= np.empty(TotaldeWaypoints, 2)

#se recorren todos los watpoints uno por uno
for i in range (0, len(waypoints)):
	#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
	while(LlegadaAlWP(waypoints[i]) != 1):
		Girar(timon, waypoints[i])
		tm.sleep(30)