def conta_letras(frase, contar="vogais"):
  vogais=0
  consoantes=0
  for palavras in frase:
    for letras in palavras:
      if letras != " ":
        if letras=="A" or letras=="E" or letras=="I" or letras=="O" or letras=="U" or letras=="a" or letras=="e" or letras=="i" or letras=="o" or letras=="u":
          vogais += 1
        else:
          consoantes += 1
  if contar=="vogais":
    return vogais
  else:
    return consoantes