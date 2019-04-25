# NOM DU FICHIER: AnalogReadPWM_RealTimePlot.py
#% IMPORTATION
import pyfirmata
import time
import matplotlib.pyplot as plt

port = 'COM3' #windows
#port = '/dev/ttyACM0'   #linux
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)  # itérateur permet de ne pas engorger 
                                     # la communication série
it.start()

pinA0 = board.get_pin('a:0:i')   # a = analogique, 0 = numéro de la pin, i = input.
LEDpin = board.get_pin('d:11:p') # d = digital, 11 = numÃ©ro de la pin, p = PWM

# Préparer la figure (matplotlib)
plt.ion() # Activer le mode interactif
fig = plt.figure() # créer une figure
pData = [0] * 25    # initiliser par une liste de 25 valeurs = 0
l1, = plt.plot(pData, "-r*") # tracer les pData initialement des 0
plt.ylim((-0.1, 1.1))
plt.grid()

i = 0
while True:
      try:
          time.sleep(1)
          valeur = pinA0.read()
          i +=1
          print("Temps = %s s; valeur = % s " %(i, valeur))
          
          pData.append(valeur) # ajouter la valeur à la fin de la liste
          del pData[0] # effacer le premier éliment de la liste 
          # update plot
          l1.set_xdata([i for i in range(25)])
          plt.pause(0.0001) # assurez-vous de faire une pause sinon il va planter
          l1.set_ydata(pData)
          plt.pause(0.0001) # assurez-vous de faire une pause sinon il va planter
          plt.title("Potentiomètre en temps réel (t = %s s)"%i)
          plt.draw()
          
          board.digital[LEDpin.pin_number].write(valeur)
          
      except KeyboardInterrupt:
          board.exit()
          break