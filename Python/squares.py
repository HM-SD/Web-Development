#importing the square and cube functions from the functions module
#import functions # or from functions import square, cube

#for i in range(100):
#    print(f"{i}^2 = {functions.square(i)}")

#for i in range(100):
#   print(f"{i}^3 = {functions.cube(i)}")

from functions import square, cube

for i in range(11):
    print(f"{i}^2 = {square(i)}")   

for i in range(11):
    print(f"{i}^3 = {cube(i)}")
