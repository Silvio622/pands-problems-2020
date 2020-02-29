'''
#  Silvio Dunst
# In this question we assume that the file count.txt exists, what happens the first time you run this program on a new machine 
# where count.txt does not exist?(answer: The program will throw an error, so)

# Write some code to check if the file exists. To do this we will need to import os.path and use the isfile() function.

# Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.
'''
import os.path # import the library os (Operation System) path functions
filename = "counts.txt" # create a new string variable with value "count.txt"
if not os.path.isfile(filename): # this function in os.path.isfile checks if the file exist in the root directory
    print("File does not exist") # if the file is not in the root directory (not True) this will be printed
    # initilazie the File here and write in the number 10
    #writeNumber(0)

# Use a try catch loop on the read (I think the best way).
# We will be covering exception handling later in the course, so don’t worry about this yet.

def readNumber(): # create a function readNumber
    try: 
        with open(filename) as f: #open the file "filename" when the file exist
            number = int(f.read()) # create a Integer variable "number" where the number in the file will be passed on
            return number # # returns the value in the file through the function readNumber()
    except IOError:
        # this file will be created when we write back
        # no file assumes first time running
        # ie 0 previous run
        return 0


