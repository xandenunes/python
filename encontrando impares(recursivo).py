def encontra_impares(lista):
  lista2=[]
  if len(lista) > 0:
    if lista[0]%2 >= 1:
      lista2.append(lista[0])
    lista2.extend(encontra_impares(lista[1:]))
  
  return lista2