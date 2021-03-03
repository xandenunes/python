def dimensoes2(matriz):
  linha=len(matriz)
  for i in matriz:
    coluna=int(len(i))
  return coluna
def soma_matrizes(m1,m2):
  coluna_m1=dimensoes2(m1)
  coluna_m2=dimensoes2(m2)
  if coluna_m1==coluna_m2 and len(m1)==len(m2):
    soma=m1
    for i in range(len(m1)):
      for j in range(coluna_m1):
        soma[i][j]=m1[i][j]+m2[i][j]
  else:
    return False
  return soma