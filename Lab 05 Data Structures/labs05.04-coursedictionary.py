# Silvio Dunst
# Write a program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data.
# The number of course she has could change.
# We can hard code the values in this dict for this example

student = { # create a new Dictionary variable student
    "name": "Mary", # first keyword "name" with the value "Mary" as a string
    "modules": [    # second keyword "modules" with a value as a List 
        {           # the first list element/array is a new Dictionary nested in
            "courseName": "Programming", # the new nested Dictionary has keyword "courseName" as None variable with value "Programming" as string
            "grade": 45 # the new nested Dictionary has second keyword "grade" as value "45" as Integer
        },
        {
           "courseName": "History", # the new second nested Dictionary has keyword "courseName" as None variable with value "History" as string 
           "grade": 99 # the new second nested Dictionary has second keyword "grade" as value "45" as Integer
        }
    ]
}
print("Student {}".format(student["name"])) # prints the dictionary keyword value out of the first main Dictionay Student
for module in student["modules"]: # create a new Variable (Module) in the for loop, loop the value of the dictionary student keyword (modules)
                                  # as a list with 2 new dictionaries with the values of the two keywords "courseName" and "grade"
    print("\t{} \t: {}".format(module["courseName"], module["grade"])) # \t means it will be printed in the new line
    