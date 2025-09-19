"""
Integrantes
Carlos Osvaldo Díaz García

Fecha
18 de septiembre de 2025

Dados tres números, ordenarlos de mayor a menor.
"""

# Entradas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
numero_3 = float(input("Tercer número: "))

# Proceso
if numero_1 >= numero_2 and numero_1 >= numero_3:
    if numero_2 >= numero_3:
        # Salida
        print("Números ordenados", numero_1, numero_2, numero_3)
    else:
        # Salida
        print("Números ordenados", numero_1, numero_3, numero_2)

elif numero_2 >= numero_1 and numero_2 >= numero_3:
    if numero_1 >= numero_3:
        # Salida
        print("Números ordenados", numero_2, numero_1, numero_3)
    else:
        # Salida
        print("Números ordenados", numero_2, numero_3, numero_1)

else:
    if numero_1 >= numero_2:
        # Salida
        print("Números ordenados", numero_3, numero_1, numero_2)
    else:
        # Salida
        print("Números ordenados", numero_3, numero_2, numero_1)