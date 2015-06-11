# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelos')
from Auto import *


class MainController():

    def __init__(self, una_ventana):
        self.Auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.Auto.subirPersonas()
        self.actualizar_Label()

    def handler_bajar_persona(self):
        self.Auto.bajarPersonas()
        self.actualizar_Label()

    def actualizar_Label(self):
        self.ventana.label.setText(str(self.Auto.cantPersonas))
