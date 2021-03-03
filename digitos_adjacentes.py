num=int(input("Digite um número inteiro: "))
soma=0
restoA=-1
adjacentes=False
while num>0:
  resto=num%10
  if restoA==resto:
    print("sim")
    adjacentes=True
    break
  restoA=resto
  num=num//10
if adjacentes==False:
  print("não")