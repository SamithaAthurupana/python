# special note----
numbers = ["a","d"]
for i in range(len(numbers)-2):
    numbers.append(i)
print(numbers)
#-------

elements = [i for i in range(10)]
print(elements)

new_elements = [i ** 2 for i in range(10)]
print(new_elements)

name = "test"
name_element = [name for i in range(10)]
print(name_element)

new_odd = [i for i in range(10) if i % 2 != 0]
print(new_odd)

