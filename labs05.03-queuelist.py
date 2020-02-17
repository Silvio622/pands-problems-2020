# Silvio Dunst
# Create a program that puts 10 random numbers into a queue(list), the program should then output all the values in the queue,  
# then take the numbers from the queue one at a time, print it and the current numbers still in the queue.

import random # imports the random function
queue = [] # create a new List variable
numberOfNumbers = 10 # create a new Integer variable with value 10
rangeTo = 100 # create a new Integer variable with value 100

for n in range(0,numberOfNumbers): # for loop n is a new Variable, the range keyword creates a "list", (0=starts on Position 0),
                                   # (ends numberOfNumbers = 10, 10-1 ends on Position 9)
    queue.append(random.randint(0,rangeTo)) # in every loop (10 times) writes a new random integer in the list from 0 to (rangeTo variable =) 100

print("queue is {}".format(queue))

# Does not run from this point yet
while len(queue) != 0: # while loop, loops the amount of time of the elements/array in the queue list variable so long elements in the list

    currentNumber = queue.pop(0) # create a new variable (currentNumber) .pop keyword reduce elements form the list variable
                                 # when all the elements are gone in the queue list variable the loop stops executing
    print("current Number is {} and the queue is {}".format(currentNumber, queue))
# while loop ends here
# when while loop finished
print("the queue is now empty")
