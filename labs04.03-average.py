# Silvio Dunst
# this program reads in numbers until user enter 0 
# it will then print back out again and their average
# use a list

numbers = [] # numbers is a list variable
# first number then we check if it is 0 in the while loop
number = int(input("Enter a number (0 will quit): ")) # Enter a integer number as Input

while number !=0: # number must not equal 0
   numbers.append(number) # writes the new entered number as a new list enrty "number" in list variable "numbers" 
    # every time the while loops is activ

    # read the next number and check if 0
   number = int(input("Enter another number (0 will quit): ")) # Enter a integer number as Input
# while loop finished

for value in numbers: # the for loop keeps tack of the amount of list entries
    print(value)

# I want average to be a float
average = float(sum(numbers)) / len(numbers) # average is a key word data type for the calculation is a float 
# the sum add in every for loop the value of list entry (number variable) and then divide by the amount of list entries
print("The average is {}".format(average))



