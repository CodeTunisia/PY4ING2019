# NOM DU FICHIER: myfirstapp_structure.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow

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
        # Propriétés de l'interface graphique
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())