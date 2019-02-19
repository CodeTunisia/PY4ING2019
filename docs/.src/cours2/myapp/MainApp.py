## NOM DU PROGRAMME: MainApp.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from UiMainApp import Ui_MainWindow
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
    @pyqtSlot()  # signal du bouton bonjour
    def on_button1_clicked(self):
        '''
        Afficher un message "Bonjour"
        '''
        message = "<h3><b><font color='green'>Bonjour IE3!</font></b>"
        self.label2.setText(message)

    @pyqtSlot()  # signal du bouton au revoir
    def on_button2_clicked(self):
        '''
        Afficher un message "Au revoir"
        '''
        message = "<h3><b><font color='red'>Au revoir IE3!</font></b>"
        self.label2.setText(message)

    @pyqtSlot(int)  # signal du Spin Box: renvoie un entier
    def on_spb_valueChanged(self, value):
        '''
        la valeur du Spin Box est un entier,
        convertissez-le en chaîne à l'aide de la fonction str().
        '''
        self.val.setText(str(self.spb.value()))
        # connecter le curseur au Spin Box
        self.sldr.setValue(value)
        self.lcd.display(value)

    @pyqtSlot(int)  # signal du curseur
    def on_sldr_valueChanged(self, value):
        '''
        connecter le Spin Box au curseur
        '''
        self.spb.setValue(value)
        self.lcd.display(value)
    @pyqtSlot(int)  # signal du curseur
    def on_dial_valueChanged(self, value):
        '''
        connecter le Spin Box au curseur
        '''
        self.spb.setValue(value)
        self.lcd.display(value)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Myapplication = MainApp()
    Myapplication.show()
    sys.exit(app.exec_())