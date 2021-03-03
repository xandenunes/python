# Introdução
# Manuel Estandarte é monitor na disciplina Introdução à
# Produção Textual I na Universidade de Pasárgada (UPA).
# Durante o período letivo, Manuel descobriu que uma
# epidemia de COH-PIAH estava se espalhando pela UPA.
# Essa doença rara e altamente contagiosa faz com que
# indivíduos contaminados produzam, involuntariamente,
# textos muito semelhantes aos de outras pessoas. Após
# a entrega da primeira redação, Manuel desconfiou que
# alguns alunos estavam sofrendo de COH-PIAH. Manuel,
# preocupado com a saúde da turma, resolveu buscar
# um método para identificar os casos de COH-PIAH. Para
# isso, ele necessita da sua ajuda para desenvolver um
# programa que o auxilie a identificar os alunos contaminados.

# Detecção de autoria
# Diferentes pessoas possuem diferentes estilos de escrita;
# por exemplo, algumas pessoas preferem sentenças mais curtas,
# outras preferem sentenças mais longas. Utilizando diversas
# estatísticas do texto, é possível identificar aspectos que
# funcionam como uma “assinatura” do seu autor e, portanto,
# é possível detectar se dois textos dados foram escritos por
# uma mesma pessoa. Ou seja, essa “assinatura” pode ser
# utilizada para detecção de plágio, evidência forense ou,
# neste caso, para diagnosticar a grave doença COH-PIAH

# Traços linguísticos
# Neste exercício utilizaremos as seguintes estatísticas para
# detectar a doença:
# Tamanho médio de palavra: Média simples do número de caracteres
#   por palavra.
# Relação Type-Token: Número de palavras diferentes utilizadas
#   em um texto divididas pelo total de palavras.
# Razão Hapax Legomana: Número de palavras utilizadas uma única
#   vez dividido pelo número total de palavras.
# Tamanho médio de sentença: Média simples do número de
#   caracteres por sentença.
# Complexidade de sentença: Média simples do número de frases
#   por sentença.
# Tamanho médio de frase: Média simples do número de caracteres
#   por frase.

# Funcionamento do programa
# A partir da assinatura conhecida de um portador de COH-PIAH,
# seu programa deverá receber diversos textos e calcular os
# valores dos diferentes traços linguísticos desses textos
# para compará-los com a assinatura dada. Os traços
# linguísticos que seu programa deve utilizar são calculados
# da seguinte forma:

# Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
# Relação Type-Token é o número de palavras diferentes
#   dividido pelo número total de palavras. Por exemplo,
#   na frase "O gato caçava o rato", temos 5 palavras no total
#   (o, gato, caçava, o, rato) mas somente 4 diferentes(o,
#   gato, caçava, rato). Nessa frase, a relação Type-Token
#   vale 45 = 0.8
# Razão Hapax Legomana é o número de palavras que aparecem uma
#   única vez dividido pelo total de palavras. Por exemplo, na
#   frase "O gato caçava o rato", temos 5 palavras no total(o,
#   gato, caçava, o, rato) mas somente 3 que aparecem só uma
#   vez(gato, caçava, rato). Nessa frase, a relação Hapax
#   Legomana vale 35 = 0.6
# Tamanho médio de sentença é a soma dos números de caracteres
#   em todas as sentenças dividida pelo número de sentenças(os
#   caracteres que separam uma sentença da outra não devem ser
#   contabilizados como parte da sentença).
# Complexidade de sentença é o número total de frases divido
#   pelo número de sentenças.
# Tamanho médio de frase é a soma do número de caracteres em
#   cada frase dividida pelo número de frases no texto(os
#   caracteres que separam uma frase da outra não devem ser
#   contabilizados como parte da frase).
# Após calcular esses valores para cada texto, você deve
#   compará-los com a assinatura fornecida para os infectados
#   por COH-PIAH. O grau de similaridade entre dois textos,
#   a e b, é dado pela fórmula:


#       6
#       ∑    .||f{i,a} - f{i,b}||
#       i = 1
# S{ab} =  _________________________
#                   6

# Onde:
# S{ab} é o grau de similaridade entre os textos a e b
# fi, a é o valor de cada traço linguístico i no texto a
# fi, b é o valor de cada traço linguístico i no texto b.
# No nosso caso, o texto bb não é conhecido, mas temos a
# assinatura correspondente: a assinatura de um aluno
# infectado com COH-PIAH. Ou seja, sabemos o valor de
# f{i, b} que é dado como valor de entrada do programa.

# Caso você não esteja acostumado com a notação matemática,
# podemos destrinchar essa fórmula da seguinte maneira:

# Para cada traço linguístico i(tamanho médio da palavra,
# relação type-token etc.) se quer a diferença entre o valor
# obtido em cada texto dado(a) e o valor típico do texto de
# uma pessoa infectada(b): f{i, a} - f{i, b}

# Dessa diferença se toma o módulo (∣∣…∣∣), lembre-se da função
# abs do python.

# Somamos os resultados dos 6 traços linguísticos
#       6
#       ∑
#       i = 1

# E por final dividimos por 6 (x/6)

