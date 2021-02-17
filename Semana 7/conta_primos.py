# Crie um programa que conte o número de números primos a partir de 2 até N, incluindo N, caso seja primo
def ePrimo(n):
    i = 2
    while i < n:
        if n % i != 0:
            i += 1
        else:
            return False
    if n == i:
        return True

def n_primos(n):
    i = 2
    qtd = 0
    while i < n:
        if ePrimo(i) == True:
            qtd += 1
            i += 1
        else:
            i += 1
    return qtd