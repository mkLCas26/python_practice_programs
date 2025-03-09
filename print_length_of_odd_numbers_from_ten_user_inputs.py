# B1 Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Initialize counter and list
counter = 0
odd_numbers = []

# While loop for 10 inputs
while counter < 10:
    counter += 1
    ten_numbers = int(input("Enter 10 numbers: "))

    # Determines odd numbers
    if ten_numbers % 2 != 0:                               
        odd_numbers.append(ten_numbers)

# Print length of odd numbers
print(len(odd_numbers))