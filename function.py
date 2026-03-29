def sum(a):
  x = a ** 3
  y = a ** 4
  return x,y
result = sum(4)
print(result)
x,y = sum(4)
print(x)
print(y)

#it isnt compulsory to use args and kwargs
def respective(*args,**kwargs):
  for v in args:
    print(v)
  for key, value in kwargs.items():
    print(f"{key}: {value} ")
    
respective(1,2,3,4,"victor",name="victor",count="number")