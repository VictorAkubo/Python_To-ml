
def closure(x):
  def innerclosure(y):
    return x+y
  return innerclosure

let = closure(4)
result =let (5)
print(result)