#include "widget.h"
#include "ui_widget.h"
#include <QTcpSocket>
#include <QTextStream.h>
Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    mSocket = new QTcpSocket (this);

    connect (mSocket,&QTcpSocket::readyRead, [&](){

          QTextStream T(mSocket);
          ui->listWidget->addItem(T.readAll());

    });
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_conectar_clicked()
{
     mSocket -> connectToHost(ui->servidor->text(),ui->puerto->value());
}

void Widget::on_quitar_clicked()
{
    close ();
}
