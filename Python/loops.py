print("looping over a list of elements : " , end = "")
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i , ", ", end = "") # prints numbers from 1 to 10 in a single line separated by commas
print()  # prints a new line after the loop  
print("looping over a range of elements : ", end = "")
# using range function to loop from 1 to 10 
# range(1, 11) generates a list of numbers from 1 to 10
for i in range(1,11):
    print(i, ", ", end = "")
print()  # prints a new line after the loop
print("looping over a range of elements with a step of 2 : ", end = "")
for i in range(1, 11, 2):  # looping with a step of 2
    print(i, ", ", end = "")  # prints odd numbers from 1 to 10 
print()  # prints a new line after the loop
print("looping over a string : ", end = "")
# looping over a string to print each character
s = "Hello, world!"
for i in s:
    print(i, " ", end = "")
print()  # prints a new line after the loop
print("looping over a list of names : ", end = "")
names = ["hassan", "ali", "sara", "ahmed", "fatima"]
for name in names:
    print(name, " ", end = "")