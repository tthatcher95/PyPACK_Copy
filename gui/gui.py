import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenu, QAction, QVBoxLayout, QSizePolicy,
                            QMessageBox, QWidget, QPushButton, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

import libpypack
import pandas as pd
from libpypack import locations
from libpypack.visualization import generate_maps

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('File Path:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        pybutton = QPushButton('Run', self)
        pybutton.clicked.connect(lambda: PlotCanvas(self, width=5, height=4))
        pybutton.resize(200,32)
        pybutton.move(80, 60)
        self.show()
        
        menubar = self.menuBar()
        locMenu = menubar.addMenu('Locations')
        visMenu = menubar.addMenu('Visualization')

        self.impMenu = QMenu('Parse Locations')
        self.impAct = QAction('Run Mordecai')
        self.impMenu.addAction(self.impAct)
        self.impAct.triggered.connect(self.print_something)

        self.genMenu = QMenu('Generate Visuals')
        self.heatAct = QAction('Heatmap')
        self.choroAct = QAction('Choropleth')

        self.genMenu.addAction(self.choroAct)
        self.genMenu.addAction(self.heatAct)

        self.choroAct.triggered.connect(self.print_something)
        self.heatAct.triggered.connect(self.print_something)


        locMenu.addMenu(self.impMenu)
        visMenu.addMenu(self.genMenu)

        # self.setGeometry(self.left, self.top, self.width, self.height)
        #
        # button = QPushButton('PyQt5 button', self)
        # button.setToolTip('This s an example button')
        # button.move(500,0)
        # button.resize(140,100)

    def print_something(self):
        print("Hey it worked!")

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
