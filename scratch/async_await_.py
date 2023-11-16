# https://www.youtube.com/watch?v=t5Bo1Je9EmE
import asyncio
import time

def part1():
    async def t1():
        print("test 1")
        task = asyncio.create_task(t2())
        await asyncio.sleep(0.5)
        print('finished')
        await task

    async def t2():
        print("idfk")
        await asyncio.sleep(2)
        print("finished task func")
    
    asyncio.run(t1())

# part1()


def part2():
    async def fetch_data():
        print("fetching data...")
        await asyncio.sleep(2)
        print("done fetching")
        return {"data": 10}

    async def print_nums():
        for i in range(10):
            print(i)
            await asyncio.sleep(0.25)
    
    async def main():
        task1 = asyncio.create_task(fetch_data())
        task2 = asyncio.create_task(print_nums())

        value = await task1
        print(value)
        await task2

    asyncio.run(main())

part2()
