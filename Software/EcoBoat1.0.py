import RPi.GPIO as GPIO			#Libreréa de pines GPIO
import time
import threading 				#Librería de los hilos
import pynmea2 as nmea 			#Librería del GPS
import serial 					#Librería para el puerto serial del GPS
import numpy as np 				#Librería de arrays
import motores as mt 			#Librería de los motores (Desarrollada por el equipo de EcoBoat)
import math 					#Librería de funciones matemáticas
from lib_nrf24 import NRF24 	#Librería del NRF24l01
import spidev 					#Librería de comunicación SPI
import sensoresUS as US  		#Librería de los Sensores Ultrasónicos (Desarrollada por el equipo de EcoBoat)

#Defino el modo de uso de los pines GPIO
GPIO.setmode(GPIO.BCM)

#---------------------Variable global-----------------------
class Data():	#Aca guardamos todos los datos que van a ser utilizados por más de un hilo

	def __init__(self):
		self.lat=0		#Latitud
		self.long=0		#Longitud
		self.curso=0	#Curso
		self.escan=0	#Esta variable sirve para saber si el GPS recibe datos
		self.fin=0		#Esta variable es para detectar cuando el barco finaliza su recorrio
		self.timon=0	#Ángulo del timón, se utiliza para controlar el motor paso a paso
		self.bateria=0  #Porcentaje de batería
		self.motProp=0  #Consumo del motor de propulsión
		self.motCang=0  #Consumo del motor de la cinta transportadora

DATOS= Data()
#-----------------------------------------------------------

#--------------------------------------------------------------------GPS-----------------------------------------------------------------------
def GPS():

	def disponible():
		while True:
	        #Función que detecta disponibilidad de datos
	        port="/dev/ttyAMA0"		#Puerto UART de la Raspberry
			ser=serial.Serial(port, baudrate=9600, timeout=0.5)	#Inicio el puerto serial
			#Mido posición con el GPS
			dataout=pynmea2.NMEAStreamReader()
			data=ser.readline()
			#Tomo únicamente la línea que nos interesa que posee la posición
	        if data[0:6] == b'$GPRMC':
			    data = data.decode("utf-8","ignore")
			    datos=pynmea2.parse(data)
			    DATOS.lat = datos.latitude
			    DATOS.long = datos.longitude
			    DATOS.curso = datos.true_course

			    DATOS.escan = 1
			    break
        return 0
        
	def lectura(self):	#----------------Función que toma los datos de posición-------------------
		port="/dev/ttyAMA0"		#Puerto UART de la Raspberry
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)	#Inicio el puerto serial
		
		while True:
			#Mido posición con el GPS
			dataout=pynmea2.NMEAStreamReader()
			data=ser.readline()

			#Tomo únicamente la línea que nos interesa que posee la posición
			if data[0:6] == b'$GPRMC':
			    data = data.decode("utf-8","ignore")
			    datos=pynmea2.parse(data)
			    DATOS.lat = datos.latitude
			    DATOS.long = datos.longitude
			    DATOS.curso = datos.true_course

			#Si el barco finalizó el recorrido, salimos del while
			if DATOS.fin = 1:
				break


	while DATOS.escan != 1:
		disponible()	#Una vez que detecto disponibilidad de datos inicio la lectura de datos e inicio los otros
						#hilos

    lectura()                
#-------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------Conversor Analógico/Digital--------------------------------------------------------
def conversor():	#El conversor A/D funciona con comunicación SPI
	#Inicio la comunicación SPI
	spi = spidev.SpiDev()
	spi.open(0, 0)

	spi.max_speed_hz = 300000
	spi.mode = 0

	while True:
		for canal in range (0, 3):	#Voy tomando los datos de todos los canales
			#Primero tomamos los datos crudos del conversor A/D (le digo que canal y que modo quiero usar)
	        datosCrudos = spi.xfer([(12 + canal), 0, 0])
	        #Proceso esta información para tenerla en un numero de 0 a 1023
	        datosProcesados = ((datosCrudos[1]) << 1) + (datosCrudos[2] >> 7)
	        #--------------------------------------------Conversión a porcentaje de batería--------------------------------------------
	        if canal == 0:	#Canal del sensor de porcentaje de la batería
			    if datosProcesados < 808: #Si es menor a 808bits significa que estoy al 0% (11,8V)
			    	porcentaje = 0
			    else:
			    	porcentaje = ((datosProcesados - 808) * 100) / float(1023 - 808) #Si el valor es igual o mayor a 808 calculo el procentaje
			    	porcentaje = round(porcentaje)
			    
			    DATOS.bateria = porcentaje
			    return 0
			#-----------------------------------------------Conversión a grados del timón----------------------------------------------
			if canal == 1:	#Canal del sensor de posición del timón
	        	grados = -128 + datosProcesados		#La marca de 0 grados está justo en el medio del pote, por ende, es una conversión de sumar.
	        	
	        	DATOS.timon = grados
	        	return 0
	        #--------------------------------------Conversión a consumo del motor de propulsión (A)------------------------------------
	        if canal == 2:	#Canal del sensor de corriente del motor de propulsión
	        	voltaje = (datosProcesados * 5) / float(1023) #Convierto el valor en bits a volts (0 a 5V)
			    voltaje = round(voltaje, 3) #Redondeo a tres decimales
			    if voltaje <= 2,5: #Si es negativo
			    	consumo = - (voltaje * 0.1) #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)

			    else: #Si es positivo
			    	consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)

			    DATOS.motProp = consumo
			   	return 0
			#-------------------------------Conversión a consumo del motor de la cinta Transportadora (A)------------------------------
			if canal == 3:	#Canal del sensor de corriente del motor de propulsión
	        	voltaje = (datosProcesados * 5) / float(1023) #Convierto el valor en bits a volts (0 a 5V)
			    voltaje = round(voltaje, 3) #Redondeo a tres decimales
			    if voltaje <= 2,5: #Si es negativo
			    	consumo = - (voltaje * 0.1) #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)

			    else: #Si es positivo
			    	consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)

			    DATOS.motCang = consumo
			   	return 0

			#Cuando se finaliza el recorrido, dejamos de sensar datos.
			if DATOS.fin == 1:
				spi.close()
				break
