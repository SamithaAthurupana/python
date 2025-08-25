class ExampleClass:

    count = 0 # class variable

    def __init__(self,val = 1):
        self.val = val # instance variable
        self.val2 = 10
        ExampleClass.count += 1

    def __str__(self):
        return "test"

    def say_hello(self):
        self.hello = "Helloooo!"



test = ExampleClass()
print(ExampleClass.count)
test.z = 20
test.val = 30

test2 = ExampleClass() # when object is create, count also incresed
print(ExampleClass.count)

test.say_hello() #object call
print(test)

'''print(ExampleClass.count)
ExampleClass.count = 3
print(ExampleClass.count)'''
print(test.__dict__)