# B2 Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# First user input, initialize counter and other variables
first_input = int(input("Enter 10 numbers: "))
counter = 0

# While loop for user input and difference
while counter < 9:
    counter += 1
    other_inputs = int(input("Enter 10 numbers: "))

    first_input -= other_inputs

# Print difference
print(first_input)