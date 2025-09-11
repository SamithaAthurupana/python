class Number_Generator:
    def __init__(self, num:int):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration
        self.current += 1
        return self.current

number_generator = Number_Generator(10)
number_generator = iter(number_generator)

print(next(number_generator))
print("------------------")
for i in number_generator:
    print(i)

for i in Number_Generator(6):
    print(i)


