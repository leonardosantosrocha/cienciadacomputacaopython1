# Crie uma função que devolva a soma dos números inteiros de uma lista
def soma_elementos(lista):
    i = 1
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = soma_elementos(lista)
print(lista)