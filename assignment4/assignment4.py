import math # To use sqrt()
# Take a positive whole number, n. Output the square root of n 
# using two approaches: 1) the Babylonian algorithm, and 
# 2), by using the math library function sqrt().

def main():
	numToRoot = getInput();
	mathLibRoot = math.sqrt(numToRoot);
	userAnswer = userBabylon(numToRoot);
	print("Given your specified number of loop iterations and first guess we got the square root of ", numToRoot, " is ", userAnswer);
	programmerLoopCount = programmerBabylon(numToRoot);
	print("The number of iterations necessary for the algorithm to exactly reach the same value as the Math library's estimate with a starting guess of n/2 is ", programmerLoopCount, ".");
	print("For reference, the root of the number as calculated by the math library is ", mathLibRoot, ".");
	return 0;

def getInput():
	rootNum = int(input('Please enter a positive whole number. '));
	if rootNum ==  0:
		print('The square root of 0 is 0. ');
		getInput();
	
	if rootNum < 0:
		print("That's a negative number. I'll change that to a positive. ")
		rootNum = rootNum * -1;
		print('The number is now ', rootNum, '.');
		return rootNum;
	
	if rootNum > 0:
		return rootNum;

	getInput();

def userBabylon(rootNum):
	# LET THE USER TRY AND GUESS
	userGuess = float(input("First, I'll let you try and get to the right answer. Please guess a number you think the square root might be.  "));
	userLoop = int(input("How many times should we call the loop?  "));
	userCount = 0;
	userRoot = rootNum;

	while userCount != userLoop:
		s = userRoot / userGuess;
		userGuess = (userGuess + s) / 2;
		userCount+=1;
		if (userCount == userLoop):
			return userGuess;
	
	userBabylon(rootNum);

def programmerBabylon(rootNum):
	print("Let's find out how many iterations it would take to get to the Math library's sqrt root result using the Babylonian algorithm.  ");
	# FIND HOW MANY ITERATIONS TO EQUAL MATHLIBRARY
	guessNum = rootNum / 2;
	print('The initial guess, as recommended by the assignment details, will be the imputed number divided by 2, which is ', guessNum, '.');
	print('Using that initial guess... ');
	counter = 1;
	while guessNum != math.sqrt(rootNum): # Make the Babylonian algorithm compute until it reaches the math library's answer.
		r = rootNum / guessNum;
		guessNum = (guessNum + r) / 2;
		counter+=1;
	return counter;

main();
