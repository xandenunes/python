class Triangulo:
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c
  def perimetro(self):
    perimetro=self.a+self.b+self.c
    return perimetro
  def tipo_lado(self):
    if self.a==self.b and self.c==self.b and self.a==self.c:
      return "equilátero"
    elif self.a==self.b or self.c==self.b or self.a==self.c:
      return "isósceles"
    else:
      return "escaleno"
  def retangulo(self):
    a=self.a**2
    b=self.b**2
    c=self.c**2
    print(a)
    print(b)
    print(c)
    if a>b:
      if a>c:
        if a==b+c:
          return True
        else:
          return False
    elif b>c:
      if b==a+c:
        return True
      else:
        return False
    else:
      if c==a+b:
        return True
      else:
        return False