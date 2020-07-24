def controlPID(waypoint)
	KP = 1 #Constante Proporcional
	KI = 0.1 #Constante Integral
	KD = 0.2 #Constante Derivativa
	ZI = 5 #Zona activa de la Integral

	while DeltaD >= 0.005 or DeltaD <= -0.005:
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

		timon.girar(angulo)