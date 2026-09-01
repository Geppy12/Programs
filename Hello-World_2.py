# BAI 1150: Introduction to Python Programming for AI!
# Todd Simpson - August 25th, 2026
# This is a simple Python program that prints "Hello, World!" to the console.

# --------------------------------------------------
# Program: Extending Hello World with a Library
# Purpose: Demonstrate printing and importing a module
# --------------------------------------------------

# Import Python's random module.
# This gives our program access to additional functions.
import random

# Display the traditional Hello, World! message.
print("\nHello, World!\n")

# --------------------------------------------------
# Part 2: Extending the Program with a Library
# --------------------------------------------------

# Create a list of possible greetings.
greetings = [
    "Welcome to Python!\n",
    "Python is ready!\n",
    "Let's start programming!\n",
    "Python is number 1 on Tiobe Index!\n",
    "Hello from the Python community!\n"
]

# Use the random module to select one greeting.
message = random.choice(greetings)

# Display the randomly selected greeting.
print(message)

# Add a blank line after the output.
print()

# END OF FILE