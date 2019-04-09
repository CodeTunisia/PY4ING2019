## NOM DU PROGRAMME: MainMyAppLED.py
#% IMPORTATION
from PyQt5.QtWidgets import QMainWindow, QApplication
from UiMyAppLED import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import pyfirmata

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.PIN = 13 # Pin 13 est utilisé
        PORT = 'COM3'
        self.board = pyfirmata.Arduino(PORT)
    # Ajouter des signaux
    @pyqtSlot()
    def on_btn1_clicked(self):
        '''
        Allumer la LED et afficher: LED ON
        '''
        self.board.digital[self.PIN].write(1) # Set the LED pin to 1 (HIGH)
        message= "LED ON"
        self.OnOffTxt.setText(message)
    @pyqtSlot()
    def on_btn2_clicked(self):
        '''
        Allumer la LED et afficher: LED OFF
        '''
        self.board.digital[self.PIN].write(0) # Set the LED pin to 0 (LOW)
        message= "LED OFF"
        self.OnOffTxt.setText(message)
        
        
    
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())