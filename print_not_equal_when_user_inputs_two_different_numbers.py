# B2 Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Ask for user input
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

# If-else statement to determine if the numbers are not equal
if num1 != num2: 
    print("Not Equal")
else:
    print("Equal")