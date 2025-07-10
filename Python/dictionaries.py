types = {"apple": "fruit", "potato": "vegetable", "dog": "animal", "flu": "disease"}
print(types["apple"])
types["banana"] = "fruit" #adding a new key-value pair
print(types["banana"])
# Deleting a key-value pair
del types["dog"]
print(types)
#change the value of a key
types["flu"] = "virus"
print(types["flu"])
# Check if a key exists
if "apple" in types:
    print("Apple is in the dictionary.")
