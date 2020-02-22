# Silvio Dunst
# Write a function that prints out a menu of commands we can perform, ie add, view and quit. The function should return what the user chose. 
# Test the function. We don’t need to worry about error handling yet

def displayMenu(): # create/ define a function with the name "displayMenu"
    print("What would you like to do?")
    print("\t (a) Add new student") # \t is a text format for tabular
    print("\t (v) View student")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip() # create a choice local variable as User input as string with strip function to clear leading and trailing spaces

    return choice # returns a value in the local variable choice
    # Test function
choice = displayMenu() # create a global variable choice and put in the displayMenu function in it (the four print lines)
print("you chose {}".format(choice)) # print in the space the return local variable choice value in the diplayMenu function to the global variable choice

    