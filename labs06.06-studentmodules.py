# Silvio Dunst
# now we can put in the created modules

students =[] # create a list/array variable student

# Functions
def displayMenu(): # create/ define a function with the name "displayMenu"
    print("What would you like to do?")
    print("\t (a) Add new student") # \t is a text format for tabular
    print("\t (v) View student")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip() # create a choice local variable as User input as string with strip function to clear leading and trailing spaces
    return choice # returns a value in the local variable choice

def doAdd(): # create a new function with the name "doAdd"
    currentStudent = {} # create a new variable currentstudent as a Dictionary
    currentStudent ["name"] = input("enter name :") # create a Keyword "name" use a user input to put in a value string in keyword name
    currentStudent ["modules"] = readModules() # create a Keyword "modules" and calls the function "readModules()"
    
    students.append(currentStudent) # add the keywords "name" and "modules" with the values to a list

def readModules(): # create a new function with the name "readModules"
    modules = [] # create a new local list/array variable "modules"
    moduleName = input("\tEnter the firts Module name (blank to quit): ").strip() # create a new local moduleName string variable, 
    # form user input with strip function to cut out leading and trailing spaces
    while moduleName != "": # create a while loop, loops so long something is written from the user (not equal empty space)
        module = {} # create a local dictionary variable variable "module"
        module ["name"] = moduleName # put in a keyword name in the dictionary module with the string value from the user input
        #I am not doing error handling
        module ["grade"] = int(input("\t\tEnter grade:")) # put in a keyword grade in the dictionary module with a Integer value from the user input
        modules.append(module) # add the values from keyword name and grade from the dictionary module to the variable modules list
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules  # returns the values in the list/array variable "modules"

def displayModules(modules): # create a function displayModules with a input modules
    print("\tName  \tGrade") # print out the Name and Grade of the input variable modules
    for module in modules: # create a foor loop with a new local variable module and loops through the variable list/array modules
        print("\t{} \t{}".format(module["name"], module["grade"])) # prints the name and grade in a new text line
        print(modules)
        

def doView():
    for currentStudent in students: # create a for loop with a new local variable currentStudent and loops through the variable list/array students
        print(currentStudent["name"]) #  prints the name of the student list/array
        displayModules(currentStudent["modules"]) # calls the function "displayModules"
       
    print(students) # prints out the list /array students

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


