from Clase_punto import Punto
from Rectangulos_clase import Rectangulo
# Este código crea cuatro puntos y determina a qué cuadrante pertenecen, calcula vectores y distancias entre ellos,
#Crear los puntos A, B, C y D
def crear_puntos():
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)
    O = Punto()
    return A, B, C, D, O

# Imprimir los puntos
def imprimir_puntos(puntos):
    for nombre, punto in puntos.items():
        print(f"Punto {nombre}: {punto}")

def consultar_cuadrantes(puntos):
    for nombre, punto in puntos.items():
        print(f"Cuadrante de {nombre}: {punto.cuadrante()}")

def consultar_vectores(punto1, punto2):
    print(f"Vector {punto1} a {punto2}: {punto1.vector(punto2)}")
    print(f"Vector {punto2} a {punto1}: {punto2.vector(punto1)}")

def consultar_distancias(punto1, punto2):
    print(f"Distancia entre {punto1} y {punto2}: {punto1.distancia(punto2)}")
    print(f"Distancia entre {punto2} y {punto1}: {punto2.distancia(punto1)}")

def punto_mas_lejos_origen(puntos, origen):
    distancias = {nombre: punto.distancia(origen) for nombre, punto in puntos.items()}
    punto_mas_lejos = max(distancias, key=distancias.get)
    print(f"El punto más lejos del origen es: {punto_mas_lejos}")

# Crear el rectángulo correctamente


# Ahora sí, pasar el objeto rectángulo a la función


def consultar_rectangulo(rectangulo):
    print(f"Base del rectángulo: {rectangulo.calcular_base()}")
    print(f"Altura del rectángulo: {rectangulo.calcular_altura()}")
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

def lanzado():
    # Crear los puntos
    A, B, C, D, O = crear_puntos()

    # Guardar los puntos en un diccionario
    puntos = {"A": A, "B": B, "C": C, "D": D}

    # Imprimir información de los puntos
    imprimir_puntos(puntos)
    consultar_cuadrantes(puntos)
    consultar_vectores(A, B)
    consultar_distancias(A, B)
    punto_mas_lejos_origen(puntos, O)

    # Crear un rectángulo con los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar información del rectángulo
    consultar_rectangulo(rectangulo)
