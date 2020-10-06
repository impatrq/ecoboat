#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTImer>
#include <wiringPi.h>
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
    void on_pushButton_clicked();

    void on_label_2_linkActivated(const QString &link);

    void on_horizontalSlider_actionTriggered(int action);

    void on_horizontalSlider_2_actionTriggered(int action);

private:
    Ui::MainWindow *ui;
private slots:
    void update_estado1 ();
    void update_estado2 ();
    void on_textBrowser_copyAvailable(bool b);
    void on_pushButton_2_clicked();
    void on_textBrowser_2_copyAvailable(bool b);
};
#endif // MAINWINDOW_H
