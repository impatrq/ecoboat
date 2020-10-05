#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_progressBar_valueChanged(int value);

    void on_horizontalSlider_valueChanged(int value);

    void on_horizontalSlider_sliderMoved(int position);

    void on_verticalSlider_actionTriggered(int action);

    void on_horizontalSlider_2_windowIconTextChanged(const QString &iconText);

    void on_horizontalSlider_2_valueChanged(int value);

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
