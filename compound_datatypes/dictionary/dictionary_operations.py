student = { "name": "Jack", "city":"London", "age":30, "result": "pass" }

#find length
#print(len(student))
#convert to string
x = str(student)
#print(x)
#print(type(x))
#copy function

student2 = student.copy()
#print(student2)
student["city"] = "Delhi"
#print(student)
#print(student2)

#for loop on dict
for k, v in student.items():
    print(f"key is {k} , value is {v}")

for k in student.keys():
    print(f"key is {k} ")

for v in student.values():
    print(f"value is {v}")


