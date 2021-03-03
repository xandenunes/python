largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))
i=0
while i<altura:
  cont=0
  while cont<largura:
    if i==altura-1 or i==0 or cont==largura-1 or cont==0:
      print("#",end=(""))
    else:
      print(" ",end=(""))
    cont=cont+1
  print()
  i=i+1