# Crie um programa para verificar o maior número entre três parâmetros
def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z