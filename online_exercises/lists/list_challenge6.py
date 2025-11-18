'''
“Write a program to concatenate two lists and return a sorted list”
Example:
list1 = [21,23,14,5]
list2 = [34,2,22,55]

Output : [2,5,14,21,22,23,34,55]
'''
list1 = [21, 23, 14, 5]
list2 = [34, 2, 22, 55]

combined = list1 + list2
combined.sort()

print(combined)
