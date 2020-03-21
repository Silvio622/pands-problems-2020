# This program prints out a random fruit as a Tuples

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear') # writes variables in a Tuples (Array) shown in brackets

# we want a random number between 0 and lenght-1
index = random.randint(0, len(fruits)-1) # 0 is the first word in th elist on index position 0 
# len is the lenght amout of total list position minus 1 (4 Positions -1 = 3 ) list start with 0 Position

fruit = fruits[index] # pick the random index position from fruits list and write's it in the new variable fruit
print("A Random Fruit:{}".format(fruit)) # pick the fruit variable and writes it in the space
