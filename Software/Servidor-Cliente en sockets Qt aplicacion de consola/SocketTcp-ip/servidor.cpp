#include "servidor.h"

Servidor::Servidor(QObject *parent) :
    QTcpServer(parent)
{

}

void Servidor::StartServer(){
if(!this->listen(QHostAddress::Any,1234)){

    qDebug() << "Esperando Conexiones";
}
else {
    qDebug() << "Cliente conectado, esperando mensajes:  ";
}
}

void Servidor::incomingConnection(int socketdesc){
    qDebug() << socketdesc << "Conectando, espere...";
    Cliente *thread = new Cliente (socketdesc,this);
    connect (thread,SIGNAL(finished()), thread, SLOT(deleteLater()));
}
