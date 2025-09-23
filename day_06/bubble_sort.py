# watch bro code channel
arr_length = [6, 9, 3, 4, 6, 8, 1]
print("print before Sort")
print(arr_length)

# outer loop identify index using length - 1
for i in range(len(arr_length) - 1):
    # Controls how many times to compare in each pass.
    # range(total_elements - pass_number - 1)
    for j in range(len(arr_length) - i - 1): # last element already sorted. we don't need try to sort. that's why -i
        if arr_length[j] > arr_length[j + 1]:
            arr_length[j], arr_length[j + 1] = arr_length[j + 1], arr_length[j]

print("print after Sort")
print(arr_length)


unsorted_list = [6, 9, 3, 4, 6, 8, 1]
arr_length = len(unsorted_list)

'''
print("print before Sort")
print(unsorted_list)

for i in range(len(unsorted_list) - 1):
    print(i)
    print(unsorted_list)
    for j in range(len(unsorted_list) - 1 -i): # last element already sorted. we don't need try to sort. that's why -i
        print("=====================")
        print(j)
        print(f"first element {unsorted_list[j]} second element {unsorted_list[j + 1]}")
        if unsorted_list[j] > unsorted_list[j + 1]:
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
            print(f"first element {unsorted_list[j]} second element {unsorted_list[j + 1]}")
        print("=====================")
print("print after Sort")
print(unsorted_list)
'''