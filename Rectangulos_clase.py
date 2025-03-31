import math
from Clase_punto import Punto

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        """
        Constructor para inicializar el rectángulo con dos puntos.
        Si no se envían puntos, se crean en el origen por defecto.
        """
        self.punto_inicial = punto_inicial if punto_inicial else Punto()
        self.punto_final = punto_final if punto_final else Punto()

    def base(self):
        """
        Calcula la base del rectángulo.
        :return: La longitud de la base.
        """
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        """
        Calcula la altura del rectángulo.
        :return: La longitud de la altura.
        """
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        """
        Calcula el área del rectángulo.
        :return: El área del rectángulo.
        """
        return self.base() * self.altura()