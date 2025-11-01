#named tuples
from collections import namedtuple

from variables.python_variables import first_name

Student = namedtuple("Student", ["first_name", "last_name","location"])

john = Student(first_name="John", last_name="Smith", location="NY")

cory  = Student(first_name="Cory", last_name="Adams", location="TO")

print("FirstName is ",john.first_name)

print("FirstName is ",john[0])
john_new = john._replace(last_name="Wick")
print(john_new)

kat = Student("Kat", "Orange", "UU")
print(kat)
print(cory)