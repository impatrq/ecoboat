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

		radio.openWritingPipe(pipes[1])

		radio.printDetails()

	#envia un mensaje
	def enviar(self, mensaje)
	    msj = list(mensaje)
	    radio.Write(msj)
	    print ("Se mandó el mensaje")

	    if radio.isAckPayloadAvailable ():
	        returnedPL = []
	        radio.read(returnedPL, radio.getDynamicPayloadSize())
	        print (returnedPL)
	    else:
	        print ("No se recivió el mensaje")
	    time.sleep(1)

	#configuracion del modulo por si no se quiere la predeterminada
	#se le pueden agregar mas cosas
	def config(self, canal, tamaño):
		radio.setPayloadSize(tamaño)
		radio.setChannel(canal)