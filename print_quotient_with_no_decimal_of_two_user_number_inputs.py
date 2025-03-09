# B2 Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Ask for user input
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

# Print quotient w/o decimals (whole number only)
if num2 == 0:
    print("Undefined")
else: 
    quotient = num1 / num2
    print(int(quotient))