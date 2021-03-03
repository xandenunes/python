def e_hipotenusa(n):
  import math
  i=1
  while i<n:
    j=1
    while j<n:
      x=0
      x=math.sqrt(i**2+j**2)
      if n==x:
        return True
      j=j+1
    i=i+1
  return False
def soma_hipotenusas(n):
  i=1
  x=0
  soma=0
  while i<=n:
    x=e_hipotenusa(i)
    if x==True:
      soma=soma+i
      print(i)
    i=i+1
  return soma