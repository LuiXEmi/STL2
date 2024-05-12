import re


def main():
    # Definir las variables para llevar un seguimiento de los tipos de datos
    variables = {}

    # Definir las funciones permitidas y sus tipos de retorno
    funciones = {"suma": "int"}

    # Expresión regular para encontrar declaraciones de variables
    regex_variable = r"\b(int|float)\s+(\w+)\s*;"

    # Expresión regular para encontrar asignaciones de variables
    regex_asignacion = r"(\w+)\s*=\s*([\w\(\),\+\-\*\/]+)\s*;"

    # Expresión regular para encontrar llamadas a funciones
    regex_llamada_funcion = r"(\w+)\s*=\s*(\w+)\s*\(([^\)]*)\)\s*;"

    # Código a analizar
    codigo = """
    int main(){
        float a;
        int b;
        int c;
    }
    """

    # Analizar las declaraciones de variables
    variables_declaradas = re.findall(regex_variable, codigo)
    for tipo, nombre in variables_declaradas:
        variables[nombre] = tipo

    # Analizar las asignaciones y llamadas a funciones
    asignaciones_llamadas = re.findall(
        regex_asignacion + "|" + regex_llamada_funcion, codigo
    )
    for result in asignaciones_llamadas:
        if len(result) == 2:  # Si es una asignación
            variable, expresion = result
            # Analizar asignaciones
            tipo_variable = variables.get(variable)
            if tipo_variable is None:
                raise Exception(f"Error semántico: Variable '{variable}' no declarada.")
            if not validar_expresion(tipo_variable, expresion, variables):
                raise Exception(
                    f"Error semántico: Asignación no válida para la variable '{variable}'."
                )
        else:  # Si es una llamada a función
            variable = result[0]
            nombre_funcion, argumentos = result[1], result[2]
            # Analizar llamadas a funciones
            if nombre_funcion not in funciones:
                raise Exception(
                    f"Error semántico: Función '{nombre_funcion}' no definida."
                )
            tipo_retorno = funciones[nombre_funcion]
            if not validar_argumentos(argumentos.split(","), variables):
                raise Exception(
                    f"Error semántico: Argumentos inválidos para la función '{nombre_funcion}'."
                )

    print("El código ha pasado la validación semántica.")


def validar_expresion(tipo_variable, expresion, variables):
    # Validar que la expresión sea válida para el tipo de variable dado
    # En este ejemplo, simplemente verificamos que todas las variables en la expresión
    # estén declaradas y tengan el mismo tipo que la variable a la que se asigna.
    if expresion.replace(" ", "").isalpha():
        if expresion not in variables:
            return False
        return True
    elif expresion.replace(" ", "").isalnum():
        return True
    else:
        variables_expresion = re.findall(r"\b\w+\b", expresion)
        for variable in variables_expresion:
            tipo_variable_expresion = variables.get(variable)
            if tipo_variable_expresion is None:
                return False
            if tipo_variable_expresion != tipo_variable:
                return False
        return True


def validar_argumentos(argumentos, variables):
    # Validar que los argumentos sean válidos para la función dada
    # En este ejemplo, simplemente verificamos que todas las variables en los argumentos
    # estén declaradas y tengan un tipo compatible con el tipo de argumento esperado.
    for argumento in argumentos:
        tipo_argumento = variables.get(argumento.strip())
        if tipo_argumento is None:
            return False
    return True


main()
