__version__ = "0.1.0"
__author__ = "Davi"
"""
Este programa imprime a tabuada de 1 a 10.
"""
numeros = list(range(1, 11))

for numero in numeros:
    print(f"Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-" * 20)
