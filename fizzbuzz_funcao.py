def fizzbuzz(x):
  resto=x%3
  resto2=x%5
  if resto==0 and resto2==0:
    return "FizzBuzz"
  else:
      if resto==0:
        return "Fizz"
      if resto2==0:
        return "Buzz"
      else:
        return x