import socket
import threading

#Defino el puerto y la dirección IP del servidor.
PUERTO = 5050
SERVIDOR = socket.gethostbyname(socket.gethostname())
ADDR = (SERVIDOR, PUERTO)
FORMATO = 'utf-8' #Formato de bytes que se va a usar para transmitir
HEADER = 64 #Cantidad de bytes que se va a usar para mandar la longitud del dato
MSJDESCONEXION = "!DESCONECTAR"

#Defino el socket, indicando el tipo y el modo de conexión
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def cliente(conn, addr):
	print(f"Nueva conexión: {addr}")

	while True:
		longitud = conn.recv(HEADER).decode(FORMATO)
		if longitud:
			longitud = int(longitud)
			mensaje = conn.recv(longitud).decode(FORMATO)
			if mensaje == MSJDESCONEXION:
				print(f"{addr} {mensaje}")
				break
			print(f"{addr} {mensaje}")

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