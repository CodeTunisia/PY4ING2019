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
        board = pyfirmata.Arduino(port)
        it = pyfirmata.util.Iterator(board)  # itérateur permet de ne pas engorger 
                                     # la communication série
        it.start()
        
        self.pinA0 = board.get_pin('a:0:i')   # a = analogique, 0 = numéro de la pin, i = input.
        LEDpin = board.get_pin('d:11:p') # d = digital, 11 = numÃ©ro de la pin, p = PWM
        self.pyqtgraph.plotItem.showGrid(True, True, 0.7)
        self.update()
        
    def update(self):
        '''
        mettre à jour la valeur
        '''
        time.sleep(1)
        valeur = self.pinA0.read()
        self.lcd.display(valeur)
        pData = [0] * 25    # initiliser par une liste de 25 valeurs = 0
        pData.append(valeur) # ajouter la valeur à la fin de la liste
        del pData[0] # effacer le premier éliment de la liste 
        xData = [i for i in range(25)]
        C=pyqtgraph.hsvColor(0.95,alpha=.9)
        pen=pyqtgraph.mkPen(color=C,width=3)
        self.pyqtgraph.plot(xData, pData,pen=pen,clear=True)
        QTimer.singleShot(1, self.update) # QUICKLY repeat
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())