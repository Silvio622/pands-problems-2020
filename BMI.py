# BIM.py Calculates the BMI of 
# the BMI is calculted persons height in centimeters and the weight in Kilogramm
# the output BMI is weight divided by their heights in metres squared

# Weigth = 65
Weight = float(input("Enter the Weight of the Person in kg:  "))

# Heigth = 180
Height = float(input("Enter the Height of the Person in cm:  "))

BIM = Weight / (Height * Height / 10000 )
print("The BMI is", BIM,"for this person")
