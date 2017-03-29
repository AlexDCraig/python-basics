# get initial input, no preconditions, passes user input to next function (postconditions). These inputs must be valid for the program to continue.

def get_initial_input():
	try:
		numTests = int(input("Please enter the number of tests. "));
	except:
		print("Insufficient information.");
		pass;
	try:
		numAssign = int(input("Please enter the number of assignments. "));
	except:
		print("Insufficient information.");
		pass;
	try:
		numEx = int(input("Please enter the number of exercises. "));
	except:
		print("Insufficient information.");				
		pass;
	try:
		numLabs = int(input("Please enter the number of labs. "));
	except:
		print("Insufficient information.");
		pass;
	
	try:
		if (numTests > 0):
			temp = int(input("Is there a final exam? 1 = yes, 0 = no. "));
		
			if (temp == 1):
				isFinal = True;

			elif (temp == 0):
				isFinal = False;
				finalWeight = 0;

			else:
				print("Invalid input.");

			if (isFinal == True):
				num = float(input("What is the weight of the final? "));
				if (num >= 0 and num <= 100):
					finalWeight = num;
				else:
					print("Invalid input.");
		
			num2 = float(input("What is the weight of each non-final exam? "));
			if (num2 >= 0 and num2 <= 100):
				examWeight = num2;
			else:
				print("Invalid input.");
	
		elif (numTests == 0):
			examWeight = 0;
			finalWeight = 0;
			isFinal = False;

		else:
			print("Invalid input.");

	except:
		print("Invalid.");		
		pass;
	
	try:
		if (numAssign > 0):
			
			num3 = float(input("What is the weight of the assignments? "));
			if (num3 >= 0 and num3 <= 100):
				assignWeight = num3;
			else:
				print("Invalid input.");
		elif (numAssign == 0):
			assignWeight = 0;
		else:
			print("Invalid input");
	
	except:
		print("Invalid.");
		pass;
	try:
		if (numEx > 0):
			num4 = float(input("What is the weight of the exercises? "));
			if (num4 >= 0 and num4 <= 100):
				exerciseWeight = num4;
			else:
				print("Invalid input");
		elif (numEx == 0):
			exerciseWeight = 0;
		else:
			print("Invalid input");
	except:
		print("Invalid.");
		pass;

	try:
		if (numLabs > 0):
			num5 = float(input("What is the weight of the labs? "));
			if (num5 >= 0 and num5 <= 100):
				labWeight = num5;
			else:
				print("Invalid input");
		elif (numLabs == 0):
			labWeight = 0;
		else:
			print("Invalid input");
	except:
		print("Invalid.");
		pass;

	try:
		get_scores(numTests, numAssign, numEx, numLabs, finalWeight, examWeight, assignWeight, exerciseWeight, labWeight, isFinal);
	except:
		print("Insufficient information.");
		pass;


# get_scores. preconditions: accepts info from initial user input function, these data must be valid. postconditions: ships more info to next function "get scores", so this info must be valid

