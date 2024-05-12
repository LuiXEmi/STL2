def parse_sentence(sentence):
    # Dividimos la sentencia en tokens
    tokens = sentence.split("+")

    # Comprobamos si hay dos tokens y si ambos son variables
    if len(tokens) == 2 and all(token.strip().isalpha() for token in tokens):
        print("La sentencia es válida.")
    else:
        print("La sentencia no coincide con la gramática.")


# Ejemplo de uso
sentence = "hola + mundo"
parse_sentence(sentence)
