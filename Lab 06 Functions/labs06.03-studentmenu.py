# Silvio Dunst
# Write a function that prints out a menu of commands we can perform, ie add, view and quit. The function should return what the user chose. 
# Test the function. We don’t need to worry about error handling yet

# Functions
def displayMenu(): # create/ define a function with the name "displayMenu"
    print("What would you like to do?")
    print("\t (a) Add new student") # \t is a text format for tabular
    print("\t (v) View student")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip() # create a choice local variable as User input as string with strip function to clear leading and trailing spaces
    return choice # returns a value in the local variable choice
def doAdd(): # create/ define a function with the name "doAdd"
    # we fill this in later
    print("in adding")
def doView(): # create/ define a function with the name "doView"
    # we fill this in later
    print("in viewing")

    # Main program
choice = displayMenu() # create a global variable choice and put in the displayMenu function in it (the four print lines)
while (choice != 'q'): # the while loop loops as long the user doesn't put in "q"
    # we could do this with lambda functions
    # I am keeping it this basicfor the moment
    if choice == 'a': 
        doAdd() # if choice is equal to "a" then call the doAdd function
    elif choice == 'v':
        doView() # if choice is equal to "v" then call the doView function
    elif choice == 'q':
        print("\n\nplease select either a, v or q") # \n\n is a text format removes the input
    choice = displayMenu()
