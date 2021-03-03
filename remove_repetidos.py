def remove_repetidos(x):
  z=[]
  for y in x:
    if y not in z:
      z.append(y)
  z.sort()
  return z