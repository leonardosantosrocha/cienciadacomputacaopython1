# Crie um programa para calcular o perimetro e prenchê-la com hashtags
def perimetro():
    i = j = 1
    largura = int(input('digite a largura: '))
    altura = int(input('digite a altura: '))
    while i <= largura:
        while j <= altura:
            if j == 1:
                print(largura * '#')
            elif j > 1 and j < altura:
                print('#' + (' ' * (largura - 2)) + '#')
            elif j == altura:
                print(largura * '#')
            j += 1
        i += 1
    
perimetro()