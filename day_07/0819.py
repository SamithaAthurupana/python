'''array = ["A", "B", "C", "D"]

array2 = array[:]
array3 = array2[:]

del array[0]
del array2[0] #Nothing to happen
del array2[:] #delete all the references
del array3[1]

print(array3)

multi_type_arr = [22, "text", 1.01, None, True]
print(multi_type_arr)'''

'''
#make 10 to numbers in list
#get a new array and print first 4 array

new_arr = []
copy_arr =[]

for number in range(10):
    new_arr.append(number)
    copy_arr = new_arr[0:4] # copy first 4 values into copy_arr

print(new_arr)
print(copy_arr)
'''
'''
numbers = [x for x in range(10)] #[0,1,2,3,4,5,6,7,8,9]
numbers_copy = [] # Empty list
numbers_copy.append(numbers) #[0,1,2,3,4,5,6,7,8,9]
numbers_copy.append(numbers) #[0,1,2,3,4,5,6,7,8,9] , [0,1,2,3,4,5,6,7,8,9]
numbers_copy.extend(numbers)


print(numbers_copy[0])
print(numbers_copy[1][2:8])
print(numbers_copy)'''

'''
#print 1 to 100 2 to power numbers to empty list
copy_numbers = []
numbers = [number ** 2 for number in range(11)]
copy_numbers.append(numbers)
print(copy_numbers)'''

'''#print 1 to 100 2 to power numbers to empty list & check them module by 5
copy_numbers = []
numbers = [i ** 2 for i in range(100) if i % 5 == 0]
copy_numbers.append(numbers)

print(copy_numbers)
'''