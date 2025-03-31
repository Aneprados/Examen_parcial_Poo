from Clase_punto import Punto
from Rectangulos_clase import Rectangulo
# Este código crea cuatro puntos y determina a qué cuadrante pertenecen, calcula vectores y distancias entre ellos,
#Crear los puntos A, B, C y D
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.base = abs(punto2.x - punto1.x)
        self.altura = abs(punto2.y - punto1.y)

    # Otros métodos de la clase
    def area(self):
        return self.base * self.altura
    
# Imprimir los puntos
print(f"Punto A: {A}")
print(f"Punto B: {B}")
print(f"Punto C: {C}")
print(f"Punto D: {D}")

# Consultar a qué cuadrante pertenecen los puntos
print(f"Cuadrante de A: {A.cuadrante()}")
print(f"Cuadrante de C: {C.cuadrante()}")
print(f"Cuadrante de D: {D.cuadrante()}")

# Consultar los vectores AB y BA
print(f"Vector AB: {A.vector(B)}")
print(f"Vector BA: {B.vector(A)}")

# Consultar la distancia entre los puntos A y B, y B y A
print(f"Distancia entre A y B: {A.distancia(B)}")
print(f"Distancia entre B y A: {B.distancia(A)}")

# Determinar cuál de los puntos A, B o C está más lejos del origen
distancias = {"A": A.distancia(D), "B": B.distancia(D), "C": C.distancia(D)}
punto_mas_lejos = max(distancias, key=distancias.get)
print(f"El punto más lejos del origen es: {punto_mas_lejos}")

# Crear un rectángulo utilizando los puntos A y B
rectangulo = Rectangulo(A, B)

# Consultar la base, altura y área del rectángulo
print(f"Base del rectángulo: {rectangulo.base}")
print(f"Altura del rectángulo: {rectangulo.altura}")
print(f"Área del rectángulo: {rectangulo.area()}")