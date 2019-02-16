# NOM DU FICHIER: myfirstappLabels.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

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
        label1 = QLabel('Ma première application affiche: ', self)
        # fixer la largeur de l'étiquette
        label1.setFixedWidth(160)
        # position de l'étiquette (x, y) en pixels
        label1.move(10, 10)
        ## Label 2: Texte riche
        label2 = QLabel("", self)
        # créer un message HTML
        message = "<h3><b><font color='green'>Bonjour IE3!</font></b>"
        # ajouter le text du message 
        label2.setText(message)
        # fixer la largeur de l'étiquette
        label2.setFixedWidth(120)
         # position de l'étiquette (x, y) en pixels
        label2.move(200, 10)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())
