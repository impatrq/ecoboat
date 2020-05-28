import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import EstructuraPilotoAutomatico
import gps

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
        radio.setPALevel(NRF24.PA_MIN)

        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()

        radio.openReadingPipe(1, pipes[1])
        radio.openWritingPipe(pipes[0])

        radio.printDetails()

        radio.startListening()

def direccion():
    #Tomo la direccion del barco
    Gps.lectura()
    direccion = Gps.cur
    return direccion

def latitud():
    #Tomo la latitud del barco
    Gps.lectura()
    latitud = Gps.lat
    return latitud

def longitud():
    #Tomo la latitud del barco
    Gps.lectura()
    longitud = Gps.lng
    return longitud

def bateria():
    #Detecto el porcentaje de bateria
    return bateria

def consPropulsion():
    #Mido el consumo del motor de propulsión.
    return consPropulsion

def consCangilon():
    #Mido el consumo del motor del cangilón.
    return consCangilon

def anguloMotDir():
    #Mido el ángulo del motor de dirección
    return anguloMotDir


def enviarDatos(direccion, latitud, longitud, bateria, consPropulsion, consCangilon, anguloMotDir):
    #Creo un array con todos los datos y lo envío.
    time.sleep(0.25)
    direccionSend = list(direccion)
    radio.Write(direccionSend)
    latitudSend = list(latitud)
    radio.Write(latitudSend)
    longitudSend = list(longitud)
    radio.Write(longitudSend)

def Llegada():
    #Detecto si el barco volvió a la estación de carga.
    return estacionado

Gps= gps.Gps()

while True:
    
    #Avisa que resivió el comando.
    ackPL = [1]
    radio.writeAckPayload(1, ackPL, len (ackPL))
    
    #se queda esperando un mensaje
    while not radio.available(0):
        time.sleep(1/100)

    #Recive un comando del Master.
    msjRecibido = []
    radio.read(msjRecibido, radio.getDynamicPayloadSize())
    print ("Recivido: {}".format(msjRecivido))

    print ("Traduciendo los mensajes...")
    mensaje = ""
    for n in msjRecibido
        if (n >= 32 and n <= 126)
            mensaje += chr(n)
    print (mensaje)

    #Cuando el Master se lo pide, obtiene todos los datos y los envía.
    if mensaje == "Si":
    	radio.stopListening()
        while Llegada == 0: #Una vez que el barco estaciona, sale del while.
            direccion = direccion()
            latitud = latitud()
            longitud = longitud ()
            bateria = bateria()
            consPropulsion = consPropulsion()
            consCangilon = consCangilon()
            anguloMotDir = anguloMotDir()
            enviarDatos(mensaje)
            time.sleep(0.5)

        radio.startListening()
        radio.witeAckPayload(1, ackPL, len(ackPL))
        print("Se envió la confirmación de mensaje de {}".format(ackPL))
