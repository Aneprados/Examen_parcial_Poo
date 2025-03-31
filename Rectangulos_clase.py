import math
from Clase_punto import Punto

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        
        self.punto_inicial = punto_inicial if punto_inicial else Punto()
        self.punto_final = punto_final if punto_final else Punto()

    def base(self):
        
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        
        return self.base() * self.altura()

    @classmethod
    def perimetro(cls, punto_inicial, punto_final):
        
        rect = cls(punto_inicial, punto_final)
        return 2 * (rect.base() + rect.altura())
    
    def __str__(self):
        """
        Sobreescribe el método string para mostrar el rectángulo en formato (Punto inicial, Punto final).
        """
        return f"Rectángulo: ({self.punto_inicial}, {self.punto_final})"

    def crear_con_puntos(cls, punto_inicial=None, punto_final=None):
            """
            Método de clase para crear un rectángulo a partir de dos puntos.
            :param punto_inicial: Instancia de la clase Punto.
            :param punto_final: Instancia de la clase Punto.
            :return: Una instancia de Rectangulo.
            """
            return cls(punto_inicial, punto_final)
    def crear_con_puntos(cls, x1=0, y1=0, x2=0, y2=0):
            """
            Método de clase para crear un rectángulo a partir de coordenadas.
            Si no se reciben coordenadas, se inicializan en cero.
            :param x1: Coordenada x del punto inicial.
            :param y1: Coordenada y del punto inicial.
            :param x2: Coordenada x del punto final.
            :param y2: Coordenada y del punto final.
            :return: Una instancia de Rectangulo.
            """
            punto_inicial = Punto(x1, y1)
            punto_final = Punto(x2, y2)
            return cls(punto_inicial, punto_final)
    
def crear_con_puntos(cls, punto1, punto2):

    def __init__(self, punto1, punto2):
        self.base = abs(punto2.x - punto1.x)
        self.altura = abs(punto2.y - punto1.y)

    # Otros métodos de la clase
    def area(self):
        return self.base * self.altura