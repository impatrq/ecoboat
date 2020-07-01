import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

MSJZARPAR = "!ZARPAR"
MSJANALISIS = "!ANALISIS"

GPIO.setmode(GPIO.BCM)

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
        radio.setPALevel(NRF24.PA_MAX)

        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()

        radio.openReadingPipe(1, pipes[1])
        radio.openWritingPipe(pipes[0])

        radio.printDetails()

        radio.startListening()

def enviar(dato):
    datoStr = str(dato) #Convierto el dato en string
    datoSend = list(datoStr) #Lo separo en letras
    radio.Write(datoSend) #Lo envio

def recivir():
    #Empiezo a escuchar
    radio.startListening()

    #Guardo el mensjae en una variable
    msjRecivido = []
    radio.read(msjRecibido, radio.getDynamicPayloadSize())
    print ("Recivido: {}".format(msjRecivido))

    #Decodifico el mensaje
    print ("Traduciendo el mensaje...")
    mensaje = ""
    for n in msjRecibido
        if (n >= 32 and n <= 126)
            mensaje += chr(n)
    return mensaje

while True:
    #se queda esperando un mensaje
    while not radio.available(0):
        time.sleep(1/100)

    #Recivo el mensaje
    mensajeRcv = recivir()
    print(mensajeRcv)

    if mensajeRcv == MSJZARPAR:
        #Dejo de escuchar
        radio.stopListening()
        a = 0
        while a < 20:
            enviar(a)
            a++
            time.sleep(2)

    if mensajeRcv == MSJANALISIS:
        #Dejo de escuchar
        radio.stopListening()
        a = 0
        enviar(a)