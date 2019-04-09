## NOM DU PROGRAMME: UI2PYconverter.py
#% IMPORTATION
from PyQt5 import uic
# Le module uic de PyQt5, convertit un fichier ui (code XML)
# en un fichier py (code Python)
fin = open('UiMyAppLED.ui', 'r')
fout = open('UiMyAppLED.py', 'w')
uic.compileUi(fin, fout, execute=True)
fin.close()
fout.close()