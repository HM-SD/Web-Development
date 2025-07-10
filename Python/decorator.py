def announce(f):
    def wrapper(a, b):
        print("about to call function:", f.__name__)  # f.__name__ gives the name of the function
        print("if a < b, the wrapper function will swap the arguments so that the neumerator is always greater than the denominator")
        if a < b:
            a, b = b, a  # Swap the arguments if a is less than b
        result = f(a, b) # Call the original function with the possibly swapped arguments
        print("function", f.__name__, "called successfully")
        return result   # Return the result of the function call
    return  wrapper  # Return the wrapper function 
# This code defines a decorator that modifies the behavior of a function to ensure that the first argument is always greater than or equal to the second argument before performing division.

@announce
def div(a, b):
    return a/b;


# Example usage of the decorated function
result = div(10, 2)  # This will call the wrapper function first
print("Result of division:", result)
