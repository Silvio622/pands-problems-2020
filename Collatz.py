# Silvio Dunst
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

currentvalue = int(input("Please Enter a positive Integer: ")) # convert a Input to an Integer
m = 2 # If you divide a number by 2 and it gives a remainder of 0 then it is known as even number, otherwise an odd number.
nextvalue = currentvalue

while currentvalue == 1:
    
    nextvalue = nextvalue - currentvalue
    if nextvalue % m == 0: # if you have a remainder of 0 it is true it is a even number
        nextvalue = nextvalue / 2
    else:
        nextvalue = (nextvalue * 3) + 1
        print(nextvalue)
if currentvalue <= 0: 
  print("The number you entered is not a positive Integer")
