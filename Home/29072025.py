'''
arr = [12,25,64,22,11]
print(arr)
allways_five = len(arr)
empty_list = []

for i in range(allways_five):
    for j in range(0, allways_five - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    empty_list += arr

print(empty_list)

#example usage
for i in range(0,5):
    print(i, end=", ")

'''

numbers = [12, 25, 64, 22, 11]  # Original list
n = len(numbers)

i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if numbers[j] > numbers[j + 1]:
            # Swap the two numbers
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        else:
            pass  # Do nothing if already in correct order
        j += 1
    i += 1

print("Sorted list:", numbers)
