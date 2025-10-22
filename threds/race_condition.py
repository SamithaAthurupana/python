import threading
import time
from threading import Thread

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter

    for i in range(1000):
        with lock:
            current = counter
            time.sleep(0.01)
            counter = current + 1

def main():
    global counter
    thread1= threading.Thread(target=increment_counter)
    thread2=threading.Thread(target=increment_counter)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print(counter)

main()

