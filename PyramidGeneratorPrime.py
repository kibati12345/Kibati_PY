# Name:Kibati omotosho
#  Date: May 25th, 2023
# App name: Leap year calculator(AppName)
# Description: App that calculates if a year is leap or not !
# if a year is leap or not


# Import the system function
from os import system

# Title
system("title Pyramid Generator(Prime) - oluwakibati")

# Constants
MIN, MAX = 2, 100

# Introduction
# DocString - multiline string
INTRODUCTION = """
======================
== Prime Numbers  ==
======================
"""


# Repeat the  whole app in case the user enters "r"
restart = "r"  # we want to enter the loop at least ONCE
while restart == "r":
    # Clear terminal
    system("cls")

    # print the banner and intro
    print(INTRODUCTION)

    # Validation loop - will repeat if an invalid height is given
    valid = False  # we want to enter the loop at least once
    while valid == False:

        # Ask for the height
        height = input(f"Enter a height from {MIN} to {MAX}: ")

        # Try to convert the height into an integer
        try:
            height = int(height)
            valid = True  # conversion worked
        except:
            valid = False  # conversion did not work

        # Error in case height is not numeric
        if not valid:
            print("Error - Input must be a whole number.")

        # Error in case the height is not in the valid range
        # if vs elif
        # or because we can't have a number that's both less than
        # the min and greater than the max
        elif height < MIN or height > MAX:
            print(f"Error - Height must be between {MIN} and {MAX}")
            valid = False  # invalidate the input

        # only gets here in case input is valid

    # Draw the Pyramid
    # Initialize count of prime numbers
    prime_count = 0

    for line_number in range(1, height + 1):
        if line_number > 1:
            is_prime = True
            for i in range(2, int(line_number ** 0.5) + 1):
                if line_number % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                prime_count += 1
                # Print asterisks -print as many asterisks as line number
                for asterisks in range(line_number):
                    print("#", end="")  # print them on the same line
                # Print the Pyramid line number
                print(line_number)
    print(f"There are {prime_count} prime numbers from {MIN} up to {height} ")

    # Exit prompt
    restart = input("Enter 'r' to restart: ")
