#ifndef LOCALSERVER_H
#define LOCALSERVER_H

#include <QTcpServer>
class QTcpSocket;
class LocalServer : public QTcpServer
{
    Q_OBJECT
public:
    explicit LocalServer(QObject *parent = nullptr);
    void envia (const QString &msj);
signals:
private:
    QTcpSocket *mSocket;
};

#endif // LOCALSERVER_H
