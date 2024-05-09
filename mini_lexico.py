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
            identificador = re.match(r"[a-zA-Z][a-zA-Z0-9]*", codigo[posicion:])
            if identificador:
                token_tipo = 0  # Tipo de identificador según la tabla
                tokens.append((token_tipo, identificador.group()))
                posicion += len(identificador.group())
            else:
                print("Error: Identificador no válido")
                return None

        # Números Enteros
        elif codigo[posicion].isdigit():
            entero = re.match(r"\d+", codigo[posicion:])
            if entero:
                token_tipo = 1  # Tipo de entero según la tabla
                tokens.append((token_tipo, int(entero.group())))
                posicion += len(entero.group())
            else:
                print("Error: Número entero no válido")
                return None

        # Números Reales
        elif codigo[posicion] == ".":
            decimal = re.match(r"\.\d+", codigo[posicion:])
            if decimal:
                posicion += len(decimal.group())
                entero = re.match(r"\d+", codigo[posicion:])
                if entero:
                    token_tipo = 2  # Tipo de real según la tabla
                    tokens.append((token_tipo, float("0" + decimal.group())))
                    posicion += len(entero.group())
                else:
                    print("Error: Número decimal no válido")
                    return None
            else:
                print("Error: Número decimal no válido")
                return None

        # Operadores, símbolos y palabras reservadas
        else:
            simbolo = codigo[posicion]
            token_tipo = None
            if simbolo in ["+", "-"]:
                token_tipo = 5  # opSuma
            elif simbolo in ["*", "/"]:
                token_tipo = 6  # opMul
            elif simbolo in ["<", "<=", ">", ">=", "!=", "=="]:
                token_tipo = 7  # opRelac
            elif simbolo == "&":
                token_tipo = 9  # opAnd
            elif simbolo == "|":
                token_tipo = 8  # opOr
            elif simbolo == "!":
                token_tipo = 10  # opNot
            elif simbolo == ";":
                token_tipo = 12
            elif simbolo == ",":
                token_tipo = 13
            elif simbolo == "(":
                token_tipo = 14
            elif simbolo == ")":
                token_tipo = 15
            elif simbolo == "{":
                token_tipo = 16
            elif simbolo == "}":
                token_tipo = 17
            elif simbolo == "=":
                token_tipo = 18
            else:
                # Revisar palabras reservadas
                for palabra_reservada in [
                    "if",
                    "while",
                    "return",
                    "else",
                    "int",
                    "float",
                ]:
                    if codigo[posicion:].startswith(palabra_reservada):
                        token_tipo = 19 + [
                            "if",
                            "while",
                            "return",
                            "else",
                            "int",
                            "float",
                        ].index(palabra_reservada)
                        posicion += len(palabra_reservada) - 1
                        break

            if token_tipo is not None:
                tokens.append((token_tipo, simbolo))
                posicion += 1
            else:
                print("Error: Símbolo no reconocido")
                return None

    return tokens


# Ejemplo de uso
codigo_de_prueba = """
int main() {
    int x = 42;
    int y = 31;
    if (x > 0) {
        return x;
    } else {
        return -x;
    }
}
"""
tokens_resultantes = analizador_lexico(codigo_de_prueba)

if tokens_resultantes:
    for token in tokens_resultantes:
        print(token)
