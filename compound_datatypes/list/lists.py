from distutils.command.config import dump_file
from os import supports_follow_symlinks

# student1 = 70
# student2 = 80
# student3 = 90
#
# average = (student1 + student2 + student3) / 3
# print(average)

student_marks = [10,20,30,40,50,60,70,80,50,30,58,56]
total_students = len(student_marks)
#print("total studetns are",total_students)
sum=0
#print("sum is value before for loop",sum)

for mark in student_marks:
    sum = sum+mark
#print("sum is value after for loop",sum)

average = sum/total_students
print("average marks are",average)







