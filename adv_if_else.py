# 🔍 1. Number Category with Divisibility
# Problem:
# Ask the user to enter a number. Print:

# "Divisible by both 3 and 5"

# "Divisible only by 3"

# "Divisible only by 5"

# "Not divisible by 3 or 5"

# Taking user input
user_input = input('Enter a number: ')

# validating the input 
if not user_input.isnumeric():
    print('Enter a valid number')
    exit()

# converting user_input into integer
user_input= int(user_input)

# main program
if user_input % 3 == 0 and user_input % 5 == 0:
    print(f'{user_input} is divisible by both 3 and 5')
elif user_input % 3 == 0:
    print(f'{user_input} is only divisible by 3')
elif user_input % 5 == 0:
    print(f'{user_input} is only divisible by 5')
else:
    print(f'{user_input} is not divisible by both 3 and 5')

# -----------------------------------------------------------------------#------------------------------------------------------------#

# 🔍 2. Triangle Type Checker
# Problem:
# Input 3 sides of a triangle and determine whether it is:

# Equilateral (all sides equal)

# Isosceles (two sides equal)

# Scalene (all sides different)

# Also, check if the sides form a valid triangle using the triangle inequality rule.

# Taking all three sides of triangle as user input
side1 = input('Enter Side 1 ')
side2 = input('Enter Side 2 ')
side3 = input('Enter Side 3 ')

# Validating the user input
if not (side1.isnumeric() and side2.isnumeric() and side3.isnumeric()):
    print('Enter a valid number')
    exit()

# Converting the sides into integer
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

# Validating for positive values
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print('Sides must be greater than zero.')
    exit()

# Checking for triangle inequality rule
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:

    # Main program
    if side1 == side2 == side3:
        print("It's an Equilateral Triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("It's a Isosceles Triangle")
    else:
        print("It's a Scalene Triangle.")
else:
    print("Not a valid triangle based on triangle inequality.")

# -----------------------------------------------------------------------#------------------------------------------------------------#