def get_scores(numTests, numAssign, numEx, numLabs, finalWeight, examWeight, assignWeight, exerciseWeight, labWeight, isFinal):
	
	try:	
		if(numTests != 0):
			if (isFinal == True):
				finalScoreActual = float(input("Please enter your final exam score. "));
				finalScoreTotal = float(input("What was the total amount possible? "));
			else:
				finalScoreActual = 0;
				finalScoreTotal = 0;
		
			k = 0;
			testlist = [];
			while (k < numTests):
				testlist.append(float(input("Please enter your test score. ")));
				k += 1;
			testScoresTotal = float(input("What was the total points possible for all tests? "));
		
		else:
			finalScoreActual = 0;
			finalScoreTotal = 0;
			testlist = [];
			testlist.append(0);
			testScoresTotal = 0;
	except:
		print("Invalid info");
		pass;
		
	try:

		if (numAssign != 0):
			assignmentlist = [];
			k = 0;
			assignmentScoresTotal = float(input("What was the total points possible for all assignments. "));
			while (k < numAssign):
				assignmentlist.append(float(input("Please enter your assignment score. ")));
				k += 1;

		else:
			assignmentlist = [];
			assignmentlist.append(0);
			assignmentScoresTotal = 0;
	except:
		print("Invalid.");
		pass;
	
	try:

		if (numEx != 0):
			exerciselist = [];
			k = 0;
			exerciseScoresTotal = float(input("What was the total points possible for all exercises? "));
			while (k < numEx):
				exerciselist.append((float(input("Please enter your exercise score. "))));
				k += 1;
		else:
			exerciselist = [];
			exerciselist.append(0);
			exerciseScoresTotal = 0;
	except:
		print("Invalid.");
		pass;
	

	try:

		if (numLabs != 0):
			lablist = [];
			k = 0;
			labScoresTotal = float(input("What was the total points possible for all labs? "));
			while (k < numLabs):
				lablist.append((float(input("Please enter your lab score. "))));
				k += 1;

		else:
			lablist = [];
			lablist.append(0);
			labScoresTotal = 0;
	except:
		print("Invalid.");
		pass;

	try:
		calculate_weighted_avg(finalScoreActual, finalScoreTotal, testlist, testScoresTotal, assignmentScoresTotal, exerciseScoresTotal, assignmentlist, exerciselist, lablist, labScoresTotal, assignWeight, finalWeight, exerciseWeight, examWeight, labWeight);
	except:
		print("Invalid info provided.");
		pass;


# calculates percentages of each category and ships it off to calc_class_grade. Preconditions: info must be valid from the last function.


def calculate_weighted_avg(finalScoreActual, finalScoreTotal, testlist, testScoresTotal, assignmentScoresTotal, exerciseScoresTotal, assignmentlist, exerciselist, lablist, labScoresTotal, assignWeight, finalWeight, exerciseWeight, examWeight, labWeight):
	if (finalScoreActual != 0):
		finalpct = finalWeight * (finalScoreActual/finalScoreTotal);

	else:
		finalpct = 0;
		
	if (testlist[0] != 0):
		k = 0;
		studenttotal = 0;
		size = len(testlist);
		while (k < size):
			studenttotal += testlist[k];
			k += 1;
		testpct = examWeight * (studenttotal/testScoresTotal);
	else:
		testpct = 0;

	if (assignmentlist[0] != 0):
		k = 0;
		studenttotal = 0;
		size = len(assignmentlist);
		while (k < size):
			studenttotal += assignmentlist[k];
			k += 1;
		assignmentpct = assignWeight * (studenttotal/assignmentScoresTotal);
	else:
		assignmentpct = 0;

	if (exerciselist[0] != 0):
		k = 0;
		studenttotal = 0;
		size = len(exerciselist);
		while (k < size):
			studenttotal += exerciselist[k];
			k += 1;
		exercisepct = exerciseWeight * (studenttotal/exerciseScoresTotal);

	else:
		exercisepct = 0;
	
	if (lablist[0] != 0):
		k = 0;
		studenttotal = 0;
		size = len(lablist);
		while (k < size):
			studenttotal += lablist[k];
			k += 1;
		labscorespct = labWeight * (studenttotal/labScoresTotal);

	else:
		labscorespct = 0;

	calculate_class_grade(finalpct, testpct, assignmentpct, exercisepct, labscorespct);

# adds up all percentages, compares them to 100. preconditions: must be passed valid data otherwise an error will be thrown, program must restart

def calculate_class_grade(finalpct, testpct, assignmentpct, exercisepct, labscorepct):
	totalPct = 0;
	totalPct += finalpct;
	totalPct += testpct;
	totalPct += assignmentpct;
	totalPct += exercisepct;
	totalPct += labscorepct;

	if (totalPct >= 90):
		print("You got an A.");

	elif (totalPct >= 80):
		print("You got a B.");

	elif (totalPct >= 70):
		print("You got a C.");

	elif (totalPct >= 60):
		print("You got a D.");

	elif (totalPct >= 0):
		print("You got an F.");
	

def main():
	get_initial_input();	
	
	try:
		userInput = int(input("Care to calculate another class grade? 1 for yes, 0 for no. "));
		if (userInput == 1):
			main();
		elif (userInput == 0):
			print("Goodbye.");
	except:
		print("Program terminated.");
		pass;






main();
