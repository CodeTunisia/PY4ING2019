# NOM DU FICHIER: QLCD.py
#% IMPORTATION
import sys
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication)

class QLCDNumber_QDial(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        the_lcd = QLCDNumber(self)
        the_dial = QDial(self)

        self.setGeometry(150, 100, 220, 100)
        self.setWindowTitle('QLCDNumber')

        the_lcd.setGeometry(10,10,70,70)
        the_dial.setGeometry(140,10,70,70)

        the_dial.valueChanged.connect(the_lcd.display)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = QLCDNumber_QDial() 
    sys.exit(app.exec_())