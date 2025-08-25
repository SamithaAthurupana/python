class Stack:
    def __init__(self):
        self.__stack_list = [] # making stack list private __

    def push(self, elem):
        self.__stack_list.append(elem)

    def pop(self):
        if len(self.__stack_list) > 0:
            val = self.__stack_list[-1]
            del self.__stack_list[-1]
            return val
        raise Exception("Stack is Empty")


class AddingStack(Stack):  # sub class from Stack  --> inheritance

    def __init__(self):
        Stack.__init__()
        self.__sum = 0

    def push(self, elem): # method overriding
        self.push(self,elem)
        self.__sum += elem

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def pop(self):
        self.__count += 1
        return Stack.pop(self)

    def get_count(self):
        return self.__count


# select all and ctrl + / comment all

stack_1 = Stack()
stack_1.push(1)
stack_1.push(2)
stack_1.push(3)

counting_stack = CountingStack()

for i in range(20):
    counting_stack.push(i)
    counting_stack.pop()

print(counting_stack.get_count())

