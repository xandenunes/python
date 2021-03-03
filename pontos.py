import math
X1=int(input("insira um numero: "))
Y1=int(input("insira um numero: "))
X2=int(input("insira um numero: "))
Y2=int(input("insira um numero: "))
distancia=math.sqrt(((X1-X2)**2)+((Y1-Y2)**2))
if distancia>=10:
  print("longe")
if distancia<10:
  print("perto")