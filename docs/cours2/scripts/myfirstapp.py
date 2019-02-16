# NOM DU FICHIER: myfirstapp.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QWidget
import sys
# créer un objet QApplication
app = QApplication(sys.argv)
# appeler la classe QWidgets
window = QWidget()
# définir les dimensions de la fenêtre
window.setGeometry(400, 100, 300, 200)
# définir un titre pour la fenêtre
window.setWindowTitle('My first app')
# afficher l'objet graphique dans l'application
window.show()
# fermer l'application
sys.exit(app.exec_())
