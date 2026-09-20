def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


OPERACIONES = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
}


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número.")


def main():
    print("=== Calculadora en Python ===")
    print("Operaciones disponibles: +  -  *  /")
    print("Escribe 'salir' para terminar.\n")

    while True:
        operador = input("Operación (+, -, *, /) o 'salir': ").strip()

        if operador.lower() == "salir":
            print("¡Hasta luego!")
            break

        if operador not in OPERACIONES:
            print("Operación no válida. Intenta de nuevo.\n")
            continue

        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        try:
            resultado = OPERACIONES[operador](a, b)
            print(f"Resultado: {a} {operador} {b} = {resultado}\n")
        except ValueError as error:
            print(f"Error: {error}\n")


if __name__ == "__main__":
    main()