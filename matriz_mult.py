def dimensoes2(matriz):
  linha=len(matriz)
  for i in matriz:
    coluna=int(len(i))
  return coluna
def sao_multiplicaveis(m1, m2):
  coluna_m1=dimensoes2(m1)
  if len(m2)==coluna_m1:
    return True
  else:
    return False