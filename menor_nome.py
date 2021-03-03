def menor_nome(nomes):
  curto_max=len(nomes[0])
  menor=nomes[0]
  for nome in nomes:
    nome_limpo=nome.strip()
    curto=len(nome_limpo)
    if curto<curto_max:
      curto_max=curto
      menor=nome_limpo
  return menor.capitalize()