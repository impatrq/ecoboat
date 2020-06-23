import socket
import threading
import time

#Defino el puerto y la dirección IP del servidor.
PUERTO = 29999
SERVIDOR = "127.0.0.1"
ADDR = (SERVIDOR, PUERTO)
FORMATO = 'utf-8' #Formato de bytes que se va a usar para transmitir
HEADER = 64 #Cantidad de bytes que se va a usar para mandar la longitud del dato
MSJDESCONEXION = "!DESCONECTAR"
MSJZARPAR = "!ZARPAR"
MSJANALISIS = "!ANALISIS_RAPIDO"
MSJESTACIONADO = "!ESTACIONADO"

#Defino el socket, indicando el tipo y el modo de conexión
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def cliente(conn, addr):
	print(f"Nueva conexión: {addr}")

	lat = 0
	lon = 0
	dirr = 0
	prop = 0
	cang = 0
	bat = 0 
	PS = 1
	motDir = 1
	estacionamiento = 1

	def enviar(msj):
		#Codifico el mensaje y envío su longitud
		mensaje = msj.encode(FORMATO)
		longMsj = len(mensaje)
		enviarLong = str(longMsj).encode(FORMATO)
		enviarLong += b' ' * (HEADER - len(enviarLong))
		conn.send(enviarLong)
		conn.send(mensaje)
		print (f"{msj} enviado")

	def recivir():
		#Recivo la longitud y el mensaje y decodifico ambos
		longitud = conn.recv(HEADER).decode(FORMATO)
		if longitud:
			longitud = int(longitud)
			msjRecivido = conn.recv(longitud).decode(FORMATO)
		print(f"{addr} Pidió: {msjRecivido}")
		return msjRecivido

	funcion = recivir()
	if funcion == MSJZARPAR:
		while True:
			lat += lat + 1
			lon += lon + 1
			dirr += dirr + 1
			enviar(str(lat))
			enviar(str(lon))
			enviar(str(dirr))
			prop += prop + 1
			enviar(str(prop))
			cang += cang + 1
			enviar(str(cang))
			bat += bat + 1
			enviar(str(bat))
			if PS == 0:
				enviar("EL PANEL SOLAR NO ESTÁ CARGANDO")
			else:
				enviar("El panel solar está cargando")
			if motDir == 0:
				enviar("EL MOTOR DE DIRECCIÓN TIENE UNA FALLA")
			else:
				enviar("El motor de dirección está funcionando correctamente")
			if estacionamiento == 1:
				enviar(MSJESTACIONADO)
				break
			else:
				enviar("El barco sigue en curso")
			time.sleep(7)

	if funcion == MSJANALISIS:
		enviar(str(bat))
		if PS == 1:
			enviar("EL PANEL SOLAR ESTÁ CARGANDO")
		if PS == 0:
			enviar("EL PANEL SOLAR NO ESTÁ CARGANDO")

def iniciar():
	server.listen()
	print (f"Escuchando en {SERVIDOR}")
	while True:
		#Acepto el cliente
		conn, addr = server.accept()
		#Inicio en paralelo la función de cliente
		thread = threading.Thread(target=cliente, args=(conn,addr))
		thread.start()
		print(f"[Conexiones Activas]: {threading.activeCount() - 1}")

print("Iniciando el servidor...")
iniciar()