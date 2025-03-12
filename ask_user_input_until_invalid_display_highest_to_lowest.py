# B4 Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

"""
Initialize empty lists or needed variables
While loop for user input
    Try-except for determining invalid inputs
    Storing number inputs in a list
    Use sort() function for the descending order
    Print list of number inputs in descending order
"""

numbers = []
num = 0

while True:
    user_input = input("Enter a number: ")
    try:
        num = float(user_input)
        numbers.append(num)
        numbers.sort()
        numbers.reverse()
        print(numbers)
    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")