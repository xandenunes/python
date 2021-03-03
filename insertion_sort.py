def insertion_sort(lista):
  for i in range(len(lista)):
      for j in range(i, 0, -1):
          if lista[j] < lista[j-1]:
              lista[j], lista[j-1] = lista[j-1], lista[j]

  return lista