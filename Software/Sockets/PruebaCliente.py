import socket

#Defino el puerto y la dirección IP del servidor.
PUERTO = 5050
SERVIDOR = "192.168.56.1"
ADDR = (SERVIDOR, PUERTO)
FORMATO = 'utf-8' #Formato de bytes que se va a usar para transmitir
HEADER = 64 #Cantidad de bytes que se va a usar para mandar la longitud del dato
MSJDESCONEXION = "!DESCONECTAR"

#Defino el cliente, indicando tipo y modo
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)

def enviar (msj):
	#Codifico el mensaje y envío su longitud
	mensaje = msj.encode(FORMATO)
	longMsj = len(mensaje)
	enviarLong = str(longMsj).encode(FORMATO)
	enviarLong += b' ' * (HEADER - len(enviarLong))
	cliente.send(enviarLong)
	cliente.send(mensaje)

enviar("Te saludo desde el cliente!")
enviar(MSJDESCONEXION)
