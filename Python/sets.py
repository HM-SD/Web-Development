#create an empty set
s = set() #used to store unique elements and does not allow duplicates
print("Empty set: ", s)
#add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(7)
#display the set
print("Set after adding elements: " , s)
s.add(5)  #adding a duplicate element, will not raise an error but will ignotre the addition of the duplicate element
#display after adding a duplicate element (5)
print("Set after adding a duplicate element: ", s)
#remove an element from the set
s.remove(3)
#display the set after removing an element
print("Set after removing an element: ", s)
#display the length of the set
print(f"The set has {len(s)} elements")



