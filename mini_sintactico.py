def analizar_cadena(cadena):
    tabla_lr1 = {
        (0, "id"): "d2",
        (0, "E"): "1",
        (1, "$"): "r0(accept)",
        (2, "+"): "d3",
        (3, "id"): "d4",
        (4, "$"): "r1",
    }

    pila = [0]
    cadena += "$"  # Agregar el marcador de final de entrada
    indice = 0

    while True:
        estado_actual = pila[-1]
        simbolo_actual = cadena[indice]

        accion = tabla_lr1.get((estado_actual, simbolo_actual))

        if accion is None:
            print(
                "Error: No se encontró una acción para el estado {} y el símbolo {}".format(
                    estado_actual, simbolo_actual
                )
            )
            return False

        if accion.startswith("r"):
            regla, _ = accion.split(
                "("
            )  # Separar el número de regla del resto de la cadena
            regla = int(regla[1:])  # Obtener el número de regla como un entero
            if regla == 0 or regla == 1:
                print("Reducción: E -> id + id")
                for _ in range(3):
                    pila.pop()
                estado_anterior = pila[-1]  # Estado anterior antes de la reducción
                simbolo_anterior = pila[-2]  # Símbolo anterior antes de la reducción
                nuevo_estado = int(tabla_lr1[(estado_anterior, "E")])
                pila.append("E")
                pila.append(nuevo_estado)
                print("Ir a: {} -> {}".format(estado_anterior, nuevo_estado))
                if pila[-3:] == [
                    "id",
                    "+",
                    "id",
                ]:  # Verificar si la producción es 'id + id'
                    print("La cadena es válida.")
                    return True
            else:
                print("Error: Reducción no válida")
                return False
        elif accion.startswith("d"):
            nuevo_estado = int(accion[1:])
            pila.append(simbolo_actual)
            pila.append(nuevo_estado)
            indice += 1
            print("Desplazamiento: {} -> {}".format(estado_actual, nuevo_estado))
        else:
            print("Error: Acción no válida")
            return False


# Ejemplo de uso
cadena_prueba = "a+b"
analizar_cadena(cadena_prueba)
