import RPi.GPIO as GPIO
import time
import threading 
import pynmea2 as nmea
import numpy as np 
import motores as mt 
import math
from lib_nrf24 import NRF24
import spidev

#estado del codigo= naranja

#//////////////// defino la lista que va a guardar las variables/////////////

datos= [0,0,0,0]
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
		DD= DireccionDeseada(datos[0], datos[1], waypoint)
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
				DD= DireccionDeseada(datos[0], datos[1], waypoint)
				DA= datos[2]
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
		dis= distancia(datos[0], datos[1], destino)

		if(abs(dis) <= 5):
			return 0
		else:
			return 1

	timon= mt.PaP(1, 2, 3, 4)
	Cangilon= mt.Cangilon(1,2,50)
	motorDirec= mt.Propulsion(1,2,50)
	#meto primera
	Cangilon.girarD()
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

	Cangilon.detener()
	motorDirec.detener()
	
#//////////////// funciones de RF //////////////////////

def comRF():
	class slave():

	    def __init__(self, pin1, pin2):
	        self.pin1=pin1
	        self.pin2=pin2

	        #configuracion del modulo

	        pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

	        radio = NRF24(GPIO, spidev.SpiDev())

	        radio.begin(self.pin1, self.pin2)

	        radio.setRetries(15,15)
	        radio.setPayloadSize(32)
	        radio.setChannel(0x60)
	        radio.setDataRate(NRF24.BR_2MBPS)
	        radio.setPALevel(NRF24.PA_MIN)

	        radio.setAutoAck(True)
	        radio.enableDynamicPayloads()
	        radio.enableAckPayload()

	        radio.openReadingPipe(1, pipes[1])
	        radio.openWritingPipe(pipes[0])

	        radio.printDetails()

	        radio.startListening()

    #--------------------------------------------Funciones de sensores---------------------------------------------------
    #Abro el SPI
    spi = spidev.SpiDev()
    spi.open(0, 0)

    #Defino un canal para cada sensor
    sCorriente1 = 0
    sCorriente2 = 1
    sBateria = 2
    sMotDir = 3

    def tomarDatos(canal):
    	#Primero tomamos los datos crudos del conversor A/D
    	datosCrudos = spi.xfer([1, (8 + canal) << 4, 0])
    	#Proceso esta información para tenerla en un numero de 0 a 1023
    	datosProcesados = ((datosCrudos[1]&3) << 8) + datosCrudos[2]
    	return datosProcesados

	def bateria(redondeoDecimal = 3):
	    porcentajeB = tomarDatos(sBateria)
	    voltaje = (porcentajeB * 5) / float(1023)
	    voltaje = round(voltaje, redondeoDecimal)
	    if pocentajeB < 808:
	    	porcentaje = 0
	    else:
	    	porcentaje = (porcentajeB * 100) / float(1023)
	    	porcentaje = round(porcentaje)
	    return porcentaje

	def consPropulsion(redondeoDecimal = 3):
	    consumoB = tomarDatos(sCorriente1) #Tomo el valor en bits
	    voltaje = (consumoB * 5) / float(1023) #Lo convierto a cuando voltaje representa
	    voltaje = round(voltaje, redondeoDecimal) #Redondeo a dos decimales
	    consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)
	    return consumo

	def consCangilon():
	    consumoB = tomarDatos(sCorriente2) #Tomo el valor en bits
	    voltaje = (consumoB * 5) / float(1023) #Lo convierto a cuando voltaje representa
	    voltaje = round(voltaje, redondeoDecimal) #Redondeo a dos decimales
	    consumo = (voltaje - 2.5) * 0.1 #Convierto el valor de voltaje en corriente (Relación: 100mV = 1A)
	    return consumo

	def anguloMotDir():
	    #Detecto si el motor de dirección falla
	    GPIO.setup(12, GPIO.IN)
	    return anguloMotDir

	def estacionamiento():
		#Detecto si el barco estaciona
		GPIO.setup(26, GPIO.IN)
		return estacionamiento

	def PS():
		#Detecto si el panel solar carga o no
		GPIO.setup(6, GPIO.IN)
		return PS
	#--------------------------------------------------------------------------------------------------------------------------

	#Función de recibir mensjaes
	def recibirRF():
	    rcvMsj = []
	    radio.read(rcvMsj, radio.getDynamicPayloadSize())
	    msj = ""
	    for n in rcvMsj:
	        if (n >= 32 and n <= 126)
	            msj += chr(n)
	    return msj

	#Función de enviar datos
	def enviarRF(msj):
		mensaje = list(msj)
		radio.Write(mensaje)

	#Recibo el comando de zarpar
	comando = recibirRF()
	if comando == "ZARPAR":
		TGPS = threading.Thread(name="GPS", target=GPS)
		TPA = threading.Thread(name="PA", target=pilotoAutomatico)
		TGPS.start()
		
		while True:
    			if(datos[3]==1):
        			break
	
		TPA.start()
		while True:
			lat = datos[0]
			lon = datos[1]
			dirr = datos[2]
			enviarRF(lat)
			enviarRF(lon)
			enviarRF(dirr)
			prop = consPropulsion()
			enviarRF(prop)
			cang = consCangilon()
			enviarRF(cang)
			bat = bateria()
			enviarRF(bat)
			PS = PS()
			enviarRF(PS)
			estacionamiento = estacionamiento()
			#Si el barco estaciona, salgo del loop
			if estacionamiento == 1:
				enviarRF(estacionamiento)
				break
			if estacionamiento == 0:
				enviarRF(estacionamiento)


#//////////////// funciones de GPS //////////////////////

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

                datos[3]==1
            return 0
        
	def lectura():
	    port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout=pynmea2.NMEAStreamReader()
            data=ser.readline()

            if data[0:6] == "$GPRMC":
                pos=pynmea2.parse(newdata)
		datos[0]=pos.latitude
		datos[1]=pos.longitude
		datos[2]=pos.direction

	    time.sleep(0.05)
	    return 0

        disponible()

        if (datos[3]==1):
            while True:
                lectura()
                time.sleep(1)


#//////////////// programa /////////////////////////

#////////////// inicio los hilos ////////////////////
while True:
	cmRF()
