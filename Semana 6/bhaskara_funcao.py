# Crie um programa para calcular as raizes da fórmula de bhaskara
import math

def delta(a, b, c):
    delta = b ** 2 - 4 * a * c 
    return delta

def calcula_raizes(a, b, c):
    d = delta(a, b, c)
    x1 = ((-b + math.sqrt(d)) / (2 * a))
    x2 = ((-b - math.sqrt(d)) / (2 * a))
    return x1, x2

def raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return 'As raizes não possuem valores reais!'
    if d == 0:
        return f'Delta igual à zero gera apenas uma raiz: {calcula_raizes(a, b, c)}'
    if d > 0:
        return f'As raizes reais são: {calcula_raizes(a, b, c)}'

def main():
    again = 'S'
    while again == 'S':    
        a = int(input('A: '))
        b = int(input('B: '))
        c = int(input('C: '))
        print(raizes(a, b, c))
        print()
        again = input('Realizar um novo cálculo (S/N): ')
        print()

main()