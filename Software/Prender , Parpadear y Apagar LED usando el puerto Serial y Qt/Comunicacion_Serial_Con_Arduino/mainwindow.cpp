#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this); //Constructor
    serial = new QSerialPort();
    arduino_available = false;

    foreach (const QSerialPortInfo &serial_Info , QSerialPortInfo::availablePorts()){
     qDebug ()<<"Puerto"<<serial_Info.portName();
     numerodepuerto = serial_Info.portName();
     qDebug ()<< "Vendor Id: "<<serial_Info.vendorIdentifier();
     vendorId =serial_Info.vendorIdentifier();
     qDebug () << "Product Id "<<serial_Info.productIdentifier();
     productId = serial_Info.productIdentifier();
     arduino_available = true;
    }
    if (arduino_available){

        inicializacionarduino();
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::inicializacionarduino(){

   serial-> setPortName(numerodepuerto);
   serial-> setBaudRate(QSerialPort::Baud9600);
   serial-> setDataBits(QSerialPort::Data8);
   serial-> setParity(QSerialPort::NoParity);
   serial-> setStopBits(QSerialPort::OneStop);
   serial-> setFlowControl(QSerialPort::NoFlowControl);
   serial->open(QIODevice::ReadWrite);
}


void MainWindow::on_Encendido_clicked()
{
    if (serial->isWritable()){
        serial->write("1");
    }
}

void MainWindow::on_pushButton_3_clicked()
{
    if (serial->isWritable()){
        serial->write("2");
    }
}

void MainWindow::on_Parpadear_clicked()
{
    if (serial->isWritable()){
        serial->write("3");
    }
}
