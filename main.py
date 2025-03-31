from Lanzador import (punto_mas_lejos_origen, imprimir_puntos, consultar_cuadrantes, consultar_vectores, consultar_distancias, consultar_rectangulo
)


if __name__ == "__main__":
    # Crear los puntos
    A, B, C, D, O = crear_puntos()

    # Imprimir los puntos
    imprimir_puntos(A, B, C, D)

    # Consultar los cuadrantes de los puntos A, C y D
    consultar_cuadrantes(A, C, D)

    # Consultar los vectores AB y BA
    consultar_vectores(A, B)

    # Consultar las distancias y determinar el punto más lejano del origen
    consultar_distancias(A, B, C, O)

    # Crear el rectángulo con los puntos A y B
    consultar_rectangulo (A, B)

    punto_mas_lejos_origen(A, B, C, O)
     
    