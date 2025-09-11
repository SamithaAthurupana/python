from typing import List

from Library.share.arrow.gdb.gdb_arrow import ListTypePrinter

student_names = ["kalana", "pasan", "dasun"] #iterable
print(type(student_names))

for student in student_names:
    print(student)
print("\n ============")

student_names1 = ["kalana", "pasan", "dasun"]
student_iterator = student_names1.__iter__() #calling iterator dunder method to get an iterator

print(type(student_names)) # <class 'list'>
print(type(student_iterator)) # <class 'list_iterator'>
for student in student_names1:
    print(student)

print("\n ============__next__() call next value in list iter")
try:
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
    print(student_iterator.__next__())
except StopIteration as e:
    print(e)

print("\nEasy way to iter")
student_iterator2 = iter(student_names)

for student in student_names:
    print(student)


