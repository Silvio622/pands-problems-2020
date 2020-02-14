# Check if one the number divides another

import datetime


p = 8 # Integer
m = 3 # Integer

if (p % m) == 0: # % sign is for Modulo or Remainder if the Result is True (no Remainder)
 print(p, "divided by", m, "leaves a remainder of zero.")

else:
 print(p, "divided by", m, "does not leaves a remainder of zero.")

print("I run no matter what")

time = datetime.datetime.now() # new variable
print(time)

date = time.date() # new variable
print(date)
