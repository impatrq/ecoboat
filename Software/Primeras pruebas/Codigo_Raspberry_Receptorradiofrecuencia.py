from __future__ import print_function
from flask import Flask, render_template
import time
from RF24 import *
import RPi.GPIO as GPIO
irq_gpio_pin = None
radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_8MHZ)
def try_read_data(channel=0):
    if radio.available():
        while radio.available():
            len = radio.getDynamicPayloadSize()
            receive_payload = radio.read(len)
            receive_payload.decode('utf-8')
            print(receive_payload)
            radio.stopListening()
            radio.write(receive_payload)
            
            radio.startListening()
pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]
radio.begin()
radio.setAutoAck(False)
radio.enableDynamicPayloads()
radio.setRetries(5,15)
radio.printDetails()
inp_role = '0'
if inp_role == '0':
    print('esperando transmision')
    if irq_gpio_pin is not None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(irq_gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(irq_gpio_pin, GPIO.FALLING, callback=try_read_data)
    radio.openWritingPipe(pipes[1])
    radio.openReadingPipe(1,pipes[0])
    radio.startListening()

while 1: 
        if irq_gpio_pin is None:
            try_read_data()
        else:
            time.sleep(1000)