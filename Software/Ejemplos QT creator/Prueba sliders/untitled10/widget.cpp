#include "widget.h"
#include "ui_widget.h"
#include <QProgressBar>



#include <QWidget>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{

  //  int x = 50;
   // ui->progressBar->valueChanged(x);


}


void Widget::on_pushButton_clicked()
{
    close();
}

void Widget::on_pushButton_2_clicked()
{


}

void Widget::on_progressBar_valueChanged(int value)
{
    int bateria = 40;
    ui->progressBar->setMinimum(0);
    ui->progressBar->setMaximum(100);
    //value=50;
    ui->progressBar->valueChanged(bateria);
    update();
}

void Widget::on_horizontalSlider_valueChanged(int value)
{

    float x[2];
    x[0] = 10;
    ui->horizontalSlider->setRange(0, 100);
    ui->horizontalSlider->setValue(x[0]);
    ui->horizontalSlider->update();




}

void Widget::on_horizontalSlider_2_valueChanged(int value)
{
    int x[2];
    x[0] = 50;
    ui->horizontalSlider_2->setRange(0, 100);
    ui->horizontalSlider_2->setValue(x[0]);
    ui->horizontalSlider_2->update();
}
