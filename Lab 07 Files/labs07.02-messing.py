# Silvio Dunst
# Write a program that counts how many times it was run.
# For this exercise will have to store data outside of memory, and that is accessible each time the program is run, 
# (this is called persistent data). We would normally use a database for something like this, but we can use a file.
# To make life easier lets assume that the file already exists. So we can just read the current count from it then overwrite it 
# with the new count. Create a file called count.txt and put in 0 into it

# a. Write a function that reads in a number from a file that already exists (count.txt). 
# test the program by calling the function and outputting the number.

filename = "count.txt" # create a string variable "filename" with the string values "count.txt"
def readNumber(): # create a function "readNumber"
    with open(filename) as f: # open a text file with name "count.txt" via variable filename
        number = int(f.read()) # create a Integer variable "number" where the number in the file will be passed on
        return number # returns the value in the file through the function readNumber()
# test it
num = readNumber() # the value of local variable number is passed out of the function readNumber() and written in new variable num
#print(num) # prints out the value in the file

def writeNumber(number): # # create a function "writeNumber" and put in a Input variable number
    with open(filename, "wt") as f: # write in a text file with name "count.txt" via variable filename
        # writes takes a string so we need to convert 
        f.write(str(number))
# test it
#writeNumber(3) # writes the value 3 now in the file

# Main Program
numcount = readNumber() # the value of local variable number is passed out of the function readNumber() and written in new variable numcount
numcount +=1 # every time the readNumber function is called the count value of numcount goes up by 1 like "numcount = numcount + 1"
print("we have run this program {} time".format(numcount))# prints how often the file was opened
writeNumber(numcount) # writes in the file the value how often it was opened

