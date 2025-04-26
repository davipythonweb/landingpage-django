#! /usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Davi Nascimento"

"""
Funcionamentos :

[operacao] [n1] [n2]

Operaçoes:

sum -> soma
sub -> subtração
mul -> multiplicação
div -> divisão

Uso:

exemplo de uso1:
$ infixcalc.py sum 5 4
9

exemplo de uso2:
$ infixcalc.py sub 5 4
1

exemplo de uso3:
$ infixcalc.py mul 5 4
20

exemplo de uso4:
$ infixcalc.py div 5 4
1.25

exemplo de uso5:
$ infixcalc.py
operaçao: sum
n1: 5
n2: 4

resultado=9


"""



import sys

arguments = sys.argv[1:]

# TODO: Exceptions
if not arguments:
    operation = input("operation: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Invalid number of arguments")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Invalid invalid")
    print(valid_operations)
    sys.exit(1)

valid_nums = []

for num in nums:
    # TODO: Repetiçao while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Invalid number: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

n1, n2 = valid_nums

# TODO: Usar dict de funcoes


if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"The result is: {result}")

