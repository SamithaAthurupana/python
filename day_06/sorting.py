letters = ["c", "z", "a", "d"]
print(letters)
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)

numbers = [1,2,3,5,6,8]
numbers2 = numbers
numbers[0] = 100

print(numbers)
print(numbers2)