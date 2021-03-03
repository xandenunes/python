def busca(seq,x):
  #seq é uma lista e X é oq vc quer achar
  for i in range(len(seq)):
    if seq[i]==x:
      return i
  return False