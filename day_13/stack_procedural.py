# last in first out - LIFO
# stack call --> when we think program, calling structure equal this proceed

'''stack = [3,5]

def push(item):
    stack.append(item)
    return stack

user_input = int(input("Enter number: "))
print(push(user_input))


def pop():
    if stack:
        x = stack[-1]
        del stack[-1]
        return x
    return None


print(pop())
print(stack)'''

stack = []

def push(elem):
    stack.append(elem)

def pop():
    # return the popped value
    if len(stack) > 0:
        val = stack[-1]
        del stack[-1]
        return val
    raise Exception("Stack is Empty")


try:
    push(2)
    push(5)
    push(9)
    print(stack)
    pop()
    print(stack)
except Exception as e:
    print(e)

