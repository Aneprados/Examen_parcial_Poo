from Lanzador import (punto_mas_lejos_origen, imprimir_puntos, consultar_cuadrantes, consultar_vectores, consultar_distancias, consultar_rectangulo
)

if __name__ == "__main__":
    puntos = {"A": A, "B": B, "C": C, "D": D}
    imprimir_puntos(puntos)
    consultar_cuadrantes({"A": A, "C": C, "D": D})
    consultar_vectores(A, B)
    consultar_distancias(A, B)
    punto_mas_lejos_origen({"A": A, "B": B, "C": C}, D)
    rectangulo = Rectangulo(A, B)
    consultar_rectangulo(rectangulo)