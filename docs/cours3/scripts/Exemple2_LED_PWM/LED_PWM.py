# NOM DU FICHIER:LED_PWM.py
#% IMPORTATION
import pyfirmata
port = 'COM3'            #windows
#port = '/dev/ttyACM0'   #linux
 
board = pyfirmata.Arduino(port)

LEDpin = board.get_pin('d:11:p') ## d = digital, 11 = numéro de la pin, p = PWM

print("-------------- CONTROLE DE LEDS ----------------")
print("En tout temps, vous pouvez quitter le programme en répondant par 'q'.")

while True:  
    print("Luminosité désirée pour la LED:")
    luminosite = input("De 0 à 100 (ou q):  ")
    if (luminosite == 'q'):
        board.exit();
        print("Au revoir!")
        break;
    
    board.digital[LEDpin.pin_number].write(float(luminosite)/100.0)