# NOM DU FICHIER:LEDSerial.py
#% IMPORTATION
import serial
# créer un objet de port série appelé Arduino_Serial
Arduino_Serial = serial.Serial('com12',9600)
# lire les données de série et l'afficher en ligne
print(Arduino_Serial.readline())
print("Entrez 1 pour allumée la LED et 0 pour l'éteindre")

# boucle infinie
while 1:
    # attend que l'utilisateur entre les données                                 
    input_data = input()
    # affiche les données pour confirmation
    print ("you entered", input_data)
    # si la donnée entrée est 1
    if (input_data == '1'):
        # envoyer 1 à arduino               
        Arduino_Serial.write('1')
        print("LED ON")

    # si la donnée entrée est 0
    if (input_data == '0'):    
        # envoyer 0 à arduino                
        Arduino_Serial.write('0')
        print("LED OFF")