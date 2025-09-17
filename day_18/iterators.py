from typing import List  # just importing List type hint (not used much here)

from Library.share.arrow.gdb.gdb_arrow import ListTypePrinter
# ⚠️ This import seems external, not needed for normal Python iterators.
# (Your code will work without this line.)

student_names = ["kalana", "pasan", "dasun"]  # a list (iterable)
print(type(student_names))  # <class 'list'>

for student in student_names:  # looping through list directly
    print(student)
print("\n ============")

student_names1 = ["kalana", "pasan", "dasun"]

student_iterator = student_names1.__iter__()  # manually call __iter__() → gives an iterator object

print(type(student_names)) # <class 'list'>
print(type(student_iterator)) # <class 'list_iterator'>
for student in student_names1:
    print(student)

print("\n ============__next__() call next value in list iter")
try:
    print(student_iterator.__next__())  # get first value
    print(student_iterator.__next__())  # get second value
    print(student_iterator.__next__())  # get third value
    print(student_iterator.__next__())  # No more items → raises StopIteration
except StopIteration as e:
    print(e)  # print empty message


print("\nEasy way to iter")
student_iterator2 = iter(student_names)  # using built-in iter() instead of __iter__()

for student in student_names:  # normal for loop again
    print(student)



