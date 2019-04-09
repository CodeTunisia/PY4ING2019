import serial

ser = serial.Serial('/dev/ttyACM0', 9600) # sur Linux
# ser = serial.Serial('COM3', 9600) # sur Windows
while True:
    ligne = ser.readline()
    print('Valeur:', ligne)