# Crie um programa para definir se um número é primo
def ePrimo(n):
    i = 2
    # Verificando se o número é primo
    while i < n:
        if n % i != 0:
            i += 1
        else:
            return False
    if n == i:
        return True

print(ePrimo(13))