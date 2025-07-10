s = "Hello, world!" 
print(s[5])
#s[5] = "W"  # This will raise an error because strings are immutable
#to change a string, you need to create a new one
s = s[:5] + "W" + s[6:]  # This creates a new string with the change
print(s)
list = ["hassan", "Mohammed", "Sohail"]     #can be changed (mutable)
print(list[0] + " " + list[1] + " " +  list[2])
list[0] = "Ahmed"  #changing the first element
print(list[0] + " " + list[1] + " " +  list[2])
tuble = ("hassan", "moahammed", "sohail")    #cannot be changed (immutable)
print(tuble[0] + " " + tuble[1] + " " +  tuble[2])
#tuble[0] = "Ahmed"  # This will raise an error because tuples are immutable
#to change a tuple, you need to create a new one    
tuble = ("Ahmed", "Mohammed", "Sohail")  # This creates a new tuple with the change
print(tuble[0] + " " + tuble[1] + " " +  tuble[2])


