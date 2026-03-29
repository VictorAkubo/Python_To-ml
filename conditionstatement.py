#if
x = 7
if x > 5:
  print("x is surely greater than 5")

#if else

if x < 5:
  print("x is surely greater than 5")
else:
    print("x is surely not less than 5")


#if elif else
if x > 5:
  print("x is greater than 5")
elif x==5:
    print("x is surely equal to 5")
else:
  print("{} is less than 5".format(x))
  
#nested if statement
if x > 5:
  if x == 6:
    print("x is equal to 6")
  else:
    print("x is not 6")
else:
  print("x is less than 5 and definitely not equal to 6")

#ternary
result = "let me in" if True else "let me out"
print(result)