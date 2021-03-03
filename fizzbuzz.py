num=int(input("insira um numero: "))
resto=num%3
resto2=num%5
if resto==0 and resto2==0:
  print("FizzBuzz")
else:
  print(num)