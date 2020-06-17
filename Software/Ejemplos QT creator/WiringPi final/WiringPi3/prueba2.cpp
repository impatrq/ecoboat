#include "mainwindow.h"
#include "ui_mainwindow.h"
#define Base 120
#define zarpar 5
#define Motor1
#define Motor
double tension,Velocidad , Velocidad1;


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    wiringPiSetup();
    pcf8591Setup(BASE,Direccion);
    softPwmCreate(Motor,Velocidad);
    softPwmCreate (Motor1,Velocidad1);
    pinMode (panel_solar,INPUT);
    pinMode (zarpar , OUTPUT);
    pinMode (tension , INPUT);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    digitalWrite (zarpar , HIGH);
    delay (50);
}

void MainWindow::on_label_2_linkActivated(const QString &link)
{
    double valor;
    tension AnalogRead (BASE + valor);
    valor = tension * 0.0470588;
    ui->label_2->setText (QString::number(valor,'f',2)+ 'Volts');
}

void MainWindow::on_horizontalSlider_actionTriggered(int action)
{
    Motor AnalogRead (Base ,Velocidad);
    softPwmWrite (Velocidad,action);
    ui->motor1-> setText (QString::number ("La velocidad del motor es:"(Motor,'f',1));
}

void MainWindow::on_horizontalSlider_2_actionTriggered(int action)
{
    Motor1 AnalogRead (Base ,Velocidad);
    softPwmWrite (Velocidad,action);
    ui->motor1-> setText (QString::number ("La velocidad del motor es:"(Motor1,'f',1));
}
