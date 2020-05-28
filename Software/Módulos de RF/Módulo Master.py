import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

class transmisor():

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

def comandoZarpar():
    #Envía el comando para que el barco zarpe.
    if zarpar== 1:
    	return Si 
    else:
    	return No

def recivirDireccion():
        rcvDireccion = []
    radio.read(rcvDireccion, radio.getDynamicPayloadSize())
    Direccion = ""
    for n in rcvDireccion:
        if (n >= 32 and n <= 126)
            Direccion += chr(n)
    return Direccion

def recivirLatitud():
        rcvLatitud = []
    radio.read(rcvLatitud, radio.getDynamicPayloadSize())
    Latitud = ""
    for n in rcvLatitud:
        if (n >= 32 and n <= 126)
            Latitud += chr(n)
    return Latitud

def recivirLongitud():
        rcvLongitud = []
    radio.read(rcvLongitud, radio.getDynamicPayloadSize())
    Longitud = ""
    for n in rcvLongitud:
        if (n >= 32 and n <= 126)
            Longitud += chr(n)
    return Longitud

def recivirBateria():
        rcvBateria = []
    radio.read(rcvBateria, radio.getDynamicPayloadSize())
    Bateria = ""
    for n in rcvBateria:
        if (n >= 32 and n <= 126)
            Bateria += chr(n)
    return Bateria

def recivirConsPropulsion():
        rcvConsPropulsion = []
    radio.read(rcvConsPropulsion, radio.getDynamicPayloadSize())
    consPropulsion = ""
    for n in rcvConsPropulsion:
        if (n >= 32 and n <= 126)
            consPropulsion += chr(n)
    return consPropulsion

def recivirConsCangilon():
        rcvConsCangilon = []
    radio.read(rcvConsCangilon, radio.getDynamicPayloadSize())
    consCangilon = ""
    for n in rcvConsCangilon:
        if (n >= 32 and n <= 126)
            consCangilon += chr(n)
    return consCangilon

def recivirAnguloMotDir():
        rcvAnguloMotDir = []
    radio.read(rcvAnguloMotDir, radio.getDynamicPayloadSize())
    anguloMotDir = ""
    for n in rcvAnguloMotDir:
        if (n >= 32 and n <= 126)
            anguloMotDir += chr(n)
    return anguloMotDir

while True:
        comando = comandoZarpar()
	mensaje = list (comando)
	radio.Write(mensaje)
	print ("Se mandó el comando de zarpar.")

    #Chequea si el slave recivió el comando.
	if radio.isAckPayloadAvailable():
                returnedPL = []
                radio.read(returnedPL, radio.getDynamicPayloadSize())
                print (returnedPL)
                #Si se recive el ackPL se empiezan a recivir los datos
                radio.startListening()
                while radio.available(0):
                    recivirDireccion()
                    recivirLatitud()
                    recivirLongitud()
                    recivirBateria()
                    recivirConsPropulsion()
                    recivirConsCangilon()
                    recivirAnguloMotDir()
                radio.stopListening()
                
        else:
                print ("No se recivió el mensaje")
                time.sleep(1)
