# B2 Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Ask user input
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# Divide and print remainder
if num2 == 0:
    print("Undefined")
else:
    remainder = num1 % num2
    print(remainder)