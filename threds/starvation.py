import threading


def infinite_loop():

    while True:
        print("I m starving others")

def rand_function():
    print("Hello world")


threading.Thread(target=infinite_loop).start()
threading.Thread(target=rand_function).start()