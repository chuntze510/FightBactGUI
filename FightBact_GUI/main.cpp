#include "mainwindow.h"
#include <QApplication>
#include <QCoreApplication>
#include <QDebug>
#include <QtSerialPort/QtSerialPort>
#include <QSerialPortInfo>
#include <QSerialPort>

int main(int argc, char *argv[])
{

    QApplication a(argc, argv);
    MainWindow main_window;
    main_window.show();

    return a.exec();
}
