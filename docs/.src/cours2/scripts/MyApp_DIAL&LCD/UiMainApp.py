# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainApp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 229)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.val = QtWidgets.QLabel(self.centralwidget)
        self.val.setText("")
        self.val.setObjectName("val")
        self.gridLayout.addWidget(self.val, 2, 3, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 2)
        self.spb = QtWidgets.QSpinBox(self.centralwidget)
        self.spb.setMaximum(100)
        self.spb.setObjectName("spb")
        self.gridLayout.addWidget(self.spb, 2, 2, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 2, 1, 1)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 2)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 1, 0, 1, 2)
        self.sldr = QtWidgets.QSlider(self.centralwidget)
        self.sldr.setMaximum(100)
        self.sldr.setOrientation(QtCore.Qt.Horizontal)
        self.sldr.setObjectName("sldr")
        self.gridLayout.addWidget(self.sldr, 3, 0, 1, 4)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 1, 2, 1, 2)
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setStyleSheet("color: rgb(153, 255, 0);\n"
"background-color: rgb(0, 85, 0);")
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd.setObjectName("lcd")
        self.gridLayout.addWidget(self.lcd, 4, 3, 1, 1)
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setAutoFillBackground(False)
        self.dial.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.dial.setMaximum(100)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My first app"))
        self.label1.setText(_translate("MainWindow", "Ma première application affiche: "))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Bonjour IE3!</span></p></body></html>"))
        self.label3.setText(_translate("MainWindow", "La valeur actuelle est: "))
        self.button1.setToolTip(_translate("MainWindow", "C\'est le bouton Bonjour"))
        self.button1.setText(_translate("MainWindow", "Bonjour"))
        self.button2.setToolTip(_translate("MainWindow", "C\'est le bouton Au revoir"))
        self.button2.setText(_translate("MainWindow", "Au revoir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

