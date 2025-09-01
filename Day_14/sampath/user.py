class User:
    def __init__(self, nic, age, name):
        self.__nic = nic    # Encapsulation - private object variable
        self.__age = age
        self.__name = name

    def set_nic(self, nic):
        self.__nic = nic

    def get_nic(self):
        return self.__nic

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):  # overriding parent class object __str_method__
        return f"User name - {self.__name} - User age - {self.__age} - Nic - {self.__nic}"


'''user_01 = User("1234567890V", 34, "sadun")
print(user_01.get_age())
user_01.set_age(19)
print(user_01.get_age())'''
# here is the getters and setters usage.
