# This program reads in a string and strips
# any leading or trailing spaces
# It also converts all the letters to lower case
# this program also outputs the length of the original string
# and the normalised one

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower() # strips out any leading or trailing space and put sentence in lower case

lenghtOfRawString = len(rawString) # counts the spaces and characters in the rawString variable from the user input
# before strips any leading and trailing characters
lenghtOfNormalised = len(normalisedString) # counts the spaces and characters in the normalisedString variable
# after it was stripped from user input
                                              
print("That String normalised is :{}".format(normalisedString)) # normalised String without leading or trailing spaces in lower case
print("we reduced the input string from {} to {}".format(lenghtOfRawString, lenghtOfNormalised)) # counts the characters before and after strip
# of leading and trailing spaces

