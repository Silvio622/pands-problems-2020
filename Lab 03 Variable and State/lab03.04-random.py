# program that prints out a random number between 1 and 10
import random
# number = random.randint(1,10) # random number 1 til 10
lowrange = int(input("Enter Low Range Number: "))
highrange = int(input("Enter High Range Number: "))
number = random.randint(lowrange,highrange)
print("Here is a random number {}".format(number))
