# B1 Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Initialize Counter and other variables
counter = 0
sum = 0

# While Loop for 10 user inputs and sum
while counter < 10:
    counter += 1
    ten_numbers = int(input("Enter 10 numbers: ")) 

    sum += ten_numbers

# Print sum
print(sum)