# Silvio Dunst
# Write a program that reads in a text file and outputs the number e's' it contains. 
# The program should take a filename from an argument on the command line

Userfilename = input(str("Enter a name for a file like (moby-dick): ").strip()) # create a variable User input and the user can give the file a name

filename = "{}.txt".format(Userfilename) # create a variable filename with the {Userfilename}

with open(filename,"w") as f: # create/write a file as a filename
    for writeline in range(0, 116960): # counter loop the index writeline counts 116960 time starting by 0
        f.write("e\n")

with open(filename, "r") as f1: # read a file as a filename
      
   arrays = len(f1.readlines()) # create a variable arrays and read out the amoo
   print(arrays)





