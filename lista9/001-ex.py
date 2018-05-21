import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

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
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = calcula_tamanho_medio_palavra(texto)
    ttr = calcula_relacao_type_token(texto)
    hlr = calcula_razao_hapax_legomana(texto)
    sal = calcula_tamanho_medio_sentenca(texto)
    sac = calcula_complexidade_media_sentenca(texto)
    pal = calcula_tamanho_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def cria_array_todas_as_frases(sentencas):
    frases = []
    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)

    return frases

def cria_array_todas_as_palavras(frases):
    palavras = []
    for frase in frases:
        palavras = palavras + separa_palavras(frase)

    return palavras

def test_calcula_relacao_type_token():
    assert calcula_relacao_type_token('O gato caçava o rato') == 0.8

def test_calcula_razao_hapax_legomana():
    assert calcula_razao_hapax_legomana('O gato caçava o rato') == 0.6

def calcula_tamanho_medio_palavra(texto):
    tamanhoPalavras = 0
    contaPalavras = 0

    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                tamanhoPalavras = tamanhoPalavras + len(palavra)
                contaPalavras = contaPalavras + 1

    return tamanhoPalavras / contaPalavras

def calcula_relacao_type_token(texto):
    sentencas = separa_sentencas(texto)
    frases = cria_array_todas_as_frases(sentencas)
    palavras = cria_array_todas_as_palavras(frases)

    numeroPalavrasDiferentes = n_palavras_diferentes(palavras)

    return numeroPalavrasDiferentes / len(palavras)

def calcula_razao_hapax_legomana(texto):
    sentencas = separa_sentencas(texto)
    frases = cria_array_todas_as_frases(sentencas)
    palavras = cria_array_todas_as_palavras(frases)

    numeroPalavrasUnicas = n_palavras_unicas(palavras)

    return numeroPalavrasUnicas / len(palavras)

def calcula_tamanho_medio_sentenca(texto):
    ''' Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças
        dividida pelo número de sentenças (os caracteres que separam uma sentença da outra
        não devem ser contabilizados como parte da sentença). '''
    sentencas = separa_sentencas(texto)
    tamanhoTotal = 0
    for sentenca in sentencas:
        tamanhoTotal = tamanhoTotal + len(sentenca)

    return tamanhoTotal / len(sentencas)

def calcula_complexidade_media_sentenca(texto):
    ''' Complexidade de sentença é o número total de frases divido pelo número de sentenças '''
    sentencas = separa_sentencas(texto)
    frases = cria_array_todas_as_frases(sentencas)

    return len(frases) / len(sentencas)

def calcula_tamanho_medio_frase(texto):
    ''' Tamanho médio de frase é a soma do número de caracteres em cada frase
        dividida pelo número de frases no texto '''
    return tamanhoFrases / len(frases)