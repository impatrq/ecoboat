import time as tm 
import numpy as np 
#uso numpy ya que tiene un mejor manejo de matrices

def DireccionActual():
	#determinar la direccion actual, esta funcion ya esta en la libreria del gps
	#para que el gps determine la direccion debemos recorrer unos metros
	return 1

def DireccionDeseada(waypoint):
	#determinar la direccion deseada, esta funcion ya esta en la libreria del gps
	#al gps le debemos decir hacia donde queremos ir y nos dera la direccion en grados
	return 1 

def deltaDireccion(direcdeseada, direcactual):
	#calcular cuantos grados debemos girar
	return 1

def Girar(deltadirec):
	return 0

def LlegadaAlWP(destino):
	#comparar nuestra direccion con el destino
	return 0

#en esta array se guardan los waypoints a recorrer 
#cada waypoint se guarda en una fila distinta
waypoints= np.empty(TotaldeWaypoints, 2)

#se recorren todos los watpoints uno por uno
for i in range (0, len(waypoints)):

	#waypoints[i] hace referrencia a la fila entera
	direcDeseada=DireccionDeseada(waypoints[i])

	#la idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
	while(LlegadaAlWP(waypoints[i]) != 1):
		deltadirec= deltaDireccion(direcDeseada, DireccionActual())
		Girar(deltadirec)
		tm.sleep(xx)