def tomarWaypoint():
	return Waypoint

def DireccionActual():
	return 1

def DireccionDeseada(direcactual, waypoint):
	return 1 

def deltaDireccion(direcdeseada, direcactual):
	return 1

def Girar(deltadirec):
	return 0


DireccionDeseada(DireccionActual, tomarWaypoint)
deltadireccion= deltaDireccion(DireccionDeseada, DireccionActual)
Girar(deltadireccion)