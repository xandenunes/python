import math
a=int(input("insira a constante A "))
b=int(input("insira a constante B "))
c=int(input("insira a constante C "))
delta=b**2-4*a*c
if delta>0:
  raiz1=(-b + math.sqrt(delta))/(2*a)
  raiz2=(-b - math.sqrt(delta))/(2*a)
  print("as raízes da equação são",raiz2,"e",raiz1)
if delta==0:
  raiz3=(-b)/(2*a)
  print("a raiz desta equação é",raiz3)
if delta<0:
  print("esta equação não possui raízes reais")