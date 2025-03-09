# B2 Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Initialize empty list
no_zero_five = []

# For loop to print numbers from 0-100
for x in range(0, 100):
    if x % 10 != 0 and x % 5 !=0:         # Determines number not ending in 0 and 5 and excludes those that are ending in 0 and 5
        no_zero_five.append(x)

# Print list
print(no_zero_five)