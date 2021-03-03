def maior_primo(x):
  num=x
  i=2
  while num>i:
    if num%i==0:
      num=num-1
      i=2
    i=i+1
  if num==i :
    return num