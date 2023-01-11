import asyncio


async def main():
    await asyncio.sleep(0.1)
    return 1


async def main_2():
    await asyncio.sleep(0.1)
    return 2


async def main_3():
    await asyncio.sleep(0.1)
    return 3


async def main_4():
    await asyncio.sleep(0.1)
    return 4


async def squarer(n):
    for i in range(n):
        yield i**2
        await asyncio.sleep(0.1)


async def async_comprehension():
    print([i async for i in squarer(5)])  # async for inside list comprehension
    func_lst = [main, main_2, main_3, main_4]
    print([await func() for func in func_lst])  # await inside list comprehension


asyncio.run(async_comprehension())
