# Read out of a User Input text every second Character

# Insert a User Input text like "The quick brown fox jumps over the lazy dog "
UserText = str (input("Type in a Text:  "))
# Print out User Text with every second Character
# print (UserText[0:42:2])
print (UserText[::-2])
# Print out in reverse order
# print (UserText[42:0:-2])