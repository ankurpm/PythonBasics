
l1 = [10,20,30,40,50,60,70,80]

#access first element in the list
print(l1[-1])

#change values at a particular index
l1[1] = 22
print(l1)
#insert an element
l1.append(90)
#print("printing list l1",l1)

l2 = l1
#print("printing list l2",l2)
l2[1] = 23
# print("printing list l2",l2)
# print("printing list l1",l1)

#other ways to copy your list
l3 = l1.copy()
# print("printing list l3",l3)
l3[1] = 24
# print("printing list l3",l3)
# print("printing list l1",l1)

#slice operation
l4 = l1[:]
# print("printing list l4",l4)
# print("printing list l1",l1)
print("printing list l4",l4)
l4[2:5] = [11,12,13,14] #from index 2 till index 5(before index 5)
print("printing list l4",l4)
l4[2:5] = []
print("printing list l4",l4)

