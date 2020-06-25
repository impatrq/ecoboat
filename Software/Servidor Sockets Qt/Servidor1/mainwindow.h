#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include <QMainWindow>
#include <QTcpServer>
#include <QTcpSocket>
#include <QHostAdress>
#include <QList>



#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void conexionueva ();
    void leer_cliente();

private slots:
    void cliente_on_clicked();
    void cliente2_on_cliked();

private:
    Ui::MainWindow *ui;

    QTcpServer *tcpservidor;
    QTcpSocket *tcpcliente[2];
};
#endif // MAINWINDOW_H
