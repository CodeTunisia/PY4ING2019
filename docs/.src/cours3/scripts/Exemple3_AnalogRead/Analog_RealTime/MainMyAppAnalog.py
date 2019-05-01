## NOM DU PROGRAMME: MainMyAppAnalog.py
#% IMPORTATION
from PyQt5.QtWidgets import QMainWindow, QApplication
from UiMyAppAnalog import Ui_MainWindow
from PyQt5.QtCore import QTimer
import pyfirmata
import pyqtgraph
import time


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        port = 'COM3' #windows
        #port = '/dev/ttyACM0'   #linux
        self.board = pyfirmata.Arduino(port)
        it = pyfirmata.util.Iterator(self.board)  # itérateur permet de ne pas engorger 
                                     # la communication série
        it.start()
        
        self.pinA0 = self.board.get_pin('a:0:i')   # a = analogique, 0 = numéro de la pin, i = input.
        self.LEDpin = self.board.get_pin('d:11:p') # d = digital, 11 = numÃ©ro de la pin, p = PWM
        self.pyqtgraph.plotItem.showGrid(True, True, 0.7)
        self.pData = [0]  # initiliser la valeur du potentiometre par 0
        self.p1= self.pyqtgraph.plot(self.pData)
        time.sleep(1)
        self.update()
        
    def update(self):
        '''
        mettre à jour la valeur
        '''
        time.sleep(1)
        valeur = self.pinA0.read()
        self.lcd.display(valeur)
        self.board.digital[self.LEDpin.pin_number].write(valeur)
        self.pData += [valeur] # Ajouter la valeur du potentimetre à chaque mis à jour
        pen=pyqtgraph.mkPen(color="r",width=3)
        self.p1.setData(self.pData, pen=pen)
        QTimer.singleShot(10, self.update) # QUICKLY repeat
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())