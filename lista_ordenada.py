def ordenada(lista):
  for i in range(len(lista)):
    if i==0 and len(lista)>1:
      if lista[i]>lista[i+1]:
        return False
    elif lista[i-1]>lista[i]:
      return False
  return True