#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------Piloto automático-------------------------------------------------------------
def pilotoAutomático():
	#------------------------Medición de los sensores ultrasónicos---------------
	class mediciones():

			def __init__(self):
				self.Lfi=0
				self.Lfd=0
				self.Lsi=0
				self.Lsd=0
				self.Lli=0
				self.Lld=0
				self.Lti=0
				self.Ltd=0

			def medicion(self):
				medida=US.lectura()
				self.Lfd=medida[0] #Frontal derecho
				self.Lsd=medida[1] #Diagonal derecho
				self.Lld=medida[2] #Lateral derecho
				self.Ltd=medida[3] #Atras derecho
				self.Lti=medida[4] #Atras izquierdo
				self.Lli=medida[5] #Lateral izquierdo
				self.Lsi=medida[6] #Diagonal izquierdo
				self.Lfi=medida[7] #Frontal izquierdo
				
	med = mediciones()
	#---------------------------------------------------------------------------

	#---------------------------------------------Funciones de navegación---------------------------------------------
	#Esta función se utilzia para medir la distancia entre la ubicación actual y el próximo waypoint
	def distancia(lat1, lng1 , waypoint):	#lat1 y lng1 son los datos de posición actual
		lat2=waypoint[0, 0]
		lng2=waypoint[0, 1]
		r=6371000
		c=(math.pi)/180
		#Fórmula de haversine
		a = sin(c*(lat2-lat1)/2)**2
		b = cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2
		d = 2*r*asin(sqrt(a + b))
		return d

	#Esta función nos otorga el curso deseado
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

	#Est afunción nos indica cuando llegamos al waypoint
	def LlegadaAlWP(destino):
		#comparar nuestra direccion con el destino
		dis= distancia(DATOS.lat, DATOS.long, destino)

		if(abs(dis) <= 2):	#Detectamos que llegamos al wp una vez que estamos a menos de 2 metros (por los errores del GPS)
			return 0
		else:
			return 1
	#------------------------------------------------------------------------------------------------------------------

	#--------------------------------------------------Red Neuronal----------------------------------------------------
	def redNeuronal():
		#Código de la red neuronal.
	#------------------------------------------------------------------------------------------------------------------

	#---------------------------------------------------Control PID----------------------------------------------------
	def controlPID(waypoint):	#Es el algoritmo que controla el giro del timón
		KP = 1 #Constante Proporcional
	    KI = 0.1 #Constante Integral
	    KD = 0.2 #Constante Derivativa
	    ZI = 5 #Zona activa de la Integral
	        
	    DD= DireccionDeseada(DATOS.lat, DATOS.long, waypoint)
	    DA= DATOS.curso #Direccion actual dado por el modulo gps
	    DeltaD= DD - DA 	#Con estos 3 renglones tomamos la diferencia entre el curso actual y el deseado

	    errorT = 0	#Variable para cuando se activa la zona integral
	    
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
	            
	        UltimoError = DeltaD #Guardo el último error
	        Proporcional = DeltaD * KP
	        Integral = errorT * KI
	        Derivativa = (DeltaD - UltimoError) * KD

	        #Obtengo el valor del ángulo para el timón
	        angulo = Proporcional + Integral + Derivativa

	        if abs(angulo) >= 30 and DeltaD > 0: #Caso: DeltaD positivo
	            #Si el ángulo es mayor que el máximo de giro del timón giro 30°
	            angulo = 30

	        if abs(angulo) >= 30 and DeltaD < 0: #Caso: DeltaD negativo
	            #Si el ángulo es mayor que el máximo de giro del timón giro 30°
	            angulo = -30
	        
	        if angulo < 0:	#Si el giro es negativo
	        	while DATOS.timon != angulo:	#Giro hasta que el sensor del timón detecte que se lelgo al valor deseado
	        		timon.girarH()

	        if angulo > 0:	#Si el giro es positivo
	        	while DATOS.timon != angulo:	#Giro hasta que el sensor del timón detecte que se lelgo al valor deseado
	        		timon.girarAH()

	        return angulo
	#------------------------------------------------------------------------------------------------------------------

	#--------------------------------------------Inicio el piloto automático-------------------------------------------
	#Creo objetos para los motores
	timon= mt.PaP(4, 17, 27, 22)
	Cangilon= mt.Cangilon(6, 13, 100)			#Con un 1 en el pin de selección giramos horario, con un 0 antihorario.
	motorDirec= mt.Propulsion(18, 12, 100)		#Con el 12 giro horario y con el 18 antihorario.

	#Comienzo a girar los motores de propulsión y de la cinta trtansportadora
	Cangilon.girarD()
	motorDirec.girarD()

	#En esta array se guardan los waypoints a recorrer 
	#Cada waypoint se guarda en una fila distinta
	waypoints= np.array(([lat1, lng1], [lat2, lng2], ..., [latn, lngn]))

	#Se recorren todos los watpoints uno por uno
	for i in range (0, len(waypoints)):
		#La idea es que corrija el rumbo a lo largo del trayecto cada xx tiempo
		while(LlegadaAlWP(waypoints[i]) != 1):
			if DATOS.curso != None:		#Solo corrijo el rumbo si hay un curso detectado
				MEDICION DE US 		#Mido con los sensores UltraSónicos
				if CONDICIÓN DE US:		#Si detecto algo utilizo la Red Neuronal para esquivar el obstáculo
					redNeuronal()
				controlPID()

			MEDICION DE US
			if CONDICION DE US:
				redNeuronal()

	#Detengo los motores de propulsión y la cinta transportadora
	Cangilon.detener()
	motorDirec.detener()

	DATOS.fin = 1	#Indico que finalizó el recorrido
