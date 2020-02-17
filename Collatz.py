# Silvio Dunst
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

import time # import time function block for troubleshooting to slow down the while loop

UserInput = int(input("Please Enter a positive Integer: ")) # convert a Input to an Integer
StartValue = 30 # create a variable for start the equation
ResultList = [] # a list variable

if UserInput > 0: # the user input must be a positive number
    CurrentValue = StartValue - UserInput # create a variable currentvalue for the process
   
    while CurrentValue > 1: # the while loops so long the currentvalue is greater then 1 
  
        if CurrentValue % 2 == 0: # If you divide a number by 2 and it gives a remainder of 0 then it is known as even number, otherwise an odd number.
             CurrentValue = CurrentValue / 2 # even number devide the currentvalue by 2
        else:
            CurrentValue = (CurrentValue * 3) + 1 # odd number multiply currentvalue by 3 and add 1       
      
        ResultList.append(int(CurrentValue)) # writes a new entry every time to the end of the list (Append object) as currentvalue
        time.sleep(0.5)  # use timer to slow down the while loop for troubleshooting 
        print(CurrentValue) #use print out of the currentvalue for troubleshooting
    print(ResultList) # print out all the currentvalues in a list variable Resultlist
else: # when the user input is a negative number
  print("The number you entered is not a positive Integer")

