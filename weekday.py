# Silvio Dunst
# Program that outputs today is a weekday or not

import datetime # imports date time function

now = datetime.datetime.now() # create a new variable for weekday
weekday =  now.weekday() # create a new variable for (weekday), extract the weekday out of the now function

#if weekday >= 0 & <= 4 : # weeday 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
#    print("Yes, unfortunately today is a weekday")

# now.weeday()function return Value 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
if weekday ==0:
    print("Yes, unfortunately today is a weekday")
elif weekday ==1:
    print("Yes, unfortunately today is a weekday")
elif weekday ==2:
    print("Yes, unfortunately today is a weekday")
elif weekday ==3:
    print("Yes, unfortunately today is a weekday")
elif weekday ==4:
    print("Yes, unfortunately today is a weekday")
else:
   print("It is the weekend, yay!")



