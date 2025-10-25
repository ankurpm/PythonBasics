l1 = [10,20,30,20,40,50,30,20,60,60,70,80]
#remove from a certain index
l1.remove(50)
print(l1)

l1.pop()
print(l1)
#if we remove something thats not there in the list
#l1.remove(150)
l1.pop(9)

#count a value in list
print(l1.count(20))

#sort the list
print("l1 before sort: ", l1)
l1.sort()
print("l1 after sort: ", l1)

l1.reverse()
print("l1 after reverse: ", l1)

diff_list = [1,"hi",True]
#diff_list.sort()
diff_list.reverse()
print("list after reversing: ", diff_list)


