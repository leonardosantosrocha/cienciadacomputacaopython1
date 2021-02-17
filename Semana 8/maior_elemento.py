# Crie um programa para mostrar o maior elemento de uma lista
def maior_elemento(lista):
    i = 1
    anterior = -1000
    for i in range(len(lista)):
        if lista[i] > anterior:
            anterior = lista[i]
    return anterior

lista = [-90, -27, -12]
lista = maior_elemento(lista)
print(lista)