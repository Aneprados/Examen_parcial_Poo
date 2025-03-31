from Lanzador import crear_puntos, punto_mas_lejos_origen, imprimir_puntos, consultar_cuadrantes, consultar_vectores, consultar_distancias, consultar_rectangulo, Rectangulo




if __name__ == "__main__":
    # Crear los puntos
    A, B, C, D, O = crear_puntos()

    # Guardar los puntos en un diccionario
    puntos = {"A": A, "B": B, "C": C, "D": D}

    # Imprimir información de los puntos
    imprimir_puntos(puntos)
    consultar_cuadrantes({"A": A, "C": C, "D": D})
    consultar_vectores(A, B)
    consultar_distancias(A, B)
    punto_mas_lejos_origen({"A": A, "B": B, "C": C}, O)

    # Crear un rectángulo con los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar información del rectángulo
    consultar_rectangulo(rectangulo)
