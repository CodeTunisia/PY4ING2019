# NOM DU FICHIER: myfirstappButtons.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow):
    '''
    DOCUMENTATION
    -------------
    Créer une fenêtre (300x200 pixels)
    '''
    def __init__(self):
        '''
        INITIALISEUR 
        ------------
        La classe `MainWindow()` rendre une fenêtre (300x200 pixels) 
        avec un titre 'My first app'.
        '''
        super(MainWindow, self).__init__()
        # GUI proprieties
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')
        # Ajouter des étiquettes: QLabel
        ## Label 1: Texte brut
        self.label1 = QLabel('Ma première application affiche: ', self)
        # fixer la largeur de l'étiquette
        self.label1.setFixedWidth(160)
        # position de l'étiquette (x, y) en pixels
        self.label1.move(10, 10)
        ## Label 2: Texte riche
        self.label2 = QLabel("", self)
        # créer un message HTML
        message = "<h3><b><font color='green'>Bonjour IE3!</font></b>"
        # ajouter le text du message 
        self.label2.setText(message)
        # fixer la largeur de l'étiquette
        self.label2.setFixedWidth(120)
         # position de l'étiquette (x, y) en pixels
        self.label2.move(200, 10)
        
        # Ajouter des boutons: `QPushButton`
        # Push Button 1: Bouton bonjour
        button1 = QPushButton('Bonjour', self)
        button1.setToolTip("C'est le bouton Bonjour")
        button1.move(50, 50)
        # connecter le signal à l'événement
        button1.clicked.connect(self.on_click_button1)
        # Push Button 2: Bouton au revoir
        button2 = QPushButton('Au revoir', self)
        button2.setToolTip("C'est le bouton Au revoir")
        button2.move(170, 50)
        # connecter le signal à l'événement
        button2.clicked.connect(self.on_click_button2)

    @pyqtSlot()  # signal du bouton bonjour
    def on_click_button1(self):
        '''
        Afficher un message "Bonjour"
        '''
        message = "<h3><b><font color='green'>Bonjour IE3!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)

    @pyqtSlot()  # signal du bouton au revoir
    def on_click_button2(self):
        '''
        Afficher un message "Au revoir"
        '''
        message = "<h3><b><font color='red'>Au revoir IE3!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())