import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import socket
import threading

GPIO.setmode(GPIO.BCM)

#------------------------------------------------------------------------Definición de parámetros--------------------------------------------------------------------------
class transceptor():

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

        radio.openReadingPipe(1, pipes[0])
		radio.openWritingPipe(pipes[1])

		radio.printDetails()

class servidor():
	#Defino todos los datos del servidor.
	PUERTO = 29999
	SERVIDOR = "127.0.0.1"
	ADDR = (SERVIDOR, PUERTO)
	FORMATO = 'utf-8' #Formato de bytes que se va a usar para transmitir
	HEADER = 64 #Cantidad de bytes que se va a usar para mandar la longitud del dato
	MSJZARPAR = "!ZARPAR" #Comando de zarpar
	MSJANALISIS = "!ANALISIS_RAPIDO" #Comando de análisis rápido
	MSJESTACIONADO = "EL BARCO ESTACIONÓ" #Comando de estacionamiento
	MSJPSCARGANDO = "El panel solar está cargando."
	MSJPSNOCARGANDO = "EL PANEL SOLAR NO ESTÁ CARGANDO."
	MSJMOTDIR = "El motor de dirección está funcionando correctamente."
	MSJMOTDIRFALLA = "EL MOTOR DE DIRECCIÓN TIENE UNA FALLA"

	#Defino el socket, indicando el tipo y el modo de conexión
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cliente(conn, addr):

	#Función de enviar mensajes de sockets
	def enviar(msj):
		#Codifico el mensaje y envío su longitud
		mensaje = msj.encode(FORMATO)
		longMsj = len(mensaje)
		enviarLong = str(longMsj).encode(FORMATO)
		enviarLong += b' ' * (HEADER - len(enviarLong))
		conn.send(enviarLong)
		conn.send(mensaje)
		print (f"{msj} enviado")

	#Función de recibir mensajes de sockets
	def recibir():
		#Recivo la longitud y el mensaje y decodifico ambos
		longitud = conn.recv(HEADER).decode(FORMATO)
		if longitud:
			longitud = int(longitud)
			msjRecivido = conn.recv(longitud).decode(FORMATO)
		print(f"{addr} Pidió: {msjRecivido}")
		return msjRecivido

	#Función recibir mensajes de Transceptor
	def recibirRF():
	    rcvMsj = []
	    radio.read(rcvMsj, radio.getDynamicPayloadSize())
	    msj = ""
	    for n in rcvMsj:
	        if (n >= 32 and n <= 126)
	            msj += chr(n)
	    return msj

#----------------------------------------------------Toma de datos con el Módulo RF y envio de datos con socket------------------------------------------------------------------
	#Recivo la función de zarpar o análisis rápido del cliente
	funcion = recibir()
	#----------------Análisis Rápido------------------------
	if funcion == MSJANALISIS:
		BAT = recibirRF()
		enviar(BAT)
		PS = recibirRF()
		if PS == 1:
			enviar(MSJPSCARGANDO)
		if PS == 0:
			enviar(MSJPSNOCARGANDO)
	#-------------------------------------------------------

	#----------------------------------------------------Zarpar-----------------------------------------------------
	if funcion == MSJZARPAR:
		while True:
			#Le digo al barco que zarpe
			comando = "ZARPAR"
			mensajeZarpar = list(comando)
			radio.Write(mensajeZarpar)
			print ("Se mandó el comando de zarpar.")
			#Chequea si el slave recivió el comando.
			if radio.isAckPayloadAvailable():
		        returnedPL = []
		        radio.read(returnedPL, radio.getDynamicPayloadSize())
		        print (returnedPL)
		        #Si se recive el ackPL se empiezan a recivir los datos
		        #-----------------------------------Recibo y envío datos---------------------------------------------
		        radio.startListening()
		        while True:
			        Lat = recibirRF()
			        Lon = recibirRF()
			        Dirr = recibirRF()
			        enviar(Lat)
			        enviar(Lon)
			        enviar(Dirr)
			        prop = recibirRF()
			        enviar(prop)
			        cang = recibirRF()
			        enviar(cang)
			        bat = recibirRF()
			        enviar(bat)
			        motDir = int(recibirRF())
			        if motDir == 1:
			        	enviar(MSJMOTDIR)
			        if motDir == 0:
			        	enviar(MSJMOTDIRFALLA)
			        PS = int(recibirRF())
			        if PS == 1:
			        	enviar(MSJPSCARGANDO)
			        if PS == 0:
			        	enviar(MSJPSNOCARGANDO)
			        estacionamiento = int(recibirRF())
			        if estacionamiento == 0:
			        	enviar("El barco sigue en curso")
			        if estacionamiento == 1:
			        	enviar("MSJESTACIONADO")
			        	break
		        radio.stopListening()
		        break
		        #----------------------------------------------------------------------------------------------------        
		    else:
		    print ("No se recivió el mensaje")
		    time.sleep(1)
	#----------------------------------------------------------------------------------------------------------------	    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def iniciar():
	server.listen()
	print (f"Escuchando en {SERVIDOR}")
	while True:
		#Acepto el cliente
		conn, addr = server.accept()
		#Inicio en paralelo la función de cliente
		thread = threading.Thread(target=cliente, args=(conn,addr))
		thread.start()
		print(f"[Conexiones Activas]: {threading.activeCount() - 1}")

#Inicio el programa
print("Iniciando el servidor...")
iniciar()