# Silvio Dunst
# Reading a dict from a file 
# 4. Write a function that will read in a dict object from file. TEST IT 

import json # import json(Java Script Object Notation) library
filename = "testdict.json" # create a string variable filename with a "testdict" file 

def readDic(): # create a function readDict with 
    # this will throw an error if the file not exist
    # it should readly just return an empty dictionary
    # we can do this later
    with open(filename) as f: # open the file "testdict.json" via filename variable
        return json.load(f)

# Test function
somedict = readDic() # read the dictionary sample from the testdict.json file in the variable somedict
print(somedict) #prints out the value from the dictionary variable sample





