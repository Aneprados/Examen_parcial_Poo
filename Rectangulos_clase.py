
from Clase_punto import Punto
class Rectangulo:
    def __init__(self, punto_inicial: Punto, punto_final: Punto):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def calcular_base(self):
        base = abs(self.punto_final.x - self.punto_inicial.x)
        return base

    def calcular_altura(self):
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return altura

    def calcular_area(self):
        base = self.calcular_base()  # Llamar al método calcular_base
        altura = self.calcular_altura()  # Llamar al método calcular_altura
        return base * altura

    def calcular_perimetro(self):
        base = self.calcular_base()
        altura = self.calcular_altura()
        return 2 * (base + altura)

    def __str__(self):
        return (f"Rectángulo definido por los puntos "
                f"({self.punto_inicial.x}, {self.punto_inicial.y}) y "
                f"({self.punto_final.x}, {self.punto_final.y})")


