import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

MSJZARPAR = "!ZARPAR"
MSJANALISIS = "!ANALISIS"

GPIO.setmode(GPIO.BCM)

#------------------------------------------------------------Configuración del Módulo-----------------------------------------------------------------------
class slave():
    pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

    radio = NRF24(GPIO, spidev.SpiDev())

    radio.begin(0, 7)

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
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------Funciones de enviar y recibir-----------------------------------------------------------------
def enviar(dato):
    datoStr = str(dato) #Convierto el dato en string
    datoSend = list(datoStr) #Lo separo en letras
    radio.Write(datoSend) #Lo envio

def recibir():
    #Guardo el mensjae en una variable
    msjRecibido = []
    radio.read(msjRecibido, radio.getDynamicPayloadSize())
    print ("Recivido: {}".format(msjRecibido))

    #Decodifico el mensaje
    print ("Traduciendo el mensaje...")
    mensaje = ""
    for n in msjRecibido
        if (n >= 32 and n <= 126)
            mensaje += chr(n)
    return mensaje
#---------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    #Empiezo a escuchar
    radio.startListening()
    
    #se queda esperando un mensaje
    while not radio.available(0):
        time.sleep(1/100)

    #Recivo el mensaje
    mensajeRcb = recibir()
    print(mensajeRcv)

    if mensajeRcb == MSJZARPAR:
        #Dejo de escuchar
        radio.stopListening()
        a = 0
        while a <= 20:
            b = str(a)
            enviar(b)
            a++
            time.sleep(1)

    if mensajeRcb == MSJANALISIS:
        #Dejo de escuchar
        radio.stopListening()
        a = 0
        enviar(a)