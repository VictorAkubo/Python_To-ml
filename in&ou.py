#input
name = input("what is your name")
print("you entered the name: ",name)

#input always returns a string to convert to integer or float use int() | float()

number = int(input("enter a number"))
print(f'the sum of 4 and {number} is : ' , number+4)

#output
#output is basically your print function
print(name)


#formatted output prefixes "f" in frint of string just the way i did above

print(f"hi my name is {name} and i entered {number} that gave me the output of {4+number}")

#format() method 

print("Hi my name is {} and i entered {}".format(name,number))



