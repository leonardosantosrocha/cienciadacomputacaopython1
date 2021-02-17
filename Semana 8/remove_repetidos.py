# Crie uma função que remove os itens repetidos de uma lista
def remove_repetidos(lista):
    i = 1
    aux = []
    for i in range(0, len(lista)):
        if lista[i] not in aux:
            aux.append(lista[i])
    i += 1
    return sorted(aux)

lista = [1, 1, 1, 2, 2, 2, 3, 3, 3]
lista = remove_repetidos(lista)
print(lista)