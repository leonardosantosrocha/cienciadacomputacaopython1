# Crie um programa para mostra a tabuada de 1 a 10
linha = 1
coluna = 1
# Percorrendo cada linha
while linha <= 10:
    # Percorrendo cada coluna
    while coluna <= 10:
        # Resultado é linha vezes colunas (end é o espaçador)
        print(linha * coluna, end='\t')
        # Incrementando colunas
        coluna += 1
    # Incrementando linhas
    linha += 1
    print()
    # Resetando a coluna para calcular a nova linha
    coluna = 1