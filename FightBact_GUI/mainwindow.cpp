#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "stdlib.h"
#include <QMessageBox>
#include <QPushButton>
#include <QDebug>
#include <QIODevice>
#include <QSerialPortInfo>
#include <QSerialPort>




MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
  //connect(serial, static_cast<void (QSerialPort::*)(QSerialPort::SerialPortError)>(&QSerialPort::error)this, &MainWindow::handleError);

   QObject::connect(serial, &QSerialPort::readyRead, this, &MainWindow::readData);
  //connect(console, &Console::getData, this, &MainWindow::writeData);
   serial = new QSerialPort(this);
   ui->setupUi(this);
   connect(ui->X_R, SIGNAL(clicked(bool)), this, SLOT(onbtn2()));
   connect(ui->connect, SIGNAL(clicked(bool)), this, SLOT(openSerialPort()));
}
MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_X_L_clicked()
{
    qDebug()<<"you click XL";

}

void MainWindow::onbtn2()
{
    qDebug()<<"you click XR";
}


void MainWindow::openSerialPort()
{
    QSerialPort serial;
    serial.setPortName("COM3");
    serial.setBaudRate(QSerialPort::Baud9600);
    serial.setDataBits(QSerialPort::Data8);
    serial.setParity(QSerialPort::NoParity);
    serial.setStopBits(QSerialPort::OneStop);
    serial.setFlowControl(QSerialPort::NoFlowControl);
    serial.open(QIODevice::ReadWrite);
    if(!serial.open(QIODevice::ReadWrite))
          {
              qDebug()<<"can't not open";
              QMessageBox::about(NULL, "notice", "can't not open");
              return;
          }
}

void MainWindow::readData()
{
    QByteArray buffer = serial->readAll();
    QString recv = ui->recvTextEdit->toPlainText();
    recv += QString(buffer);
    ui->recvTextEdit->clear();
    ui->recvTextEdit->append(recv);
}

void MainWindow::on_send_clicked()
{
    QByteArray data = ui->sendTextEdit->toPlainText().toUtf8();
    serial->write(data);
}

void MainWindow::on_pushButton_2_clicked()
{
    ui->recvTextEdit->clear();
}
