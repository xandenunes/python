import re
def relacao_type_token(texto):
    total_palavras = lista_palavras(texto)
    palavras_dif = n_palavras_diferentes(total_palavras)
    return palavras_dif/len(total_palavras)
def tamanho_medio_palavra(lista_palavras):
    tamanho_medio = 0
    quantidade_palavras = 0
    for i in lista_palavras:
        tamanho_medio += len(i)
        quantidade_palavras += 1
    return tamanho_medio/quantidade_palavras
def lista_palavras(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    for i in sentencas:
        frases += separa_frases(i)
    palavras = []
    for i in frases:
        palavras += separa_palavras(i)
    return palavras
def hapax_legomana(texto):
    total_palavras = lista_palavras(texto)
    palavras_unicas = n_palavras_unicas(total_palavras)

    return palavras_unicas/len(total_palavras)
def lista_frase(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    for i in sentencas:
        frases += separa_frases(i)
    return frases
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
def tamanho_medio_frase(texto):
    caracteres_frase = 0
    lst_frase = lista_frase(texto)
    for i in lst_frase:
        caracteres_frase += len(i)
    return caracteres_frase/len(lst_frase)
def tamanho_medio_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    caracteres_sentencas = 0
    for i in lista_sentencas:
        caracteres_sentencas += len(i)
    return caracteres_sentencas/len(lista_sentencas)
def complexidade_sentenca(texto):
    sentencas = separa_sentencas(texto)
    frases = lista_frase(texto)
    return len(frases)/len(sentencas)
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)
def separa_palavras(frase):
    return frase.split()
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho wmédio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]
def n_palavras_unicas(lista_palavras):
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
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
def compara_assinatura(as_a, as_b):
    i=0
    soma=0
    while i<6:
      soma=soma+abs(as_a[i]-as_b[i])
      i=i+1
    compara=soma/6
    return compara
def calcula_assinatura(texto):
    assinatura = []
    assinatura.append(tamanho_medio_palavra(lista_palavras(texto)))
    assinatura.append(relacao_type_token(texto))
    assinatura.append(hapax_legomana(texto))
    assinatura.append(tamanho_medio_sentenca(texto))
    assinatura.append(complexidade_sentenca(texto))
    assinatura.append(tamanho_medio_frase(texto))
    return assinatura
def avalia_textos(textos, ass_cp):
    maior_probabilidade = 0
    count_autor = 0
    count = 0
    for i in textos:
        assinatura_texto = calcula_assinatura(i)
        probabilidade = compara_assinatura(assinatura_texto, ass_cp)
        if probabilidade > maior_probabilidade:
            maior_probabilidade = probabilidade
            count_autor = count
        count += 1
    print('\nO autor do texto', count_autor,'está infectado com COH-PIAH')
    return count_autor
assinatura_infectada = le_assinatura()
textos = le_textos()
avalia_textos(textos, assinatura_infectada)