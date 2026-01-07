"""
Programa: Conversor de Temperatura
Descripción:
Convierte una temperatura ingresada en grados Celsius a Fahrenheit.
"""

def convertir_celsius_a_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit


def main():
    nombre_usuario = input("Ingrese su nombre: ")
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

    conversion_exitosa = True
    resultado_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

    if conversion_exitosa:
        print("Hola,", nombre_usuario)
        print("Temperatura en Fahrenheit:", resultado_fahrenheit)
    else:
        print("Error en la conversión.")


main()
