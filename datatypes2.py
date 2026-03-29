#list in python
#ways to create list

list1 = [1,2,3,4,3,3,"name","victor"]
list2 = list("235782bdhbe")
print(list1)
print(list2)
#list comprehension
list3 = [x**2 for x in range(6)]
print(list3)
print(list(range(0,6)))

#access elements in list
print(list1[2])
print(list2[3])
print(list3[0])
print("3 index: ",list1.index(3))
print(list1.count(3))
#print(list1.sort(key=0,reverse=True))
#list slice
letlist = list3[1:4]
print(letlist)
#len could be used fir list,tuple,
print(len(list3))
#tuples 
tuples = (4)
print(tuples)


