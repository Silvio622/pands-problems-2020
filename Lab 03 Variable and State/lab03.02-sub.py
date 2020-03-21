# Program to subtract one number from another

# inputs reads in a string so we need to convert it into to a integer (int)
# so we can perform mathematical operations

x = int(input("Enter first number: "))# converts the input to a Interger
y = int(input("Enter second number: "))# converts the input to a Interger
answer = x-y
print("{} minus {} is {}".format(x, y, answer))