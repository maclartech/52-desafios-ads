# Precisei voltar a treinar lógica condicional, laços de repetição e manipulação de entrada/saída antes de mergulhar em estruturas mais complexas. 
# O desafio era criar uma calculadora de linha de comando que fosse além das quatro operações básicas, incluindo potenciação e resto da divisão,
# com um menu interativo que permitisse ao usuário realizar várias operações sem precisar reiniciar o programa a cada cálculo.


import os

def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b if b != 0 else None
def potencia(a, b):
    return a ** b
def modulo(a, b):
    return a % b if b != 0 else None