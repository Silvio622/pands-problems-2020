# Silvio Dunst
# A Program that reads in students unti the user inputs a blank an then prints them all out again

students = [] # a list variable

firstname = input("Enter firstname (blank to quit): ").strip() #Return a copy of the string with leading and trailing whitespace removed.

while firstname !="": # when firstname variale enrty has something written into execute the while loop
    student = {} # is a dictionary where the key words will be tracked not like lists the entry order
    student["firstname"] = firstname # writes the new firstname (variable) input Entry under the dictionary key word "firstname"
    lastname = input("Enter lastname:").strip() #Return a copy of the string with leading and trailing whitespace removed writes in new Variable
    student["lastname"] = lastname # writes the new lastname (variable) input Entry under the dictionary key word "lastname"
    students.append(student) # writes a new entry every time to the end of the list (Append object).
    # next student
    firstname = input("Enter firstname (blank to quit): ").strip() #Return a copy of the string with leading and trailing whitespace removed.

    print("here are the students you entered:")
    for currentStudent in students: # students list variable
        print("{} {}".format(currentStudent["firstname"], currentStudent["lastname"])) # prints out the dictionary inputs for first name 
        # and lastname


