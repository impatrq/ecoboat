import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from lib_nrf24 import NRF24
import time
import spidev

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

radio2 = NRF24(GPIO, spidev.SpiDev())
radio2.begin(0, 17)

radio2.setRetries(15,15)

radio2.setPayloadSize(32)
radio2.setChannel(0x60)
radio2.setDataRate(NRF24.BR_2MBPS)
radio2.setPALevel(NRF24.PA_MIN)

radio2.setAutoAck(True)
radio2.enableDynamicPayloads()
radio2.enableAckPayload()

radio2.openWritingPipe(pipes[1])

radio2.printDetails()

while True:
    mensaje = list("dato")
    radio.Write(mensaje)
    print ("Se mandó el mensaje")

    if radio.isAckPayloadAvailable ():
        returnedPL = []
        radio.read(returnedPL, radio.getDynamicPayloadSize())
        print (returnedPL)
    else:
        print ("No se recivió el mensaje")
