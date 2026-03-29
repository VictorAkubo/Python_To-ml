#break this breaks out of the loop
for v in range(5):
  if v == 4:
    break
  print(v)
  
#continue this jumps that specific loop
for v in range(5):
  if v == 2:
    continue
  print(v)
#pass
print("pass")
for v in range(6):
  if v == 2:
    pass
  print(v)