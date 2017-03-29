# 10/12/2015 : CS160 Assignment 3, Python Calculator
# By : Alex Hoffer


#Get operator
operator = input('Enter one of the following operators: +, -, *, /, %, or **. ')

#Get first number. Note: any value will be converted to float type.
num1 = float(input('Enter your first number. ')); 

#Get the second number, convert it to float.
num2 = float(input('Enter your second number. '));

#Calculate num1 operator num2.
if operator == '+':
	solution = num1 + num2;

elif operator == '-':
	solution = num1 - num2;

elif operator == '*':
	solution = num1 * num2;

elif operator == '/':
	solution = num1 / num2;

elif operator == '%':
	solution = num1 % num2;

elif operator == '**':
	solution = num1 ** num2;    

#Print the solution. 
print('The answer to that is:')
print(solution)

