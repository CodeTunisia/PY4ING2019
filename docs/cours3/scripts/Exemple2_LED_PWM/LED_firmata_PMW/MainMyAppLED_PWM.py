## NOM DU PROGRAMME: MainMyAppLED_PWM.py
#% IMPORTATION
from PyQt5.QtWidgets import QMainWindow, QApplication
from UiMyAppLED import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import pyfirmata

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        PORT = 'COM3'
        self.board = pyfirmata.Arduino(PORT)
        self.LEDpin = self.board.get_pin('d:11:p') 
        ## d = digital, 11 = numéro de la pin, p = PWM

        
    # Ajouter des signaux
    @pyqtSlot(int)
    def on_pwm_valueChanged(self, value):
        '''
        mettre à jour la valeur
        '''
        self.board.digital[self.LEDpin.pin_number].write(value/100.0)
        self.lcd.display(value)
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())