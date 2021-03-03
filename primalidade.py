num=int(input("Digite um número inteiro: "))
i=2
while num>i:
  if num%i==0:
    print("não primo")
    break
  i=i+1
if num==i :
  print("primo")
if num==1:
  print("não primo")