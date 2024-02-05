# -*- coding: utf-8 -*-
# ui 파일 변환 명령어 : pyuic5 ui파일 -o py파일

import threading

from uart import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

# CPU -> MICOM send command
# MICOM -> CPU response command
# MICOM -> CPU send command
# CPU -> MICOM response command
state = [0x0A, 0x0B, 0x0C, 0x0D]

global data

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 510)
        MainWindow.setMinimumSize(QtCore.QSize(610, 510))
        MainWindow.setMaximumSize(QtCore.QSize(610, 510))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 172, 203))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setMinimumSize(QtCore.QSize(170, 24))
        self.textEdit.setMaximumSize(QtCore.QSize(170, 24))
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.baudrateBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.baudrateBox.setMinimumSize(QtCore.QSize(170, 20))
        self.baudrateBox.setMaximumSize(QtCore.QSize(158, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.baudrateBox.setFont(font)
        self.baudrateBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baudrateBox.setAutoFillBackground(False)
        self.baudrateBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.baudrateBox.setObjectName("baudrateBox")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.verticalLayout.addWidget(self.baudrateBox)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setMinimumSize(QtCore.QSize(170, 24))
        self.textEdit_2.setMaximumSize(QtCore.QSize(170, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.stateBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.stateBox.setMinimumSize(QtCore.QSize(158, 25))
        self.stateBox.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.stateBox.setFont(font)
        self.stateBox.setObjectName("stateBox")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.verticalLayout.addWidget(self.stateBox)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setMinimumSize(QtCore.QSize(170, 24))
        self.textEdit_3.setMaximumSize(QtCore.QSize(170, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.delBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")
        self.horizontalLayout.addWidget(self.delBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(110, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.filepath = QtWidgets.QPushButton(self.centralwidget)
        self.filepath.setGeometry(QtCore.QRect(10, 430, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filepath.setFont(font)
        self.filepath.setObjectName("filepath")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(110, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clearbtn.setFont(font)
        self.clearbtn.setObjectName("clearbtn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 10, 391, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setMinimumSize(QtCore.QSize(85, 24))
        self.textEdit_4.setMaximumSize(QtCore.QSize(85, 24))
        self.textEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_3.addWidget(self.textEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.sendBox = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.sendBox.setObjectName("sendBox")
        self.verticalLayout_2.addWidget(self.sendBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setMinimumSize(QtCore.QSize(85, 0))
        self.textEdit_5.setMaximumSize(QtCore.QSize(85, 24))
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayout_4.addWidget(self.textEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.responseBox = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.responseBox.setObjectName("responseBox")
        self.verticalLayout_2.addWidget(self.responseBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startBtn.clicked.connect(self.btnEvent)
        self.filepath.clicked.connect(self.pathEvent)
        self.clearbtn.clicked.connect(self.clearEvent)

        self.addBtn.clicked.connect(self.addEvent)
        self.delBtn.clicked.connect(self.delEvent)

        def response():
            while 1:
                if self.baudrateBox.currentText() is not None:
                    connection = uart(getport(), self.baudrateBox.currentText())
                    ser = connection.open()
                    print(ser.readlines())

        thread = threading.Thread(target=response, args=())
        thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UART"))
        self.textEdit.setMarkdown(_translate("MainWindow", "**BAUDRATE**\n"
                                                           "\n"
                                                           ""))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; "
                                         "font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><span style=\" "
                                         "font-weight:600;\">BAUDRATE</span></p></body></html>"))
        self.baudrateBox.setCurrentText(_translate("MainWindow", "9600"))
        self.baudrateBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrateBox.setItemText(1, _translate("MainWindow", "19200"))
        self.baudrateBox.setItemText(2, _translate("MainWindow", "38400"))
        self.baudrateBox.setItemText(3, _translate("MainWindow", "57600"))
        self.baudrateBox.setItemText(4, _translate("MainWindow", "115200"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                           "type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Agency FB\'; font-size:9pt; "
                                           "font-weight:600; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><span style=\" "
                                           "font-family:\'Gulim\';\">STATE</span></p></body></html>"))
        self.stateBox.setItemText(0, _translate("MainWindow", "CPU->MICOM / SEND"))
        self.stateBox.setItemText(1, _translate("MainWindow", "CPU->MICOM / RESPONSE"))
        self.stateBox.setItemText(2, _translate("MainWindow", "MICOM->CPU / SEND"))
        self.stateBox.setItemText(3, _translate("MainWindow", "MICOM->CPU / RESPONSE"))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                           "type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Agency FB\'; font-size:9pt; "
                                           "font-weight:600; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><span style=\" font-family:\'Gulim\';\">COMMAND "
                                           "ID</span></p></body></html>"))
        self.addBtn.setText(_translate("MainWindow", "추가"))
        self.delBtn.setText(_translate("MainWindow", "삭제"))
        self.startBtn.setText(_translate("MainWindow", "실행"))
        self.filepath.setText(_translate("MainWindow", "파일 선택"))
        self.clearbtn.setText(_translate("MainWindow", "CLEAR"))
        self.textEdit_4.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style"
                                           "type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; "
                                           "font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;"
                                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><span style=\" "
                                           "font-weight:600;\">SEND</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style"
                                           "type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; "
                                           "font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                           "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                           "font-weight:600;\">RESPONSE</span></p></body></html>"))

    # file open event
    def pathEvent(self):
        try:
            global data
            path = QFileDialog.getOpenFileName(self, '파일 선택')
            if path[0]:
                with open(path[0], 'r', encoding='UTF8') as file:
                    readData = file.readlines()
                data = [hex(ord(text)) for text in readData]
            else:
                def Critical_event():
                    QMessageBox.critical(self, 'WARN', 'NO FILE WAS SELECTED')
                Critical_event()

        except Exception as ex:
            print(ex)

    # start progress event
    def btnEvent(self):
        try:
            port = getport()

            baudRate = self.baudrateBox.currentText()
            connection = uart(port, baudRate)
            # data => start(1) / state(1) / length(2) / command id(1) / data0 ~ dataN
            header = ['0x02']

            direction = self.stateBox.currentText()

            if direction == 'CPU->MICOM / SEND':
                if data is not None:
                    header[1] += state[0]

                    length = hex(5 + len(data))
                    header.append(length)

                    commandId = self.comboBox.currentText()
                    header.append(str(commandId))

                    # send data
                    result = header + data

                    # checksum
                    checksum = 0
                    for i in result:
                        checksum += int(i, 0)
                    checksum = hex(checksum)[:2] + hex(checksum)[-2:]

                    result += checksum
                    # send data format : ID + length + data + ack + checksum
                    for i in result:
                        with connection.open() as ser:
                            ser.write(i[2:])
                            self.sendBox.addItem(i[2:])

            # elif direction == 'CPU->MICOM / RESPONSE':
            #     header[1] += state[3]
            # elif direction == 'MICOM->CPU / SEND':
            #     header[1] += state[1]
            #     with connection.open() as ser:
            #         readData = ser.readlines()
            #         print(readData)
            # 'MICOM->CPU / RESPONSE'
            # else:
            #     header[1] += state[2]

        except Exception as ex:
            print(ex)

    def clearEvent(self):
        self.responseBox.clear()
        self.sendBox.clear()

    def addEvent(self):
        def add_event():
            QMessageBox.critical(self, 'WARN', 'Not implemented')
        add_event()

    def delEvent(self):
        def del_event():
            QMessageBox.critical(self, 'WARN', 'Not implemented')
        del_event()
