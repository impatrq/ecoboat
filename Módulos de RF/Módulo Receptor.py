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

radio2.openReadingPipe(1, pipes[1])

radio2.printDetails()

radio2.startListening()

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
