
from Clase_punto import Punto


class Rectangulo:
    def __init__(self, punto_inicial: Punto, punto_final: Punto):
        """
        Constructor para crear un rectángulo con los puntos inicial y final.
        :param punto_inicial: Punto inicial (esquina inferior izquierda del rectángulo).
        :param punto_final: Punto final (esquina superior derecha del rectángulo).
        """
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def calcular_base(self):
        """
        Calcula la base del rectángulo.
        :return: La longitud de la base.
        """
        base = abs(self.punto_final.x - self.punto_inicial.x)
        return base

    def calcular_altura(self):
        """
        Calcula la altura del rectángulo.
        :return: La longitud de la altura.
        """
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return altura

    def calcular_area(self, base, altura):
        """
        Calcula el área del rectángulo.
        :param base: La longitud de la base del rectángulo.
        :param altura: La longitud de la altura del rectángulo.
        :return: El área del rectángulo.
        """
        return base * altura

    def calcular_perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        :return: El perímetro del rectángulo.
        """
        base = self.calcular_base()
        altura = self.calcular_altura()
        return 2 * (base + altura)

    def __str__(self):
        """
        Representación en cadena del rectángulo.
        :return: Una cadena con la información de los puntos que definen el rectángulo.
        """
        return (f"Rectángulo definido por los puntos "
                f"({self.punto_inicial.x}, {self.punto_inicial.y}) y "
                f"({self.punto_final.x}, {self.punto_final.y})")
