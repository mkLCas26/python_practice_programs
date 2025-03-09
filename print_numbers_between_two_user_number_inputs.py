# B2 Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Ask user input 
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# For loop to print numbers between two user inputs
for x in range(num1 + 1, num2):
    print(x)