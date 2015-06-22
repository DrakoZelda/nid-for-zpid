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

    def handler_bajar_persona5(self):
        i = 1
        while i <= 5:
            i += 1
            self.handler_bajar_persona()

    def handler_subir_persona5(self):
        i = 1
        while i <= 5:
            i += 1
            self.handler_subir_persona()

    def actualizar_Label(self):
        self.ventana.label.setText(str(self.Auto.cantPersonas))
