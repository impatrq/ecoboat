import threading
import time

variable1=0

def prueba1(dato):
	time.sleep(1)
	variable1=dato
	return 0

def prueba2():
	print(variable1)
	time.sleep(1.5)
	print(variable1)
	return 0

t1 = threading.Thread(name="hilo1", target=prueba1, args=(10, ))
t2 = threading.Thread(name="hilo2", target=prueba2)

t1.start()
t2.start()


t1.join()
t2.join()