#!/usr/bin/python3
if __name__=="__main__":
  import calculation
  a = 4 #use this variable as a first argument to call a function 
  b = 2 #use this variable as a second argument to call a function
  
  #ADD YOUR CODE HERE

  add = calculation.add(a,b)
  sub = calculation.sub(a,b)
  mul = calculation.mul(a,b)
  div = calculation.div(a,b)

  print('4 + 2 =',add)
  print('4 - 2 =',sub)
  print('4 * 2 =',mul)
  print('4 / 2 =',div)
