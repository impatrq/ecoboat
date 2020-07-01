#include<SPI.h>
#include<RF24.h>

//ce, csn pins
RF24 radio(9, 10);

void setup(void) {
//-------------------------------------------------------------------------Configuración del Módulo Master------------------------------------------------------------------------
  while (!Serial);
  Serial.begin(9600);

  radio.begin();
  radio.serPALevel(RF24_PA_MAX);
  radio.setChannell(0x76);
  radio.openWritingPipe(0xF0F0F0E1LL);
  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openReadingPipe(1, pipe);

  radio.enableDynamicPayloads();
  radio.powerUp();

  char MSJZARPAR = "!ZARPAR";
  char MSJANALISIS = "!ANALISIS";
}
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//---------------------------------------------------------------------Funciones de enviar y recivir mensajes-------------------------------------------------------------------
int enviarRF(msj){
  //Convierto el mensaje en un string
  String msjStr(msj);
  const char texto[] = msjStr;
  //Lo envío
  radio.write(texto, sizeof(texto));
  return msj;
}

int recivirRF(){
  char msjRecivido[32] = {0};
  //Leo el mensaje y lo guardo en una variable
  radio.read(msjRecivido, sizeof(msjRecivido));
  //Lo decodifico a un string
  String mensaje(msjRecivido);
  return mensaje;
}
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void loop() {
  comando = enviarRF(MSJZARPAR);

  radio.StartListening();

  //---------------------Comando Zarpar------------------------------
  if comando == MSJZARPAR{
    int a = 0;
    while a == 0{
      mensaje = recivirRF();
      Serial.println(mensaje);
      if mensaje == "20"{
        a = 1;
      }
    }
  }
  //-----------------------------------------------------------------

  //--------------------Comando análisis-----------------------------
  else if comando == MSJANALISIS{
    mensaje = recivirRF();
    Serial.println(mensaje);
  }
  //-----------------------------------------------------------------
}
