# First in first out --> FIFO
'''class Queues:
    def __init__(self):
        self.__queues_list = []

    def put(self,elem):
        self.__queues_list.append(elem)

    def get(self):  # dequeue
        if len(self.__queues_list) > 0:
            return self.__queues_list.pop(0)  # remove first element
        raise Exception("Queue is Empty")


    def show(self):  # helper function
        return self.__queues_list

q = Queues()
q.put(10)
q.put(20)
q.put(30)

print(q.show())   # [10, 20, 30]

print(q.get())    # 10
print(q.get())    # 20
print(q.get())

print(q.show())   # [30]'''

class QueueError(Exception):
    pass

class Queues:

    def __init__(self):
        self.__queues = []

    def put(self, elem):
        self.__queues.insert(0,elem)

    def get(self):
        if self.__queues:
            val = self.__queues[-1]
            del self.__queues[-1]

            return val
        raise QueueError

    def get_queue(self):
        return self.__queues



class ChildQueue:
    def __init__(self):
        Queues.__init__(self)

    def get_size(self):
        return len(Queues.get_queue(self))

try:
    child_queue = ChildQueue()
    child_queue.put(1)
    print(child_queue.get_size())
except:
    print("Error")


try:
    restaurant_queue = Queues()
    restaurant_queue.put("Amal")
    restaurant_queue.put("kamal")
    restaurant_queue.put("Nimal")



    print("All the list..")
    for person in restaurant_queue.get_queue():
        print(person)
    print("\nfirst comer...")
    print(restaurant_queue.get())

except QueueError as e:
    print()
