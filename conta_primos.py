def primo(num):
  i=2
  while num>i:
    if num%i==0:
      return False
    i=i+1
  if num==i :
    return True
  if num==1:
    return False
def n_primos(x):
  primos=0
  cont=1
  while cont<=x:
    sera=primo(cont)
    if sera==True:
      primos=primos+1
    cont=cont+1
  return primos