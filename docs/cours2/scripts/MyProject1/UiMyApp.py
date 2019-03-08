# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMyApp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spb = QtWidgets.QSpinBox(self.centralwidget)
        self.spb.setMaximum(100)
        self.spb.setProperty("value", 50)
        self.spb.setObjectName("spb")
        self.horizontalLayout.addWidget(self.spb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.valeur = QtWidgets.QLabel(self.centralwidget)
        self.valeur.setText("")
        self.valeur.setObjectName("valeur")
        self.horizontalLayout.addWidget(self.valeur)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sldr = QtWidgets.QSlider(self.centralwidget)
        self.sldr.setMaximum(100)
        self.sldr.setProperty("value", 50)
        self.sldr.setOrientation(QtCore.Qt.Horizontal)
        self.sldr.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sldr.setObjectName("sldr")
        self.verticalLayout.addWidget(self.sldr)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setMaximum(100)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.horizontalLayout_2.addWidget(self.dial)
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setStyleSheet("color: rgb(85, 255, 0);")
        self.lcd.setObjectName("lcd")
        self.horizontalLayout_2.addWidget(self.lcd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Myfirst app"))
        self.label1.setText(_translate("MainWindow", "Ma première application affiche: "))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#005500;\">Bonjour IE3</span></p></body></html>"))
        self.btn1.setToolTip(_translate("MainWindow", "affiche bonjour"))
        self.btn1.setText(_translate("MainWindow", "Bonjour"))
        self.btn2.setToolTip(_translate("MainWindow", "affiche au revoir"))
        self.btn2.setText(_translate("MainWindow", "Au revoir"))
        self.label.setAccessibleName(_translate("MainWindow", "label3"))
        self.label.setText(_translate("MainWindow", "Valeur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

