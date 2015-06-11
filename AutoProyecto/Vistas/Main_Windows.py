# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from Main_Controller import *


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainController(self)
        self.init_ui()

    def init_ui(self):
        label = QtGui.QLabel('cantidad de personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(label)
        button_subir = QtGui.QPushButton('Subi ameo')
        button_bajar = QtGui.QPushButton('vagate o t vajo')
        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)

        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)

        self.setLayout(h_layout)
        self.setWindowTitle('Launcher Nid for zpid')
        self.setGeometry(200, 200, 200, 200)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())