# Perceba que quanto mais similares aa e bb forem, menor S{ab}
# será. Para cada texto, você deve calcular o grau de
# similaridade com a assinatura do portador de COH-PIAH e,
# no final, exibir qual texto mais provavelmente foi escrito
# por algum aluno infectado(ou seja, o texto com assinatura
# mais similar à assinatura dada).

import re


def le_assinatura():
    #   '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    #   '''A funcao le todos os textos a serem comparados e
    #   devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +
                      " (aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    #   '''A funcao recebe um texto e devolve uma lista das
    #   sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    #   '''A funcao recebe uma sentenca e devolve uma lista das
    #   frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    #   '''A funcao recebe uma frase e devolve uma lista das
    #   palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    #   '''Essa funcao recebe uma lista de palavras e devolve o
    #   numero de palavras que aparecem uma unica vez'''
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
    #   '''Essa funcao recebe uma lista de palavras e devolve o
    #   numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)


def compara_assinatura(as_a, as_b): #as_b é o valor de entrada do programa
    #   '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de
    #   texto e deve devolver o grau de similaridade nas
    #   assinaturas.'''
    i = 0
    soma = 0
    while i < 6:    #i itera sobre os diferentes indices de COH-PIAH
        soma += abs(as_a[i] - as_b[i])
        i += 1
    probabilidade = soma/6
    return probabilidade


def calcula_assinatura(texto):
    # Retorna uma lista com todos os índices de um texto
    assinatura = []
    assinatura.append(tamanho_medio_palavra(lista_palavras(texto)))
    assinatura.append(relacao_type_token(texto))
    assinatura.append(hapax_legomana(texto))
    assinatura.append(tamanho_medio_sentenca(texto))
    assinatura.append(complexidade_sentenca(texto))
    assinatura.append(tamanho_medio_frase(texto))
    return assinatura


def avalia_textos(textos, ass_cp):  #ass_cp é a assinatura de um texto infectado
    #   '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
    #   e uma assinatura ass_cp e deve devolver o numero (1 a n)
    #   do texto com maior probabilidade de ter sido infectado
    #   por COH-PIAH.'''
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

### Minhas funções ###

def lista_palavras(texto):
    #   Usando três funções, partindo texto em frases e frases em
    #   palavras, retorna uma lista de todas as palavras do texto
    sentencas = separa_sentencas(texto)  # retorna uma lista de
    # sentencas
    frases = []
    for i in sentencas:
        frases += separa_frases(i)  # retorna uma lista de frases
    palavras = []
    for i in frases:
        palavras += separa_palavras(i)  # retorna uma lista de palavras
    return palavras


def lista_frase(texto):
    # Retorna uma lista de frases a partir da função
    # "separa_sentencas" usando um texto como parametro
    sentencas = separa_sentencas(texto)
    frases = []
    for i in sentencas:
        frases += separa_frases(i)
    return frases


def tamanho_medio_palavra(lista_palavras):
    #   Recebe uma lista com todas as palavras de um texto,
    #   calcula a quantidade de caracteres de cada palavra, a
    #   quantidade total de palavras e retorna o tamanho medio
    tamanho_medio = 0
    for i in lista_palavras:
        tamanho_medio += len(i)
    return tamanho_medio/len(lista_palavras)


def relacao_type_token(texto):
    #   Recebe um texto, coleta todas as palavras, identifica as
    #   palavras diferentes e retorna o numero de palavras
    #   diferentes utilizadas em um texto divididas pelo total
    #   de palavras
    total_palavras = lista_palavras(texto)
    palavras_dif = n_palavras_diferentes(total_palavras)
    return palavras_dif/len(total_palavras)


def hapax_legomana(texto):
    #   Recebe um texto, coleta todas as palavras, identifica
    #   as palavras unicas e retorna o numero de palavras
    #   unicas utilizadas em um texto divididas pelo total
    #   de palavras
    total_palavras = lista_palavras(texto)
    palavras_unicas = n_palavras_unicas(total_palavras)
    return palavras_unicas/len(total_palavras)


def tamanho_medio_sentenca(texto):
    #   Recebe um texto, coleta todas as sentencas e a quantidade
    #   de seus caracteres e retorna-os dividido pela quantidade
    #   total de sentenças
    lista_sentencas = separa_sentencas(texto)
    caracteres_sentencas = 0
    for i in lista_sentencas:
        caracteres_sentencas += len(i)
    return caracteres_sentencas/len(lista_sentencas)


def complexidade_sentenca(texto):
    #   Recebe um texto, coleta todas as sentenças frases e
    #   retorna uma média simples
    sentencas = separa_sentencas(texto)  # retorna uma lista de sentencas
    frases = lista_frase(texto)
    return len(frases)/len(sentencas)


def tamanho_medio_frase(texto):
    #   Recebe um texto, coleta todas as frases e seus caracteres,
    #   retornando uma média simples
    caracteres_frase = 0
    lst_frase = lista_frase(texto)
    for i in lst_frase:
        caracteres_frase += len(i)
    return caracteres_frase/len(lst_frase)



### Começo do programa ###
assinatura_infectada = le_assinatura()
textos = le_textos()
avalia_textos(textos, assinatura_infectada)
