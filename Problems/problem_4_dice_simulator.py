"""
Randomly returns two numbers between 1 and 6
"""
import random
# Generate two random integer between 1 and 6 (inclusive)
number1 = random.randint(1, 6)
number2 = random.randint(1, 6)
# Tell the user what the result was
print(f"You rolled a {number1} and a {number2}.")