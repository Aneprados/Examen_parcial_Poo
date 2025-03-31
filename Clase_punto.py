import math

class Punto:
    def __init__(self, x=0, y=0):
        """Constructor para inicializar las coordenadas del punto."""
        self.x = x
        self.y = y

    def __str__(self):
        """Sobreescribe el método string para mostrar el punto en formato (X, Y)."""
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        """
        Determina a qué cuadrante pertenece el punto.
        """
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"

    def vector(self, otro_punto):
        """
        Calcula el vector resultante entre el punto actual y otro punto.
        :param otro_punto: Instancia de la clase Punto.
        :return: Una tupla representando el vector (dx, dy).
        """
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return (dx, dy)

    def distancia(self, otro_punto):
        """
        Calcula la distancia entre el punto actual y otro punto.
        :param otro_punto: Instancia de la clase Punto.
        :return: La distancia entre los dos puntos.
        """
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
