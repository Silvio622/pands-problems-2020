# Silvio Dunst
# We can now write the function doAdd(). So we need to think what we want this to do.
# a. Read in the students name (that is straightforward) 
# b. Read in the module names and grades (this is a bit more complicated so lets put this in separate function and think about it by itself,  
# c. Test this function, it creates a student dict, we can print that out. 
# d. We should add the student dict to an array (we will use a global array for the moment) 
# e. Test this. 

students =[] # create a list/array variable student

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
def doAdd(): # create a new function with the name "doAdd"
    currentStudent = {} # create a new variable currentstudent as a Dictionary
    currentStudent ["name"] = input("enter name :") # create a Keyword "name" use a user input to put in a value string in keyword name
    currentStudent ["modules"] = readModules() # create a Keyword "modules" and calls the function "readModules()"
    
    students.append(currentStudent) # add the keywords "name" and "modules" with the values to a list

# test
doAdd() # calls the doAdd function
doAdd() # calls the doAdd function
print(students) # prints out the list variable students

