# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMyAppLED.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout.addWidget(self.btn2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.OnOffTxt = QtWidgets.QLabel(self.centralwidget)
        self.OnOffTxt.setObjectName("OnOffTxt")
        self.verticalLayout.addWidget(self.OnOffTxt)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED - IE3 2019"))
        self.btn1.setText(_translate("MainWindow", "ON"))
        self.btn2.setText(_translate("MainWindow", "OFF"))
        self.OnOffTxt.setText(_translate("MainWindow", "LED OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

