#ifndef CLIENTE_H
#define CLIENTE_H

#include <QObject>
#include <QTcpSocket>
#include <QDebug>


class Cliente : public QObject
{
    Q_OBJECT
public:
    explicit Cliente(int ID, QObject *parent = nullptr);
    void ejecutar();
signals:
   void error(QTcpSocket::SocketError socketerror);

public slots:
private:
     QTcpSocket *socket;
     int socketdesc;

public slots:
  void readyRead();
  void disconnected();

};

#endif // CLIENTE_H
