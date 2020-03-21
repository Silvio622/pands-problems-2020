# Silvio Dunst
# This program reads in the student percentage mark and prints out the corrosponding grade
# (the program should check that percentage grade is valid)
# under 40% Fail 
# Between 40% and 49 % Pass
# Between 50% and 59 % Merrit 2
# Between 60% and 69 % Merrit 1
# over 70 % Destinction

percentage = float(input("Enter the percentage: ")) # Input as a float Data type
print(percentage) # prints the input value

if percentage < 0 or percentage > 100:
    # later we will show you error handling
    # this should show an error
    print("Please Enter a number between 0 and 100")
elif percentage < 40 : # we know it is greater than 0
    print("Fail")
elif percentage < 50 : # Between 40% and 49 % Pass
    print("Pass")
elif percentage < 60 : # Between 50% and 59 % Merrit 2
    print("Merrit 2")
elif percentage < 69.5 : # Between 60% and 69 % Merrit 1
    print("Merrit 1") # for answer for questioons 2
else: # over 70 % Destinction
    print("Destinction")