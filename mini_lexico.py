import re

def analizador_lexico(codigo):
    tokens = []
    posicion = 0

    while posicion < len(codigo):
        # Ignorar espacios en blanco
        if codigo[posicion].isspace():
            posicion += 1
            continue

        # Identificadores
        if codigo[posicion].isalpha():
            identificador = re.match(r'[a-zA-Z][a-zA-Z0-9]*', codigo[posicion:])
            if identificador:
                tokens.append(('IDENTIFICADOR', identificador.group()))
                posicion += len(identificador.group())
            else:
                print("Error: Identificador no válido")
                return None

        # Números Reales
        elif codigo[posicion].isdigit():
            entero = re.match(r'\d+', codigo[posicion:])
            if entero:
                posicion += len(entero.group())
                if posicion < len(codigo) and codigo[posicion] == '.':
                    posicion += 1
                    decimal = re.match(r'\d+', codigo[posicion:])
                    if decimal:
                        posicion += len(decimal.group())
                        tokens.append(('REAL', float(entero.group() + '.' + decimal.group())))
                    else:
                        print("Error: Número decimal no válido")
                        return None
                else:
                    tokens.append(('REAL', int(entero.group())))
            else:
                print("Error: Número entero no válido")
                return None

        # Otros caracteres no reconocidos
        else:
            print("Error: Carácter no reconocido")
            return None

    return tokens

# Ejemplo de uso
codigo_de_prueba = "variable123 42 3.14"
tokens_resultantes = analizador_lexico(codigo_de_prueba)

if tokens_resultantes:
    for token in tokens_resultantes:
        print(token)
