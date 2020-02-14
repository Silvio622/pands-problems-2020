# Create an Dictionary Object called currentBook that has three attributes:
# Title , Author , Price
# Print out the dictionary object
# Print just the author of the currentBook
# Create a new attribute called ISBN (with some value)
# Print out all the values in the currentBook (using for loop)

currentBook = {
    "Title":"Harry Potter eats his dinner",
    "Author": "Just Kidding Rowling",
    "Price": 12
    }
# print dictionary object
print (currentBook)

# print just the author
print (currentBook["Author"])

# create and set a attribute ISBN
currentBook["ISBN"] = "123455"

# user for loop to iterate through the currentBook's values
# notice the order the for loop gives the values.
print("the current values has these values:")
for value in currentBook.values():
    print(" => {}".format(value))
