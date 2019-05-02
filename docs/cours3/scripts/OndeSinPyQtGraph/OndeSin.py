## NOM DU PROGRAMME: OndeSin.py
#% IMPORTATION
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot, QTimer
from UiOndeSin import Ui_MainWindow

import numpy as np
import pyqtgraph
import time


class OndeSin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.update()
        
    def update(self):
        t1=time.clock()
        points=100 #number of data points
        X=np.arange(points)
        Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
        C=pyqtgraph.hsvColor(time.time()/5%1,alpha=.5)
        pen=pyqtgraph.mkPen(color=C,width=3)
        self.grPlot.plot(X,Y,pen=pen,clear=True)
        print("update took %.02f ms"%((time.clock()-t1)*1000))
        if self.cb.isChecked():
            QTimer.singleShot(1, self.update) # QUICKLY repeat
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
        