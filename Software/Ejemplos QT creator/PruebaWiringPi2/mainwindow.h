#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <wiringPi.h>
#include <sofrPwm.h>
#include <QTime>
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
    void on_label_linkActivated(const QString &link);

    void on_verticalSlider_actionTriggered(int action);
private slots :
    void panel_solar ();
    void on_label_5_linkActivated(const QString &link);

    void on_pushButton_clicked();

    void on_verticalSlider_2_actionTriggered(int action);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
