import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread


# def execute_sync_task(task_name:str, duration:int):
#     print(f"Starting task - {task_name}")
#     time.sleep(duration)
#     print(f"Ending task {task_name}")
#
# thread1 =Thread(target=execute_sync_task,args=("worker-1",6))
# thread2 =Thread(target=execute_sync_task,args=("worker-2",2))
# thread3 =Thread(target=execute_sync_task,args=("worker-3",3))
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread3.join()
# print("End Thread")


# def execute_sync_task(task_name:str, duration:int):
#     print(f"Starting task - {task_name}")
#     time.sleep(duration)
#     print(f"Ending task {task_name}")
#
# def main():
#     thread1 = threading.Thread(target=execute_sync_task, args=("Task 1", 5))
#     thread2 = threading.Thread(target=execute_sync_task, args=("Task 2", 2))
#     thread3 = threading.Thread(target=execute_sync_task, args=("Task 3", 1))
#
#     thread1.start()
#     thread2.start()
#     thread3.start()
#
# def main_threadpool():
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         executor.submit(execute_sync_task, "Task 1", 10)
#         executor.submit(execute_sync_task, "Task 2", 2)
#         executor.submit(execute_sync_task, "Task 3", 3)
#
# main_threadpool()

#main()

# def execute_sync_task(task_name:str, duration:int):
#     print(f"Starting task - {task_name}")
#     time.sleep(duration)
#     print(f"Ending task {task_name}")
#
# def main():
#     execute_sync_task("Task 1", duration=5)
#     execute_sync_task("Task 2", duration=2)
#     execute_sync_task("Task 3", duration=3)
#
#
# main()

import asyncio
async def execute_sync_task2(task_name:str, duration:int): #corouting function
    print(f"Starting task - {task_name}")
    for i in range(10):
        if i == 1:
            await asyncio.sleep(0.00001)
        print(i)
    print(f" Ending task {task_name}")

async def execute_sync_task(task_name:str, duration:int): #corouting function
    print(f"Starting task - {task_name}")
    await asyncio.sleep(duration)
    print(f" Ending task {task_name}")

async def async_main():
    await asyncio.gather(
        execute_sync_task2("task 1", 5),
        execute_sync_task("task 2", 2),
        execute_sync_task("task 3", 1)
    )
    print("Hello world")

asyncio.run(async_main()) #initiate our event loop