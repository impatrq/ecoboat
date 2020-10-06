#ifndef SERVIDOR_H
#define SERVIDOR_H

#include <QTcpServer>
#include <QDebug>
#include "cliente.h"
class Servidor : public QTcpServer
{
    Q_OBJECT
public:
    explicit Servidor(QObject *parent = nullptr);
    void StartServer();

signals:


protected:
    void incomingConnection(int socketdesc);
};

#endif // SERVIDOR_H
