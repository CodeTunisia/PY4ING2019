# NOM DU FICHIER: LEDBlink.py
#% IMPORTATION
import pyfirmata
PIN = 13 # Pin 13 est utilisé
DELAY = 2 # Un délai de 2 secondes
# Vérifiez que le port correspond à votre système, voir exemples ci-dessous:
# Sur Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# Sous Windows: 'COM1', 'COM2', 'COM3'
PORT = 'COM3'
# Creates a new board 
board = pyfirmata.Arduino(PORT)
# Boucle pour clignoter la LED
while True:
    board.digital[PIN].write(1) # Set the LED pin to 1 (HIGH)
    print("LED ON")
    board.pass_time(DELAY)
    board.digital[PIN].write(0) # Set the LED pin to 0 (LOW)
    print("LED OFF")
    board.pass_time(DELAY)