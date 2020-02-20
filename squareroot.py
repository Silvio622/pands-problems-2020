# Silvio Dunst
# this program takes a positive floating point number as input and outputs an approximation of its square root

import math    # import math library and functions
Userinput = float(input("Please Enter a positive number: ")) # User Input

if Userinput > 0: # User Input has to be a positive number

    def sqrt(Userinput): # define/create a function with the name sqrt and a input value from User Input variable
        squareroot = math.sqrt(Userinput) # create a local variable squareroot and use math library to calculate the squareroot from the User input value
        roundsquareroot = round(squareroot, 1) # round function ( to rounded variable, number of digits after decimal point)

        return roundsquareroot # returns a value in the local variable roundsquareroot
    print(sqrt(Userinput)) # calls the function sqrt in the print the result of the rounded sqrt function of the UserInput value

else:
    print("You did not enter a positve number")
 

