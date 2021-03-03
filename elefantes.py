def incomodam(n):
  if n//1==n and n>0:
    if n > 1:
      n=n-1
      return "incomodam " + str(incomodam(n))
    return "incomodam "
  else:
    return ""
    
def elefantes(n,num=1):
  frase=""
  if n>1:
    if num<=n:
      if num==1:
        frase="Um elefante incomoda muita gente\n"
      else:
        frase="{} elefantes {}muito mais".format(num,str(incomodam(num)))
      if num<n and num!=1:
        frase+= "\n{} elefantes incomodam muita gente\n".format(num)
      return frase + str(elefantes(n,num+1))
    else:
      return""
  else: 
    return ""