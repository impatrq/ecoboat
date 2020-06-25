#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    tcpservidor = new QTcpServer (this);

    tcpservidor -> setMaxPendingConnections(2);

    for (int i = 0 ; i < tcpservidor-> maxPendingConnections() ; i++){

        tcpcliente[i] = new QTcpSocket (this);

    }


    tcpservidor->listen(QHostAddress::LocalHost,124);

    connect (tcpservidor,SIGNAL( newConnection()) ,this , SLOT (conexioueva()));

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::conexionueva(){

    static int j=0;
    tcpcliente[j] = tcpservidor -> nextPendingConnection();


    connect (tcpcliente[j] , SIGNAL (readyRead()), this, SLOT (leer_cliente()));
            j++;
}




void MainWindow:: leer_cliente(){

     if (tcpcliente[0] ->bytesAvailable() > 0){

         QByteArray buffer;
         buffer.resize(tcpcliente[0] -> bytesAvailable());
         tcpcliente[0]->read (buffer.data(),buffer.size());
         ui -> plainTextEdit->setReadOnly (true);
         ui -> plainTextEdit->appendPlainText (QString (buffer));

     }

     else if (tcpcliente[1]->bytesAvailable() > 0){

        QByteArray buffer;
        buffer.resize(tcpcliente[1]->bytesAvailable());
        tcpcliente [1] ->read(buffer.data() , buffer.size());
        ui->plainTextEdit->setReadOnly (true);
        ui->plainTextEdit -> AppendPlainText (QString(buffer));

     }

     else {

         ui->plainTextEdit -> AppendPlainText ("No existe una comunicacion con el socket");
     }
}

void MainWindow::cliente2_on_cliked(){
        tcpcliente[0]-write(ui-> QLineEdit ->text().toLatin1().data(),ui-> QLineEdit ->text().size());
        ui->QLineEdit->clear();
}
void MainWindow::cliente_on_clicked(){
    tcpcliente[0]-write(ui->QLineEdit->text().toLatin1().data(),ui->QLineEdit ->text().size());
    ui->QLineEdit->clear();
}

