# Silvio Dunst
# the with statement automaticallly close the file
# when it is finished with it

#with open("test-a.txt") as f: # open a file with a with statement as a structure of variable f
#    data = f.read() # create a variable data and read something in
#    print(data) # print the value of the variable data

# this is the same as 
#f = open("test1.txt")
#data = f.read()
#print(data)
#f.close()
# a.Look at the program above, assuming that the file test-a.txt does not exist. What will happen when the program runs?
# error appears can't find the file

#b.Look at the program below, Assuming the file test-b.txt does not exist, what will be outputted to the console when this program is run?
# create a file in the same root with the name "test-b" as a text file and writes in "test b", prints out the amount of charcters 7
with open("test-b.txt", "w") as fb: # create and write to a file with a with statement as a structure of variable fb
    datab = fb.write("test b\n") # create a variable datab and write "test b" (\n jumped to a new line in the file)
    print(datab) # prints the amount of the characters in datab variable =7

#c. What will the contents of the file test-b.txt be when this program is run?
# overwrite the file context with "another line" and prints out the amount of characters
#d. Look at the modified program below, what will the contents of the file be after this program is run.
# put the new test "another line" after the previous one "test b" in a new line
with open("test-b.txt", "a") as fc: # create and write to a file with a with statement as a structure of variable fc
    datab = fc.write("another line \n") # overwrite variable datab and write "another line" (\n jumped to a new line in the file)
    print(datab) # prints the amount of the characters in datab variable = 14