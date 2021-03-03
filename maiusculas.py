def maiusculas(frase):
  respostas="p"
  for palavras in frase:
    for letras in palavras:
      if ord(letras) <= 90 and ord(letras) >= 65:
        if respostas=="p":
          respostas = letras
        else:
          respostas = respostas + letras
  return respostas