# Crie um programa para receber uma sequência de inteiros e mostrar ao inverso
def soma_elementos():
    n = 0
    lista = []
    n = int(input('Digite um número: '))
    while n > 0:
        lista.append(n)
        n = int(input('Digite um número: '))
    return lista[::-1]

def inverte_elementos():
    lista = soma_elementos()
    for i in range(len(lista)):
        print(lista[i])

inverte_elementos()