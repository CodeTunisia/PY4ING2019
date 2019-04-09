## NOM DU PROGRAMME: MainMyApp.py
#% IMPORTATION
from PyQt5.QtWidgets import QMainWindow, QApplication
from UiMyApp import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        
    # Ajouter des signaux
    @pyqtSlot()
    def on_btn1_clicked(self):
        '''
        Afficher un messge bonjour dans label2
        '''
        message='''<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#005500;">Bonjour IE3</span></p></body></html>'''
        self.label2.setText(message)
    @pyqtSlot()
    def on_btn2_clicked(self):
        '''
        Afficher un messge au revoir dans label2
        '''
        message = ''' <html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#aa0000;">Au revoir IE3</span></p></body></html>'''
        self.label2.setText(message)
    @pyqtSlot(int)
    def on_spb_valueChanged(self, value):
        """
        changer la valeur de 1 à 100 et l'afficher dans label valeur
        """
        self.valeur.setText(str(value))
        self.sldr.setValue(value)
        self.dial.setValue(value)
        self.lcd.display(value)
    # Ajouter d'autre widgets, soit par exemple:
    # * Dial
    # * Display LCD
    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        """
        Relier le Dial au SpinBox et au Slider
        """
        self.sldr.setValue(value)
        self.spb.setValue(value)
        self.lcd.display(value)
        
    @pyqtSlot(int)
    def on_sldr_valueChanged(self, value):
        '''
        mettre à jour la valeur du SpinBox et du texte dans label valeur
        '''
        self.spb.setValue(value)
        self.dial.setValue(value)
        self.lcd.display(value)
        
        
    
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())