#-------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------Módulos RF-------------------------------------------------------------------
def módulosRF():
	#-----------------------------Funciones de enviar y recibir-----------------------------
	def enviar(dato):
	    datoStr = str(dato) #Convierto el dato en string
	    datoSend = list(datoStr) #Lo separo en letras
	    radio.Write(datoSend) #Lo envio

	def recibir():
	    #Guardo el mensjae en una variable
	    msjRecibido = []
	    radio.read(msjRecibido, radio.getDynamicPayloadSize())

	    #Decodifico el mensaje
	    mensaje = ""
	    for n in msjRecibido
	        if (n >= 32 and n <= 126)
	            mensaje += chr(n)
	    return mensaje
	#----------------------------------------------------------------------------------------

	#-------------------------------Configuración del NRF24l01-------------------------------
	#Estas son las direcciones que les asignamos a las direcciones de lectura y escritura
	pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

	radio = NRF24(GPIO, spidev.SpiDev())	#Creamos el objeto de la radio

    radio.begin(0, 7)	#Iniciamos la radio

    radio.setRetries(15,15)		#Cantidad de intentos
    radio.setPayloadSize(32)	#Tamaño máximo de los mensajes
    radio.setChannel(0x60)		#Canal de comunicación
    radio.setDataRate(NRF24.BR_2MBPS)	#Velocidad de transferencia
    radio.setPALevel(NRF24.PA_MAX)		#Consumo del módulo, esto define el alcance

    #Estas funcioines sirven para que el módulo sepa si se recibió el mensaje que envió
    radio.setAutoAck(True)
    radio.enableDynamicPayloads()
    radio.enableAckPayload()

    #Abro las direcciones
    radio.openReadingPipe(1, pipes[1])
    radio.openWritingPipe(pipes[0])

    radio.startListening()
    #-----------------------------------------------------------------------------------------

    #Se queda esperando un mensaje
    while not radio.available(0):
        time.sleep(1/100)

    #Cuando detecta un mensaje, lo guardo en una variable
    comando = recibir()

	#-----------------------------------Comando: ZARPAR---------------------------------------
	if comando == MSJZARPAR:	#Cuando recibo la orden de zarapar tengo que inicar los otros hilos
		TGPS = threading.Thread(name="GPS", target=GPS)		#Creo el hilo del GPS
		TPA = threading.Thread(name="PA", target=pilotoAutomatico)	#Creo el hilo del piloto automático
		TCAD = threading.Thread(name="CAD", target=conversor)	#Creo el hilo del Conversor A/D
		#Inicio el GPS
		TGPS.start()
		
		while True:		#Espero a que el GPS reciba datos
    		if(DATOS.escan==1):
        		break
		#Inicio el Piloto Automático y el conversor A/D
		TCAD.start()
		TPA.start()

		#Envió información a la interfaz de usuario
		while True:
			enviarRF(DATOS.lat)
			enviarRF(DATOS.lon)
			enviarRF(DATOS.curso)
			enviarRF(DATOS.motProp)
			enviarRF(DATOS.motCang)
			enviarRF(DATOS.bateria)
			#Si el barco finalizó el recorrido, dejo de enviar datos
			if DATOS.fin == 1:
				break
	#---------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------Inicio el programa--------------------------------------------------------------
#Creo el hilo del módulo RF
TRF = threading.Thread(name="RF", target=comRF)

#Inicio un bucle para que cuando el programa finalice, siga esperando a recibir orden de salir de vuelta.
while True:
	TRF.start()