# B2 Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Initialize counter and empty list
counter = 0
even_numbers = []

# While loop for user input
while counter < 10:
    counter += 1
    ten_numbers = int(input("Enter 10 numbers: "))
    
    # Determining even numbers
    if ten_numbers % 2 == 0:
        even_numbers.append(ten_numbers)

# Print length of even numbers
print(len(even_numbers))