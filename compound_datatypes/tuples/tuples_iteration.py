my_tuple = (10,20,30,40,50,60,70)

#for loop
#for i in my_tuple:
    #print(i)
#range function
for i in range(len(my_tuple)):
    print(my_tuple[i])

for i, value in enumerate(my_tuple):
    print(f"index={i}, value={value}")