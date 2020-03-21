# Silvio Dunst
# a different way to dealing with a users choice

# Functions
def displayMenu(): # create a function displayMenu
    print("What would you like to do")
    print("\t(a) Add a new student") # \t is atext format tabular
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip # create a choice local variable as User input as string with strip function to clear leading and trailing spaces
    return choice

def doAdd(): # create a function doAdd
    print("do Add")

def doView(): # create a function doView
    print("do view")

def doNothing(): # create a function doNothing
    pass # The pass statement is a null operation; nothing happens when it executes

# the dictionary what maps a letter to a function
choiceMap = {       # create a dictionary variable choiceMap
    'a': doAdd,     # create a Keyword a with the value as a function doAdd
    'v': doView,    # create v Keyword a with the value as a function doView
    'q': doNothing  # create q Keyword a with the value as a function doNothing
}
# Main Program
choice = displayMenu() # create a new variable choice the value is the function displayMenu
while(choice != "q"): # create a while loop it loops so long q is not typed in from the user
    if choice in choiceMap: # in means checks for the members of the dictionary choiceMap like 'a','v','q'
        # run the function
        choiceMap[choice]()
    else: # use did not enter something valid
        print("\n\nplease select either a, v or q")
    
    choiceMap = displayMenu()



