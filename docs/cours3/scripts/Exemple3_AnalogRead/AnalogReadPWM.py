# NOM DU FICHIER: AnalogReadPWM.py
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
LEDpin = board.get_pin('d:11:p') # d = digital, 11 = numÃ©ro de la pin, p = PWM

print('#-----------------------------')
print("#  Lecture de l'entrée analogique A0 de l'Arduino ")
print('#-----------------------------')

while True:
    try:
        time.sleep(1)  # Pause d'une seconde avant la prochaine mesure
        valeur = pinA0.read()     # la valeur varie entre 0 et 1.
        print(valeur)
        board.digital[LEDpin.pin_number].write(valeur)
        
    except KeyboardInterrupt:
          board.exit()
          break