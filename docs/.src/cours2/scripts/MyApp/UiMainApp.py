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
        MainWindow.resize(392, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spb = QtWidgets.QSpinBox(self.centralwidget)
        self.spb.setMaximum(100)
        self.spb.setObjectName("spb")
        self.gridLayout.addWidget(self.spb, 2, 1, 1, 1)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.val = QtWidgets.QLabel(self.centralwidget)
        self.val.setText("")
        self.val.setObjectName("val")
        self.gridLayout.addWidget(self.val, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.sldr = QtWidgets.QSlider(self.centralwidget)
        self.sldr.setMaximum(100)
        self.sldr.setOrientation(QtCore.Qt.Horizontal)
        self.sldr.setObjectName("sldr")
        self.verticalLayout.addWidget(self.sldr)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 20))
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
        self.label3.setText(_translate("MainWindow", "La valeur actuelle est: "))
        self.button1.setToolTip(_translate("MainWindow", "C\'est le bouton Bonjour"))
        self.button1.setText(_translate("MainWindow", "Bonjour"))
        self.button2.setToolTip(_translate("MainWindow", "C\'est le bouton Au revoir"))
        self.button2.setText(_translate("MainWindow", "Au revoir"))
        self.label1.setText(_translate("MainWindow", "Ma première application affiche: "))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Bonjour IE3!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

