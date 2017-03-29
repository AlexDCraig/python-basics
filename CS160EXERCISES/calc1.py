while True: #input is used wrong each time
# while what is true? this condition statement describes nothing
# and isn't doing anything
  print("Enter a number operation (+, -, /, *, **, %):")
  o = input()

  print("Input your first number")
  f = input()

  print("Input your second number:")
  s = input() 

  if o == '%': # make these elif
    print(f % s)
  if o == '**':
    print(f ** s)
  if o == '*':
    print(f * s)
  if o == '/':
    print(f / s)
  if o == '-':
    print(f - s)
  if o == '+':
    print(f + s)

  print("Are you done? (no or yes)")
  answer = input() # Should read "answer = input("done yet? yes, no")
# input takes parameters
  if answer == "no":
    break # don't like this use of break

