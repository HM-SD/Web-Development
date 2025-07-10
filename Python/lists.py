#define list of names
names = ["hassan", "ali", "sara", "ahmed", "fatima"]
print("names : " , names[3])
#Methosds of appending and removing elements
names = names + ["sohail"] #appending a new name to the list
print("After appending: ", names)
names.append("Drar")  #appending another name using append method
print("After appending using append method: ", names)
names.remove("sara")  #removing a name from the list
print("After removing sara: ", names)
#sorting the list
names.sort()  #sorting the list in ascending order according to their precedence in ASCII table
print("After sorting: ", names)