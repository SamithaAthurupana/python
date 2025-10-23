import asyncio


async def process_numbers(a:int, b:int, duration:int):
    print(f"Adding numbers {a} + {b}")
    await asyncio.sleep(duration)
    return a + b

async def main():

    tasks = [process_numbers(3,4,5),
             process_numbers(5,8,3),
             process_numbers(6,5,2)]


    results = await asyncio.gather(*tasks)

    print(results)

async def main_background():
    task1 = asyncio.create_task(process_numbers(3,3,3))
    task2 = asyncio.create_task(process_numbers(4, 3, 4))

    result1 = await task1
    result2 = await task2
    print(result1, result2)
    
asyncio.run(main_background())
#asyncio.run(main())
