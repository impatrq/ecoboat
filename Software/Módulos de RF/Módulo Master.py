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
        return comando

def recivirDatos():
        radio.startListening()
        while not radio.available(0):
                time.sleep(1/100)
        #Recive todos los datos y los guarda en un array.
        return datos

while True:
	comando = comandoZarpar()
	mensaje = list (comando)
	radio.Write(mensaje)
	print ("Se mandó el comando de zarpar.")

        #Chequea si el slave recivió el comando.
	if radio.isAckPayloadAvailable ():
                returnedPL = []
                radio.read(returnedPL, radio.getDynamicPayloadSize())
                print (returnedPL)
                #Si se recive el ackPL se empiezan a recivir los datos
                while radio.available(0):
                        recivirDatos()
                radio.stopListening()
                
	else:
                print ("No se recivió el mensaje")
                time.sleep(1)
