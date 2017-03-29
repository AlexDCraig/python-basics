###### Function : get_gravitational_force
###### Paremters: 3 floating point numbers, 2 corresponding to two different masses, 1 corresponding to the distance between them
###### Preconditions: all three parameters must be in manipulatable floating point form
###### Postconditions: None.

def get_gravitational_force(mass1, mass2, dist):
	numerator = (.000000006673)*(mass1)*(mass2);
	denominator = dist;
	force = numerator/denominator;
	return force;


###### Function: main
###### Description: Prompts user for two masses and a distance, converts them to floating point (if possible. if not, repeats main) and prints out the resulting function call to get_gravitational_force. Then, asks the user if they want to repeat the program.

def main():
	try:
		mass1 = float(input("Please enter mass 1."));
	except:
		print("Error: Try again.");
		main();
	try:
		mass2 = float(input("Please enter mass 2."));
	except: 
		print("Error: try again");
		main();

	try:
		distance = float(input("Please enter the distance."));
	except:
		print("Error, try again");
		main();

	print("The gravitational force is ", get_gravitational_force(mass1, mass2, distance));
	try:
		repeat = int(input("Would you like to do it again? 1 for yes and 0 for no."));
	except:
		exit(1);
	
	if (repeat == 1):
		main();

	elif (repeat == 0):
		exit(1);
	
main();
