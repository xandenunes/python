def dimensoes2(matriz):
  linha=len(matriz)
  for i in matriz:
    coluna=int(len(i))
  return coluna
def imprime_matriz(matriz):
  coluna=dimensoes2(matriz)
  for i in range(len(matriz)):
    for j in range(coluna):
      if j==coluna-1:
        print(matriz[i][j], end="")
      else:
        print(matriz[i][j], end=" ")
    print("")