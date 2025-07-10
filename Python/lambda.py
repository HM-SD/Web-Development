types = [
         {"name": "carrot", "type": "vegetable"},
         {"name": "apple", "type": "fruit"},
         {"name": "horse", "type": "animal"}
         ]

"""def f(item):    #function takes a dictionary item as input
    # This function returns the value associated with the 'name' key in the dictionary item
    return item["name"]

print("Original list:", types)
types.sort(key = f)     # Sort the list by the 'name' key using the function f
print("Sorted by name:", types)
"""

#Another way to sort the list by the 'name' key using a lambda function
#lambda function is an anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not reused elsewhere.
print("Original list:", types)
# The lambda function takes a dictionary as input and returns the value associated with the 'name' key in the dictionary item 
types.sort(key = lambda item: item["name"])

print("Sorted by name using lambda:", types)


