#include<SPI.h>
#include<RF24.h>

//ce, csn pins
RF24 radio(9, 10);

void setup(void) {
//-------------------------------------------------------------------------Configuración del Módulo Master------------------------------------------------------------------------
  while (!Serial);
  Serial.begin(9600);

  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0E1LL);
  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openReadingPipe(1, pipe);

  radio.enableDynamicPayloads();
  radio.powerUp();
}

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//---------------------------------------------------------------------Funciones de enviar y recibir mensajes-------------------------------------------------------------------
int enviarRF(int msj){
  //Convierto el mensaje en un string
  String msjStr(msj);
  const char texto[] = "msjStr";
  //Lo envío
  return msj;
}

String recibirRF(){
  char msjRecibido[32] = {0};
  //Leo el mensaje y lo guardo en una variable
  radio.read(msjRecibido, sizeof(msjRecibido));
  //Lo decodifico a un string
  String mensaje(msjRecibido);
  return mensaje;
}
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void loop(void) {
  char MSJZARPAR = "!ZARPAR";
  char MSJANALISIS = "!ANALISIS";
  char comando;
  comando = enviarRF(MSJZARPAR);
  radio.write(comando, sizeof(comando));
  Serial.println("Se está enviando el mensaje");

  radio.startListening();

  //---------------------Comando Zarpar------------------------------
  if (comando == MSJZARPAR){
    Serial.println("El usuario eligió la opción zarpar");
    if (radio.available()){
      while (true){
        String mensaje;
        mensaje = recibirRF();
        Serial.println(mensaje);
        if (mensaje == "20"){
          return 0;
        }
        delay(500);
      }
   }
  return 0;
  }
  //-----------------------------------------------------------------

  //--------------------Comando análisis-----------------------------
  else if (comando == MSJANALISIS){
    Serial.println("El usuario eligió la opción análisis rápido");
    if (radio.available()){
      String mensaje;
      mensaje = recibirRF();
      Serial.println(mensaje);
      return 0;
    }
  }
  //-----------------------------------------------------------------
}
