def tomaDeDatos():
 print ("Ingrese un Valor")
 valor = input()
 return valor

def tomaDeOperacion():
 return '+'

def calculoDeResultado(primero, segundo, operacion):
 return 2

def muestraDeResultado(resultado):
 return 1

print ("comienzo del programa")
primerValor = tomaDeDatos()
operacion = tomaDeOperacion()
segundoValor = tomaDeDatos()
resultado = calculoDeResultado(primerValor, segundoValor, operacion)
muestraDeResultado(resultado)
