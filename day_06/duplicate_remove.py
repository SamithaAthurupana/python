'''elements = [1, 1, 2, 2, 3, 5, 6, 7, 7, 8]
print(elements, end=" ")
print("\n")
elements.sort()

#wrong
for i in elements:
    if elements[:] == elements:
        for j in elements:
            elements.pop()
            print(elements, end=" ")'''

elements_new = [1, 1, 9, 9, 9, 5, 6, 7, 7, 8]

unique_elements = []

for element in elements_new:
    if element not in unique_elements:
        unique_elements.append(element)
elements_new = unique_elements[:]

print(elements_new)
