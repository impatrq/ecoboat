#include "cliente.h"

Cliente::Cliente(int ID, QObject *parent) :
    QObject(parent)
{
     this->socketdesc = ID;
}
void Cliente::ejecutar(){

  qDebug() << socketdesc << "Iniciando Conexiones";
  socket = new QTcpSocket ();
  if (!socket -> setSocketDescriptor(this -> socketdesc)){

      emit error (socket ->error());
      return;
  }
   connect(socket, SIGNAL(readyRead()),this,SLOT(readyRead()),Qt::DirectConnection);
   connect(socket, SIGNAL(disconnected()),this,SLOT(disconnected()),Qt::DirectConnection);

   qDebug () <<  socketdesc << "Cliente Conectado";
   return;

}

void Cliente::readyRead(){

    QByteArray Data = socket->readAll();
    qDebug () <<  socketdesc << " Informacion :" << Data;
    socket -> write(Data);

}


void Cliente::disconnected(){
qDebug () <<  socketdesc << "Cliente desconectado";
socket->deleteLater();
exit (0);
}
