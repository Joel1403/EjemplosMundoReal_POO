"""
Ejercicio de Programación Orientada a Objetos (POO) en Python
Sistema de Vehículos

Este programa cumple con:
- Clase base y clase derivada (herencia)
- Encapsulación
- Polimorfismo
- Definición correcta de atributos y métodos
- Creación de instancias
- Código comentado
"""

# ===============================
# CLASE BASE
# ===============================

class Vehiculo:
    """
    Clase base Vehiculo
    Aplica encapsulación y sirve como base para la herencia
    """

    def __init__(self, marca, velocidad):
        # Atributos privados (encapsulación)
        self.__marca = marca
        self.__velocidad = velocidad

    # Métodos getters (encapsulación)
    def get_marca(self):
        return self.__marca

    def get_velocidad(self):
        return self.__velocidad

    # Método que será sobrescrito (polimorfismo)
    def descripcion(self):
        return f"Vehículo marca {self.__marca} con velocidad {self.__velocidad} km/h"


# ===============================
# CLASE DERIVADA
# ===============================

class Auto(Vehiculo):
    """
    Clase Auto
    Hereda de Vehiculo y sobrescribe un método (polimorfismo)
    """

    def __init__(self, marca, velocidad, puertas):
        super().__init__(marca, velocidad)
        self.puertas = puertas

    # Método sobrescrito (polimorfismo)
    def descripcion(self):
        return (
            f"Auto marca {self.get_marca()}, "
            f"{self.puertas} puertas, "
            f"velocidad máxima {self.get_velocidad()} km/h"
        )


# ===============================
# SERVICIO / LÓGICA DEL SISTEMA
# ===============================

def mostrar_vehiculos(lista_vehiculos):
    """
    Demuestra polimorfismo al tratar objetos distintos de igual forma
    """
    for vehiculo in lista_vehiculos:
        print(vehiculo.descripcion())


# ===============================
# FUNCIÓN PRINCIPAL
# ===============================

def main():
    # Creación de instancias
    vehiculo1 = Vehiculo("Yamaha", 120)
    auto1 = Auto("Toyota", 180, 4)

    # Lista con objetos de diferentes clases
    vehiculos = [vehiculo1, auto1]

    # Ejecución del sistema
    mostrar_vehiculos(vehiculos)


if __name__ == "__main__":
    main()
