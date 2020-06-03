#include "mainwindow.h"
#include "ui_mainwindow.h"
#define Direccion 0x48
#define LEC1 6
#define Base 120
#define Valordelmotoreninstantex
#define VelocidadMotor 7
#define ValorPWM 100
#define panel_solar 15
#define Boton_zarpar 5
#define Velocidad_Motor_Propulcion 16
#define Base2 120
int PWM , Velocidad;


MainWindow::MainWindow(QWidget *parent):
     QMainWindow(parent),
     ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    wiringPiSetup();
    pcf8591Setup(BASE,Direccion);
    softPwmCreate(VelocidadMotor,Valordelmotoreninstantex,ValorPWM );
    softPwmCreate (Velocidad_Motor_Propulcion,Velocidad,PWM)
    pinMode (panel_solar,INPUT);
    pinMode (Boton_zarpar, OUTPUT);

}

MainWindow::~MainWindow()
{
    delete ui;

}


void MainWindow::on_label_linkActivated(const QString &link)
{
    int valor;
    float tensionbateria;
    valor AnalogRead (BASE + LEC1);
    tensionbateria = (valor*(4.8/(50000/75000))/255;
    ui->lectura_LEC1->setText (QString::number(tensionbateria,'f',2)+ 'Volts')
}

void MainWindow::on_verticalSlider_actionTriggered(int action)
{
    float motor;
    motor AnalogRead (Base ,VelocidadMotor);
    softPwmWrite (VelocidadMotor,action);
    ui->Motor->setText (QString::number ("La velocidad del motor es:"(motor,'f',1));
}

void MainWindow::on_label_5_linkActivated(const QString &link)
{
    if (digitalWrite(panel_solar)== HIGH){
        printf("El panel solar esta activo");
    }
    else {
         printf("El panel solar no esta activo");
    }
}

void MainWindow::on_pushButton_clicked()
{
digitalWrite (Boton_zarpar,HIGH);
delay (500);
}

void MainWindow::on_verticalSlider_2_actionTriggered(int action)
{
    float motorprop;
    motorprop AnalogRead (Base2 ,Velocidad_Motor_Propulcion);
    softPwmWrite (Velocidad_Motor_Propulcion,action)
    ui->LecturaProp->setText (QString::number"La velocidad del motor de propulcion es:"(motorprop,'f',1));
}

}
