# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iplbl = QtWidgets.QLabel(self.centralwidget)
        self.iplbl.setGeometry(QtCore.QRect(290, 70, 191, 41))
        self.iplbl.setStyleSheet("font: 14pt \"Palatino Linotype\";")
        self.iplbl.setObjectName("iplbl")
        self.infoEdit = QtWidgets.QTextBrowser(self.centralwidget)
        self.infoEdit.setGeometry(QtCore.QRect(10, 120, 781, 331))
        self.infoEdit.setObjectName("infoEdit")
        self.resetbttn = QtWidgets.QPushButton(self.centralwidget)
        self.resetbttn.setGeometry(QtCore.QRect(330, 470, 131, 51))
        self.resetbttn.setObjectName("resetbttn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 40, 154, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 italic 16pt \"Palatino Linotype\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.statuslbl = QtWidgets.QLabel(self.widget)
        self.statuslbl.setStyleSheet("font: 75 italic 14pt \"Palatino Linotype\";")
        self.statuslbl.setObjectName("statuslbl")
        self.horizontalLayout.addWidget(self.statuslbl)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server Side"))
        self.iplbl.setText(_translate("MainWindow", "XX.XX.XX.XX"))
        self.resetbttn.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.statuslbl.setText(_translate("MainWindow", "Not Ready"))

    