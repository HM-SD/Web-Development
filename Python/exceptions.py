import sys 
try:
    x = int(input("Enter a number: "))  # Get user input and convert it to an integer
    y = int(input("Enter another number: "))  # Get another user input and convert it to an integer 

except ValueError:  # Catch the ValueError if input is not a valid integer
    # Handle the case where input is not a valid integer
    print("Error invalid input. Please enter valid integers.")
    sys.exit(1)

try:  # Attempt to perform division
    result = x / y  # Perform division

except ZeroDivisionError:   # Catch the ZeroDivisionError if y is zero
    # Handle the case where division by zero is attempted
    print("Error: Division by zero is not allowed.")
    sys.exit(1)

print(f"{x} / {y} = {result}")  # Print the result of
