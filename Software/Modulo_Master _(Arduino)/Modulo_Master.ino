#include<SPI.h>
#include<RF24.h>

//ce, csn pins
RF24 radio(9, 10);

void setup(void) {
//-------------------------------------------------------------------------Configuración del Módulo Master------------------------------------------------------------------------
  radio.begin();  
  radio.setPALevel(RF24_PA_MAX);  //Definimos la potencia del módulo
  radio.setChannel(0x76); //Canal
  radio.openWritingPipe(0xF0F0F0E1LL);  //Direcciones de escritura y lectura
  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openReadingPipe(1, pipe);

  radio.enableDynamicPayloads();
  radio.powerUp();  //Iniciamos la radio
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
  char comando;
  comando = enviarRF(MSJZARPAR);
  radio.write(comando, sizeof(comando));  //Envio el comando

  radio.startListening();   //Empiezo a escuchar

  //---------------------Comando Zarpar------------------------------
  if (comando == MSJZARPAR){
    if (radio.available()){
      while (true){
        String mensaje;
        latitud = recibirRF();
        longitud = recibirRF();
        curso = recibirRF();
        consProp = recibirRF();
        consCang = recibirRF();
        bateria = recibirRF();
        timon = recibirRF();
        }
        delay(500);
      }
   }
  }
  //-----------------------------------------------------------------
}
