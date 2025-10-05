class Classy:

    im_classy = "classy"

    def __init__(self):
        self.a = "samitha"
        self.b = 30

    def say_hello(self):
        print("say hello")

    def top_g(self):
        self.g = "Im TOP G"
        self.say_hello()

classy_object = Classy()
print(classy_object) # <__main__.Classy object at 0x00000206A9966F90>

print(classy_object.a) # samitha

classy_object.top_g() # without this print line will be false --> say hello
print(hasattr(classy_object, "g")) # True

if 'g' in classy_object.__dict__:
    print("yes i'm in")


# reflection and Introspection