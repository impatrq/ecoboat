import threading
import time
import numpy as np

lista= [1,2]

def prueba1():
	lista[0]=2
	time.sleep(1)
	lista[0]=4
	return 0

def prueba2():
	time.sleep(0.5)
	print(lista[0])
	time.sleep(3)
	print(lista[0])
	return 0

t1 = threading.Thread(name="hilo1", target=prueba1)
t2 = threading.Thread(name="hilo2", target=prueba2)

t1.start()
t2.start()


t1.join()
t2.join()