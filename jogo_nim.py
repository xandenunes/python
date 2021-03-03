def usuario_escolhe_jogada(n,m):
  pecas=int (input("Quantas peças você vai tirar?"))
  x=0
  print(" ")
  if pecas<=m and pecas<=n and pecas>0:
    if pecas==1:
      print("Você tirou uma peça")
    else:
      print("Você tirou",pecas,"peças")
    return pecas
  else:
    print("Oops! Jogada inválida! Tente de novo.")
    print(" ")
    x=usuario_escolhe_jogada(n,m)
    return x
def computador_escolhe_jogada(n,m):
  num=0
  x=0
  while num<=m:
    x=n-num
    if x%(m+1)==0:
      if num==1:
        print("O computador tirou uma peça.")
      else:
        print("O computador tirou",num,"peças.")
      return num 
    num=num+1
def inicio(n,m):
  if n%(m+1)==0:
    print("Você começa!")
    return True
  else :
    print("Computador começa!")
    return False
def partida():
  n=int (input("Quantas peças? "))
  m=int (input("Limite de peças por jogada? "))
  if m>=n or n<=0 or m<=0:
    print("Oops! Jogada inválida! Tente de novo.")
    partida()
  else:
    print(" ")
    tiraC=1
    tiraU=1
    i=inicio(n,m)
    if i==True :
      while n>0:
        tiraU=usuario_escolhe_jogada(n,m)
        n=n-tiraU
        print("Agora restam",n,"peças no tabuleiro.")
        print(" ")
        if n==0:
          print("Fim do jogo! Você ganhou!")
          print(" ")
          return True
        tiraC=computador_escolhe_jogada(n,m)
        n=n-tiraC
        print("Agora restam",n,"peças no tabuleiro.")
        print(" ")
        if n==0:
          print("Fim do jogo! O computador ganhou!")
          print(" ")
          return False
    else:
      while n>0:
        tiraC=computador_escolhe_jogada(n,m)
        n=n-tiraC
        print("Agora restam",n,"peças no tabuleiro.")
        print(" ")
        if n==0:
          print("Fim do jogo! O computador ganhou!")
          print(" ")
          return False
        tiraU=usuario_escolhe_jogada(n,m)
        n=n-tiraU
        print("Agora restam",n,"peças no tabuleiro.")
        print(" ")
        if n==0:
          print("Fim do jogo! Você ganhou!")
          print(" ")
          return True
def campeonato():
  n=1
  y=0
  x=0
  while n<=3:
    print("**** Rodada",n," ****\n")
    n=n+1
    part=partida()
    if part==True:
      x=x+1
    if part==False:
      y=y+1
  print("**** Final do campeonato! ****\n")
  print("Placar: Você",x,"X",y,"Computador")
print("Bem-vindo ao jogo do NIM! Escolha:")
n=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
print("")
if n==1:
  print("Voce escolheu um partida!\n")
  partida()
if n==2:
  print("Voce escolheu um campeonato!")
  campeonato()