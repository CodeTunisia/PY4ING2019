## NOM DU PROGRAMME: OndeSin.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot, QTimer
from UiOndeSin import Ui_MainWindow

import numpy as np
import pylab
import time


class OndeSin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.update()
        
    def update(self):
            t1=time.time()
            points=100 #number of data points
            X=np.arange(points)
            Y=np.sin(X/points*3*np.pi+time.time())
            C=pylab.cm.jet(time.time()%10/10) # random color
            plt= self.mpl.canvas
            plt.ax.clear() #clear on plot()
            plt.ax.plot(X,Y,ms=100,color=C,lw=3,alpha=.8)
            plt.ax.get_figure().tight_layout() # fill space
            plt.draw() # required to update the window
            print("mise à jour a pris %.02f ms"%((time.time()-t1)*1000))
#            print((time.time()-t1)*1000)
            if self.cb.isChecked():
                QTimer.singleShot(10, self.update) # QUICKLY repeat
                # QTimer.singleShot (int msec, QObject receiver, object member)
                
    @pyqtSlot()  # btn update
    def on_btn_clicked(self):
        self.update()
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Myapplication = OndeSin()
    Myapplication.show()
    sys.exit(app.exec_())
        