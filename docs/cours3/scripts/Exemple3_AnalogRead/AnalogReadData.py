# NOM DU FICHIER: AnalogReadData.py
#% IMPORTATION
import pyfirmata
import time
port = 'COM3' #windows
#port = '/dev/ttyACM0'   #linux
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)  # itérateur permet de ne pas engorger 
                                     # la communication série
it.start()

pinA0 = board.get_pin('a:0:i')   # a = analogique, 0 = numéro de la pin, i = input.

# Nom du fichier à écrire
filename = "Data.txt"
# Ouvrir le fichier avec une permission d'écriture
myfile = open(filename, 'w')
# Ecrire une ligne dans le fichier
myfile.write("#  Lecture de l'entrée analogique A0 de l'Arduino \n")
             
while True:
    try:
        time.sleep(1)  # Pause d'une seconde avant la prochaine mesure
        valeur = pinA0.read()     # la valeur varie entre 0 et 1.
        print(valeur)
        myfile.write(str(valeur) + "\n") # écrire la valeur dans le fichier
                                         # et retourner à la nouvelle ligne
    except KeyboardInterrupt:
          board.exit()
          myfile.close()
          
          break