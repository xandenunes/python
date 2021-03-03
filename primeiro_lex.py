def primeiro_lex(nomes):
  curto_max=nomes[0]
  for nome in nomes:
    if nome<curto_max:
      curto_max=nome
  return curto_max