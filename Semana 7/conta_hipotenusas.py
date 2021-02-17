# Crie um programa para somar as hipotenusas
def é_hipotenusa(n):
    i = 0
    j = 0
    aux = []
    hipotenusa = False
    for i in range(n):
        for j in range(n):
            if ((((i ** 2) + (j** 2)) == n)):
                aux.append(i)
            if len(aux) > 0:
                hipotenusa = True
    return hipotenusa, aux

print(é_hipotenusa(25))
