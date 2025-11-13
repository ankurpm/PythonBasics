from os import remove

student = { "name": "Jack", "city":"London", "age":30, "result": "pass" }
print( student["name"])
print( student["city"])
print( student["age"])

#not present key
#print( student["country"])
#print( student.get("country"))
#print( student.get("name"))

#update any value
student["country"] = "USA"
#print(student)
student["country"] = "UK"
print(student)

#remove from dictionary
#pop
student.pop("country")
print(student)
#Del
del student["city"]
print(student)
#remove all elements
student.clear()
print(student)
del student
print(student)

