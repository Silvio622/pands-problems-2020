# Silvio Dunst
# Create a tuple that stores the months of the year, 
# from that tuple create another tuple with just the summer months (May, June, July),
#  print out the summer months one at a time.

# Tuples 
months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December" 
)
summer = months[4:7] # Create a new Tuples (summer), copies the elements/Array from Position 4(May) til Position 7-1 Position 6(July) 
                    # in the new Tuples summer 7-1 the real Position
for month in summer: # Create a new Tuples (month), loops the amount of the elements/array Positions in the tuples summer
    print(month) # prints out the new Tuple month 

