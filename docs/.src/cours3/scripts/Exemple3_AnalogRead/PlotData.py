# NOM DU FICHIER: PlotData.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt

pData = np.loadtxt("Data.txt", comments = "#")
                   
fig = plt.figure()
plt.plot(pData, "-r*")
plt.xlabel("Temps [s]")
plt.ylabel("Valeurs du potentiomètre")
plt.grid()
plt.show()