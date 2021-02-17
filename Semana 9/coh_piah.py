import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Aplicando a comparação de assinaturas
    i = 0 # Base do somatório (0-5) para cada elemento linguístico
    comparacao = [] # Comparação para adicionar o resultado da diferença entre cada elemento línguistíco entre assinatura b e assinatura a
    while i < len(as_a): # Enquanto i (base) for menor que tamanho da assinatura as_a
        comparacao.append(abs(as_b[i] - as_a[i])) # Comparação recebe a diferença entre cada elemento linguístico dado por módulo (abs) as_b - as_a
        i +=1 # Incrementando
    comparacao = sum(comparacao) / 6 # Comparação valerá a soma de cada elemento linguístico dividido por seis (elementos linguísticos)
    return comparacao

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Tamanho médio da palavra (soma dos tamanhos das palavras dividida pelo número total de palavras)
    soma_tamanhos_palavras = 0
    numero_total_palavras = 0
    # Type Token (é o número de palavras diferentes dividido pelo número total de palavras)
    numero_palavras_diferentes = 0
    numero_total_palavras = 0
    # Hapax Legomana (é o número de palavras que aparecem uma única vez dividido pelo total de palavras)
    hapax_legomana = 0
    numero_palavras_unicas = 0
    numero_total_palavras = 0
    # Tamanho médio da sentença (é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças)
    tamanho_medio_sentenca = 0
    total_letras_sentenca = 0
    numero_total_sentencas = 0
    # Complexidade da sentença ( é o número total de frases divido pelo número de sentenças)
    complexidade_sentenca = 0
    numero_total_frases = 0
    # Tamanho médio da frase ( é a soma do número de caracteres em cada frase dividida pelo número de frases no texto)
    tamanho_medio_frase = 0 
    total_letras_frase = 0
    # Lista total de palavras
    lista_total_palavras = []
    
    lista_sentencas = separa_sentencas(texto)
    # Laço para percorrer sentenças
    for sentenca in lista_sentencas:
        numero_total_sentencas += 1 # Número total de sentenças
        total_letras_sentenca += len(sentenca) # Total de letras sentença
        lista_frases = separa_frases(sentenca) # Lista de frases

        # Laço para percorrer frases
        for frase in lista_frases:
            numero_total_frases += 1 # Número total de frases
            total_letras_frase += len(frase) # Total de letras frase
            lista_palavras = separa_palavras(frase) # Lista de palavras

            # Laço para percorrer palavras
            for palavra in lista_palavras:
                numero_total_palavras += 1 # Número total de palavras
                soma_tamanhos_palavras += len(palavra) # Total de letras das palavras
                lista_total_palavras.append(palavra) # Adicionando a palavra a lista total de palavras
    
    # Palavras diferentes
    numero_palavras_diferentes = n_palavras_diferentes(lista_total_palavras)

    # Palavras únicas
    numero_palavras_unicas = n_palavras_unicas(lista_total_palavras)

    # Saídas
    tamanho_medio_palavra = soma_tamanhos_palavras / numero_total_palavras         #print(f'Tamanho médio das palavras: {tamanho_medio_palavra}')
    type_token = numero_palavras_diferentes / numero_total_palavras                #print(f'Número palavras diferentes: {type_token}')
    hapax_legomana = numero_palavras_unicas / numero_total_palavras                #print(f'Número palavras únicas: {hapax_legomana}')
    tamanho_medio_sentenca = total_letras_sentenca / numero_total_sentencas        #print(f'Tamanho médio sentenças: {tamanho_medio_sentenca}')
    complexidade_sentenca = numero_total_frases / numero_total_sentencas           #print(f'Complexidade sentença: {complexidade_sentenca}')
    tamanho_medio_frase = total_letras_frase / numero_total_frases                 #print(f'Tamanho médio frases: {tamanho_medio_frase}')

    # Criando as_a (assinatura a)
    as_a = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
    
    # Retornando-a
    return as_a


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # Avaliação dos textos
    ass_original = ass_cp[0]

    # Encontrando a menor assinatura
    for i in range(len(ass_cp)):
        if ass_cp[i] < ass_original:
            ass_original = ass_cp[i]

    # Encontrando a posição da menor assinatura
    for j in range(len(ass_cp)):
        if ass_original == ass_cp[j]:
            texto = j
    
    return texto

# Start do programa
ass_b = le_assinatura()
textos = le_textos()

ass_cp = []

for autor in range(len(textos)):
    texto = textos[autor]
    ass_a = calcula_assinatura(texto)
    similaridade = compara_assinatura(ass_a, ass_b)
    ass_cp.append(similaridade)

autor = avalia_textos(textos, ass_cp)

print()
print('O autor do texto', autor, 'está infectado com COH-PIAH')