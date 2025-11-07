'''
List Manipulation and Methods (Intermediate)
Task: Start with an empty list named inventory.
a. Use the .append() method to add the items 'apple', 'banana', and 'cherry' one by one.
b. Use the .insert() method to add 'orange' at the second position (index 1).
c. Use the .remove() method to remove 'banana'.
d. Use the .pop() method to remove and print the last item in the list.
e. Print the final inventory list.
'''

# Start with an empty list
inventory = []

# a. Add items using .append()
inventory.append('apple')
inventory.append('banana')
inventory.append('cherry')

# b. Insert 'orange' at the second position (index 1)
inventory.insert(1, 'orange')

# c. Remove 'banana'
inventory.remove('banana')

# d. Remove and print the last item using .pop()
last_item = inventory.pop()
print("Removed last item:", last_item)

# e. Print the final inventory list
print("Final inventory:", inventory)
