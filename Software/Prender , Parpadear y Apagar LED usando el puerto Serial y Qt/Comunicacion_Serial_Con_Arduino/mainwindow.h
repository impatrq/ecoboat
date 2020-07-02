#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtSerialPort>
#include <QSerialPortInfo> // incluye la informacion de los puertos seriales.
#include <QDebug>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_Encendido_clicked();

    void on_pushButton_3_clicked();

    void on_Parpadear_clicked();

private:
    Ui::MainWindow *ui;
    QSerialPort *serial;
    QString numerodepuerto;
    quint16 vendorId;
    quint16 productId;
    bool arduino_available;
    void inicializacionarduino();
};
#endif // MAINWINDOW_H
