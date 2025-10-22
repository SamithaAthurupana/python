import threading
from threading import Thread
import  time

def waiter_function(name:str,duration:int):
    print(f"Function {name} is starting")
    time.sleep(duration)
    print(f"function {name}is ending")


thread =Thread(target=waiter_function,args=("worker",6))
thread.start()
thread.join()
print("\n hello world")