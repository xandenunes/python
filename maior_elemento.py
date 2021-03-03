def maior_elemento(x):
  maior=x[0]
  for y in x:
    if maior<=y:
      maior=y
  return maior