# NOM DU FICHIER: AnalogRead.py
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

print('#-----------------------------')
print("#  Lecture de l'entrée analogique A0 de l'Arduino ")
print('#-----------------------------')

while True:
    try:
        time.sleep(1)  # Pause d'une seconde avant la prochaine mesure
        print(pinA0.read())     # la valeur varie entre 0 et 1.    
        
    except KeyboardInterrupt:
          board.exit()
          break