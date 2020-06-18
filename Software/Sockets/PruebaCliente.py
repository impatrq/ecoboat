import socket

#Defino el puerto y la dirección IP del servidor.
PUERTO = 7000
SERVIDOR = "192.168.56.1"
ADDR = (SERVIDOR, PUERTO)
FORMATO = 'utf-8' #Formato de bytes que se va a usar para transmitir
HEADER = 64 #Cantidad de bytes que se va a usar para mandar la longitud del dato
MSJDESCONEXION = "!DESCONECTAR"
MSJZARPAR = "!ZARPAR"
MSJANALISIS = "!ANALISIS_RAPIDO"
MSJESTACIONADO = "!ESTACIONADO"

#Defino el cliente, indicando tipo y modo
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)

def enviar(msj):
	#Codifico el mensaje y envío su longitud
	mensaje = msj.encode(FORMATO)
	longMsj = len(mensaje)
	enviarLong = str(longMsj).encode(FORMATO)
	enviarLong += b' ' * (HEADER - len(enviarLong))
	cliente.send(enviarLong)
	cliente.send(mensaje)
	print("Mensaje enviado")

def recivir():
	#Recivo la longitud y el mensaje y decodifico ambos
	longitud = cliente.recv(HEADER).decode(FORMATO)
	if longitud:
		longitud = int(longitud)
		msjRecivido = cliente.recv(longitud).decode(FORMATO)
	return msjRecivido

enviar(MSJZARPAR)
funcion = MSJZARPAR
if funcion == MSJZARPAR:
	while True:
		lat = recivir()
		lon = recivir()
		dirr = recivir()
		print(f"Latitud: {lat} Longitud: {lon} Dirección: {dirr}")
		prop = recivir()
		print(f"Consumo del motor de propulsión: {prop}")
		cang = recivir()
		print(f"Consumo dele motor del cangilón: {cang}")
		bat = recivir()
		print(f"Procentaje de batería: {bat}")
		PS = recivir()
		print(PS)
		motDir = recivir()
		print(motDir)
		estacionamiento = recivir()
		if estacionamiento == MSJESTACIONADO:
			print("El barco estacionó")
			break
		else:
			print(estacionamiento)

if funcion == MSJANALISIS:
	bat = recivir()
	print(f"El porcentaje de batería es: {bat}")
	PS = recivir()
	print(PS)