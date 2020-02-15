# Silvio Dunst
# This program generates 10 random numbers print them out, then print out the top 3

# I will use a list to stor and manipulate the numbers

import random # imports the random function
# I programming the general case
howMany = 10 # integer variable with value 10
topHowMany = 3 # integer variable with value 3
rangeFrom = 0 # integer variable with value 0 range start by Position 0 in the list
rangeTo = 100 # integer variable with value 100 range ends by Position 100 in the list

numbers = []# list variable

for i in range(0, 10): # i is for index counting up, range is the list enrty from position 0 to 10, total 11 positions I think, loop goes 11 times
    numbers.append(random.randint(rangeFrom, rangeTo)) # add random numbers with random function, with random integer numbers(randint)
 # the range start with variable rangeFrom with value 0, the range ends with variable rangeTo with value 100
print("{} random numbers\t {}".format(howMany,numbers)) 
# I am keeping the original list may be I don't need to 
# I got the idea to sort and split the list from stackover flow
# https://stackoverflow.com/q/32296887

topOnes = numbers.copy() # copy the list numbers to the new list topOnes with the copy function
topOnes.sort(reverse = True) # sort the random numbers in reverse order start with the highest
print("The top {} are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))

