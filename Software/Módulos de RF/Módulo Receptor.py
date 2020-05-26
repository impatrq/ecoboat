import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

class receptor():

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

        radio.printDetails()

        radio.startListening()

        #se queda esperando un mensaje
        while True:
            while not radio2.available(0):
                time.sleep(1/100)

            msjRecibido = []
            radio2.read(msjRecibido, radio2.getDynamicPayloadSize())
            print ("Recivido: {}".format(msjRecivido))

            print ("Traduciendo los mensajes...")
            mensaje = ""
            for n in msjRecibido
                if (n >= 32 and n <= 126)
                    mensaje += chr(n)
            print (mensaje)

            radio.witeAckPayload(1, ackPL, len(ackPL))
            print("Se envió la confirmación de mensaje de {}".format(ackPL))
