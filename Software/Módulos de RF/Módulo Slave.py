import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

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

def coordenadas(gps):
    #Tomo la posición del barco
    return pos

def bateria():
    #Detecto el porcentaje de bateria
    return bateria

def conPropulsion():
    #Mido el consumo del motor de propulsión.
    return consPropulsion

def consCangilon():
    #Mido el consumo del motor del cangilón.
    return consCangilon

def anguloMotDir():
    #Mido el ángulo del motor de dirección
    return anguloMotDir

def PaqueteDeData():
    #repartir la informacion en paquetes para enviarlos
    return paquete

def enviarDatos(mensaje):
    #Creo un array con todos los datos y lo envío.
    radio.stopListening()
    time.sleep(0.25)
    datos = mensaje
    radio.Write(datos)
    radio.startListening()

def detectarSiEstaciono():
    #Detecto si el barco volvió a la estación de carga.
    return estacionado

while True:
    
    #Avisa que resivió el comando.
    ackPL = [1]
    radio.writeAckPayload(1, ackPL, len (ackPL))
    
    #se queda esperando un mensaje
    while not radio2.available(0):
        time.sleep(1/100)

    #Recive un comando del Master.
    msjRecibido = []
    radio2.read(msjRecibido, radio2.getDynamicPayloadSize())
    print ("Recivido: {}".format(msjRecivido))

    print ("Traduciendo los mensajes...")
    mensaje = ""
    for n in msjRecibido
        if (n >= 32 and n <= 126)
            mensaje += chr(n)
    print (mensaje)

    #Cuando el Master se lo pide. Obtiene todos los datos y los envía.
    if mensaje == "Zarpar":
        while estacionado == 0: #Una vez que el barco estaciona, sale del while.
            posicion = coordenadas()
            bateria = bateria()
            consPropulsion = consPropulsion()
            consCangilon = consCangilon()
            anguloMotDir = anguloMotDir()
            enviarDatos(mensaje)

            radio.witeAckPayload(1, ackPL, len(ackPL))
            print("Se envió la confirmación de mensaje de {}".format(ackPL))
