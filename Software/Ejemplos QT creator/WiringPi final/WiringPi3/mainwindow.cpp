#include "mainwindow.h"
#include "ui_mainwindow.h"
#define Base 120
#define Base1 120
#define zarpar 5
double tension,Velocidad , Velocidad1,estado,estado3,datos, Motor , Motor1;
QString longitud , latitud;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPlaceSearchRequest searchRequest;
    searchRequest.setSearchTerm("  ");
    searchRequest.setSearchArea(QGeoCircle(QGeoCoordinate(12.34, 56.78)));
    searchReply = manager->search(searchRequest);
    connect(searchReply, SIGNAL(finished()), this, SLOT(handleSearchReply()));
    //codigo del gps

    wiringPiSetup();
    pcf8591Setup(BASE,Direccion);
    softPwmCreate(Motor,Velocidad);
    softPwmCreate (Motor1,Velocidad1);
    pinMode (panel_solar,INPUT);
    pinMode (zarpar , OUTPUT);
    pinMode (tension , INPUT);
    pinMode (estado , INPUT);
    pinMode (estado3 , INPUT);
    pinMode (datos , OUTPUT);
    QTimer *timer= new QTimer (this);
    connect(timer,SIGNAL(timeout()),this,SLOT(update_estado1()));
    timer -> start(100); //CADA 100 MS ANALIZA EL ESTADO DEL PANEL
    connect(timer,SIGNAL(timeout()),this,SLOT(update_estado2()));
    timer -> start(100);


}

MainWindow::~MainWindow()
{
    delete ui;
}
void handleSearchReply() {
    if (searchReply->error() == QPlaceReply::NoError) {
        foreach (const QPlaceSearchResult &result, searchReply->results()) {
            if (result.type() == QPlaceSearchResult::PlaceResult) {
                QPlaceResult placeResult = result;
                qDebug() << "Name: " << placeResult.place().name();
                qDebug() << "Coordinate " << placeResult.place().location().coordinate().toString();
                qDebug() << "Street: " << placeResult.place().location().address().street();
                qDebug() << "Distance: " << placeResult.distance();
            }
        }
    }
    searchReply->deleteLater();  //discard reply
    searchReply = 0;

}
if (!place.detailsFetched()) {
    /*QPlaceDetailsReply * */ detailsReply = manager->getPlaceDetails(place.placeId());
    connect(detailsReply, SIGNAL(finished()), this, SLOT(handleDetailsReply()));
}

void handleDetailsReply() {
    QPlace place;
    if (detailsReply->error() == QPlaceReply::NoError)
        place = detailsReply->place();

    detailsReply->deleteLater(); //discard reply
    detailsReply = 0;
}

void MainWindow::on_pushButton_clicked()
{
    digitalWrite (zarpar , HIGH);
    timer -> start(100); //PONEMOS 100 MILISEGUNDOS DE DELAY.
}

void MainWindow::on_label_2_linkActivated(const QString &link)
{
    double valor,porcentaje;
    tension AnalogRead (Base + valor);
    valor = tension * 0.0470588;
    porcentaje = tension * 0.047055;
    ui->label_2->setText (QString::number(valor,'f',2)+ 'Volts');
    ui->label_7->setText (QString::number(porcentaje,'f',2)+ 'Volts');
}



void MainWindow::on_horizontalSlider_actionTriggered(int action)
{
    Motor AnalogRead (Base1 ,Velocidad);
    softPwmWrite (Velocidad,action);
    ui->motor->setText (QString::number(" "(Motor,'f',1)));

}

void MainWindow::on_horizontalSlider_2_actionTriggered(int action)
{
    Motor1 AnalogRead (Base ,Velocidad);
    softPwmWrite (Velocidad,action);
    ui->motor1-> setText (QString::number (" "(Motor1,'f',1)));
}
void MainWindow::update_estado1(){
QPixmap panelpixmap;
if (digitalRead(estado) == HIGH){
    panelpyxmap.load (QString::fromUtf8(":/new/carpeta1/tilde.png")); //Aca no pongo nada por que no se donde va a estar, pero solamente hay que poner la dirrecion
    ui->label_3 ->setPixmap (panelpixmap);
   }
else {
    panelpyxmap.load (QString::fromUtf8(":/new/carpeta1/cruz.png"));
    ui->label_3 ->setPixmap (panelpixmap);
   }
}
void MainWindow::update_estado2(){
QPixmap pixmap2;
if (digitalRead(estado3) == HIGH){
    pyxmap2.load (QString::fromUtf8(":/new/carpeta1/tilde.png"));
    ui->label_4 ->setPixmap (pixmap2);
   }
else {
    pyxmap2.load (QString::fromUtf8(":/new/carpeta1/cruz.png"));
    ui->label_4 ->setPixmap (pixmap2);
   }
}

void MainWindow::on_textBrowser_copyAvailable(bool b)
{
    InitializeComponent();

}

void MainWindow::on_pushButton_2_clicked()
{
    longitud = QTextBrowser.Text;
    latitud = QTextBrowser_2.Text;

    digitalWrite (5, longitud);
    timer (100);
    digitalWrite (5,latitud);
}


