choice = 1
while choice == 1: # this loop variable should be different than the variable used below
  print("Choose an operation:")
  print("1. +")
  print("2. -")
  print("3. *")
  print("4. /")
  print("5. %")
  print("6. **")

  choice = -1 # I don't like making the loop condition the same as the user's choice
  while choice < 1 or choice > 6: 
    choice = int(input()) # input MUST have stuff in the parantheses
	# use the choice variable and do choice = int(input(put # in ))
  return choice # this statement shouldn't be here, this isn't a function

  x = input("Enter first number:") 
  y = input("Enter second number:")

  if op == 1: # this op variable is unused
    print(x+y)
  elif op == 2:
    print(x-y)
  elif op == 3:
    print(x*y)
  elif op == 4:
    print(x/y)
  elif op == 5:
    print(x%y)
  elif op == 6:
    print(x**y)

choice = int(input("Enter 1 if you want to continue:")) # this is out of the loop, the user will never be asked this question, will never be able to loop again
