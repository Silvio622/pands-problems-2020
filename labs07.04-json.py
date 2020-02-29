# Silvio Dunst
'''
Using json module to save a data structure (Dict or List) 
If we want to store a more complicated data structure to a file, we should use either: 
a. JSON: Which will store the data structure in a human readable way. JSON is a standard way of storing objects, 
    you will see more on this later in the course. 
Python has a module called json, which has two functions: 
• dump(obj,fp); which writes a Dict or list to a file 
And 
• load(fp): which loads a data structure (Dict or list) from a file 
Or 
b. Pickle: Which will store the data structure in binary format (not human readable). 

3. Write a function that will store a simple Dict to a file as JSON. TEST IT 
'''
import json # import json(Java Script Object Notation) library
filename = "testdict.json" # create a string variable filename with a "testdict" file 
sample = dict(name = "Fred", age = 31, grades = [1, 34, 55]) # create a dictionary variable sample with keywords name,age and grades, gardes as list/array

def writeDict(obj): # create a function writeDict with return value as an object
    with open(filename, "wt") as f: # create/open write to a file "testdict.json" via filename variable
        json.dump(obj,f) # use the json function 
#test the function
writeDict(sample) # writes the dictionary sample in the testdict.json file
