#Assignment 3
#Name: CHOO YONG HAN

def mod_div(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)   

  return inner

def div(a, b):
  print("Your value a is: ", a)
  print("Your value b is: ", b)
  print("\n")
  print("Result of div(a,b) is: ", a%b)

div(2, 4)