num=1
numero=[]
i=0
while num>0:
  num=int(input("Digite um número: "))
  numero.append(num)
x=len(numero)-2
while x>=i:
  print(numero[x])
  x=x-1