def function(n):
  if n==0 | n==1:
    return n
  elif n < 0:
    return n
  else:
    print(n)
    return function(n-1)
number = function(5)
print(number)